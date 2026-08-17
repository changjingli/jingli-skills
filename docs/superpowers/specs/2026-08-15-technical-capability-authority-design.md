# Solution-to-Frontend Evidence-Gated State Machine Design

Status: design direction approved; written revision awaiting review
Date: 2026-08-17
Scope: `skills/solution-to-frontend`

## Problem

The existing workflow lists a sequence of stages and assigns each stage a coarse status. That describes the happy path, but it does not model the events and failure states that determine whether work may safely advance.

In particular, `active`, `awaiting_approval`, `blocked`, `approved`, and `superseded` conflate four different concerns:

- the lifecycle of the overall workflow;
- the execution state of the active stage;
- the validity and approval state of its artifacts;
- the state of child agents and companion skills.

This makes a formally compliant but operationally invalid transition possible. A child task can finish, a screenshot can exist, and automated tests can pass while the composed experience has never been reviewed in the target runtime. The process records artifacts but cannot prove that the evidence authorizes the next kind of work.

The missing concept is therefore broader than a Pro Components recommendation or another checklist item. `solution-to-frontend` needs a parent-owned, evidence-gated, recoverable state machine.

## Observed Baseline Failure

A real implementation exposed the baseline behavior before this design change:

- an approved complete back-office experience was decomposed into isolated code modules;
- host routing, layout, global styles, authentication, and legacy boundaries were discovered late;
- a mature component system was assembled mechanically without proving the whole operator workflow;
- adapters, state, tests, and local components were built before the complete static composition was reviewed;
- isolated tests passed while the target route and full viewport remained invalid;
- no single owner was accountable for the composed page;
- artifact and test completion was mistaken for authorization to expand.

These are baseline observations, not reusable project requirements. Literal routes, component products, viewport sizes, and domain semantics belong in project-generated acceptance contracts. The reusable skill must encode the general failure pattern.

## Outcome

The revised skill will:

- distinguish the happy-path phase sequence from the state machine that governs it;
- require target-runtime and integration evidence before visual production;
- require a complete composition proof before behavior and scale work expand;
- model clarification, rejection, remediation, retry, pause, cancellation, invalidation, recovery, and cleanup failure;
- keep artifacts, approvals, evidence, and executor runs as separate state dimensions;
- make the parent orchestrator and an experience integration owner accountable for whole-experience coherence;
- use Superpowers and Impeccable as bounded child protocols whose completion never advances the parent state by itself.

## Happy-Path Phase Sequence

The phase sequence remains useful as a map, but it is not the state machine:

```text
BOOTSTRAP
  -> INTAKE
  -> CONTENT
  -> TECHNICAL_BASELINE
  -> VISUAL_DIRECTION
  -> COMPOSITION_PROOF
  -> REPRESENTATIVE_V0
  -> SCALE_DELIVERY
  -> COMPLETE
```

The two boundaries that were previously missing are:

- `TECHNICAL_BASELINE`: prove the target runtime, integration impact, and capability architecture before visual production;
- `COMPOSITION_PROOF`: prove one complete representative composition in the target runtime before implementing deeper behavior or replicating surfaces.

## Orthogonal State Model

One status field cannot represent the workflow. `progress.md` records six orthogonal dimensions.

| Dimension | States | Purpose |
|---|---|---|
| Workflow lifecycle | `NEW`, `BOOTSTRAPPING`, `RECOVERING`, `RUNNING`, `INVALIDATING`, `PAUSED`, `CANCELLING`, `BLOCKED`, `COMPLETING`, `CLEANING_UP`, `CLEANUP_FAILED`, `COMPLETE`, `CANCELLED` | Describes the parent workflow |
| Stage execution | `WORKING`, `EXECUTOR_RUNNING`, `VERIFYING`, `AWAITING_APPROVAL`, `NEEDS_CLARIFICATION`, `RETRYABLE_FAILED`, `REMEDIATING` | Describes work inside the current phase |
| Artifact validity | `MISSING`, `DRAFT`, `QUALIFIED`, `SUPERSEDED` | Describes whether each formal artifact is usable against current upstream decisions |
| Evidence status | `MISSING`, `INCOMPLETE`, `QUALIFIED`, `DEGRADED`, `STALE`, `INVALID` | Describes whether evidence satisfies the active gate |
| Approval status | `NOT_REQUESTED`, `PENDING`, `GRANTED`, `REJECTED`, `CHANGES_REQUESTED` | Describes the accountable stakeholder's decision against a qualified artifact and evidence set |
| Executor run | `IDLE`, `RUNNING`, `CANCELLING`, `RETURNED`, `FAILED`, `TIMED_OUT` | Describes each child agent or companion-skill invocation |

Approval is recorded against a qualified artifact and evidence set. It is not inferred from the stage execution state or stored as artifact validity. `SUPERSEDED` describes an artifact, not the current workflow lifecycle.

## Parent Lifecycle State Machine

```text
NEW
  `- workflow.started -> BOOTSTRAPPING

BOOTSTRAPPING
  |- progress.absent -> RUNNING.INTAKE.WORKING
  |- progress.found -> RECOVERING
  `- progress.invalid -> BLOCKED(recovery)

RECOVERING
  |- evidence.reconciled -> RUNNING.<resolved-stage>.<resolved-state>
  |- evidence.stale -> INVALIDATING
  |- state.ambiguous -> RUNNING.<owning-stage>.NEEDS_CLARIFICATION
  `- recovery.failed -> BLOCKED(recovery)

RUNNING
  |- upstream.changed -> INVALIDATING
  |- user.paused -> PAUSED
  |- workflow.cancelled -> CANCELLING
  |- unrecoverable.blocker -> BLOCKED
  `- acceptance.approved -> COMPLETING

INVALIDATING
  |- executors.running -> CANCELLING
  `- downstream.superseded -> RUNNING.<owning-stage>.REMEDIATING

PAUSED
  `- workflow.resumed -> RECOVERING

CANCELLING
  |- executors.stopped + workflow.cancelled -> CANCELLED
  |- executors.stopped + upstream.changed -> INVALIDATING
  `- stop.failed -> BLOCKED(cancellation)

BLOCKED
  |- blocker.resolved -> RECOVERING
  |- workflow.cancelled -> CANCELLING
  `- user.paused -> PAUSED

COMPLETING
  |- formal_state.incomplete -> RUNNING.SCALE_DELIVERY.REMEDIATING
  |- reconciliation.succeeded -> CLEANING_UP
  `- reconciliation.failed -> BLOCKED(completion)

CLEANING_UP
  |- progress.deleted -> COMPLETE
  `- cleanup.failed -> CLEANUP_FAILED

CLEANUP_FAILED
  |- cleanup.retried -> CLEANING_UP
  `- user.paused -> PAUSED
```

`PAUSED`, `BLOCKED`, and `CANCELLED` retain `progress.md`. Only successful reconciliation and cleanup produce `COMPLETE` and delete the temporary file.

## Stage Sub-State Machine

Every implementation-bound phase uses the same sub-state contract:

```text
WORKING
  |- executor.dispatched -> EXECUTOR_RUNNING
  |- activity.completed -> VERIFYING
  |- meaning.ambiguous -> NEEDS_CLARIFICATION
  `- work.failed -> RETRYABLE_FAILED

EXECUTOR_RUNNING
  |- executor.returned -> VERIFYING
  |- executor.needs_context -> NEEDS_CLARIFICATION
  |- executor.failed -> RETRYABLE_FAILED
  |- executor.timed_out -> RETRYABLE_FAILED
  `- scope.changed | user.cancelled -> CANCELLING

VERIFYING
  |- evidence.qualified -> AWAITING_APPROVAL
  |- evidence.incomplete -> WORKING
  |- evidence.invalid -> REMEDIATING
  |- evidence.stale -> WORKING
  `- review.failed -> REMEDIATING

AWAITING_APPROVAL
  |- approval.granted + next_phase.exists -> NEXT_STAGE.WORKING
  |- approval.granted + final_acceptance -> COMPLETING
  |- approval.rejected -> REMEDIATING
  |- changes.requested -> REMEDIATING
  |- upstream.changed -> INVALIDATING
  `- no.response -> AWAITING_APPROVAL

NEEDS_CLARIFICATION
  |- clarification.received -> WORKING
  |- clarification.changes_scope -> INVALIDATING
  `- user.paused -> PAUSED

RETRYABLE_FAILED
  |- retry.requested -> WORKING
  |- workaround.selected -> WORKING
  |- dependency.unavailable -> BLOCKED
  `- workflow.cancelled -> CANCELLING

REMEDIATING
  |- remediation.completed -> VERIFYING
  |- root_cause.upstream -> INVALIDATING
  `- remediation.failed -> RETRYABLE_FAILED
```

A child return event can move only from `EXECUTOR_RUNNING` to `VERIFYING`. A child recommendation, local approval, passing test, or completed checklist cannot transition the parent to the next phase.

## Transition Contract

Every transition definition contains:

| Field | Requirement |
|---|---|
| Event | Observable event that requests the transition |
| Source | Exact lifecycle, stage, and sub-state |
| Guard | Predicate that must be true |
| Effects | Artifacts, executor actions, ledger entries, or invalidations produced |
| Destination | Exact next state |
| Recovery | State and action used when the effect fails |

Advancing to the next phase requires all of the following:

- required activity was performed;
- formal artifact exists;
- evidence satisfies the phase-specific evidence contract;
- evidence provenance and freshness are known;
- accountable stakeholder explicitly approved the bounded decision;
- no upstream artifact or required evidence is `SUPERSEDED` or stale;
- no load-bearing executor or review finding remains unresolved.

An artifact is a container, not proof by itself. A screenshot, test report, preview, or document qualifies only when its scope, source, target runtime, relevant configuration, and freshness satisfy the active gate.

## Phase Gates and Formal Artifacts

| Phase | Formal artifacts | Gate decision |
|---|---|---|
| `INTAKE` | `00-intake.md`, `01-outcome.md` | Value goal, audience, scope, facts, and assumptions approved |
| `CONTENT` | `02-content-design.md` | Journey, surface responsibilities, data semantics, states, and workflow approved |
| `TECHNICAL_BASELINE` | `technical-capability.md` | Target runtime, integration impact, concern inventory, and `Reuse / Adopt / Build` decisions approved |
| `VISUAL_DIRECTION` | `03-visual-brief.md`, design authority, rendered visual evidence | Complete visual and interaction direction approved |
| `COMPOSITION_PROOF` | `composition-proof.md`, runnable representative composition, whole-experience evidence | Complete composition works in the target runtime and is approved for behavior implementation |
| `REPRESENTATIVE_V0` | `04-v0.md`, runnable core journey, behavior and state evidence | Representative workflow and material states approved for replication |
| `SCALE_DELIVERY` | `05-scale-plan.md`, `06-acceptance.md` | Remaining surfaces, reuse boundaries, QA evidence, and readiness approved |

No phase may be skipped because a downstream-looking artifact already exists. The artifact must be reconciled against the current upstream decisions and current evidence contract.

## Technical Baseline Authority

`TECHNICAL_BASELINE` combines two related proofs without turning a project-specific host audit into a universal checklist.

### Target Runtime and Integration Impact

For every implementation-bound V0, record the material target-runtime contract and incumbent integration risks. Applicable concerns include:

- application and rendering model;
- canonical navigation and route behavior;
- layout and application-shell ownership;
- styling, tokens, resets, themes, and style precedence;
- authentication, permission, and redirect context;
- legacy coexistence, migration, isolation, and rollback boundaries;
- build, deployment, review runtime, device, and input constraints;
- evidence invalidation triggers when runtime configuration or code changes.

Projects decide the concrete values. The reusable skill never hard-codes a route, viewport, CSS rule, product component, or domain label.

### Capability Architecture

Inventory material concerns individually:

- application framework and rendering model;
- styling and tokens;
- accessible UI primitives;
- domain or operations workflow components;
- navigation and application shell;
- tables, forms, validation, charts, maps, and specialized surfaces;
- data adapters, state, and mock/API boundaries;
- authentication, permissions, and workflow states;
- unit, interaction, end-to-end, visual, and review-runtime testing.

Each concern is graded `Absent`, `Present but weak`, or `Established and capable`, then receives a `Reuse`, `Adopt`, or `Build` decision. Package presence, utility CSS, repeated ad hoc controls, or a few existing pages do not prove a capable system. `Build` requires concrete incompatibility with viable reuse and adoption candidates.

Candidate routing is conditional. For example, a complex React back-office workflow must evaluate Ant Design Pro Components, but a Vue workflow, a simple settings surface, or an established capable alternative follows its own evidence. Candidate evaluation does not force selection.

## Visual Direction and Composition Proof

Text is not visual evidence. A written specification, component inventory, or brainstorming summary cannot satisfy `VISUAL_DIRECTION` without a rendered artifact that communicates the complete intended experience.

Visual approval authorizes only `COMPOSITION_PROOF`. It does not authorize full behavior implementation or multi-surface replication.

`COMPOSITION_PROOF` is the first implementation unit. It must:

- represent one complete surface or journey frame rather than isolated components;
- run in the project-defined target runtime and integration context;
- include the application frame, hierarchy, context, actions, and primary content needed to judge the experience;
- use only the minimum fixtures and behavior needed to expose the complete composition;
- provide whole-experience evidence at project-defined review conditions;
- demonstrate that a user can understand where they are, what matters, and what they can do next;
- receive explicit approval before deeper state, adapter, behavior, or replication work expands.

For an operations interface this may be a complete application shell and representative work surface. For a dashboard, H5 flow, mini program, editor, or native application, the project defines the equivalent complete composition. The skill prescribes the proof obligation, not a universal layout.

## Experience Ownership and Work Decomposition

`solution-to-frontend` owns process state. One named `Experience Integration Owner` owns the coherence of the complete experience; the parent agent assumes this role unless the project names another accountable owner.

Before `COMPOSITION_PROOF` approval:

- the complete representative composition is the acceptance unit;
- visually coupled pieces are not dispatched as independently approvable modules;
- parallel child implementation is prohibited;
- local component, adapter, and state completion cannot substitute for whole-experience review.

After approval, implementation tasks are organized by vertical experience slice or complete workflow outcome where possible. Infrastructure tasks may support a slice, but they are not the user-facing acceptance unit. Every material integration returns to whole-experience review.

## Failure Routing

Review failures return to the earliest authority that owns the root cause:

| Failure | Return state |
|---|---|
| Wrong value goal, audience, or scope | `INTAKE.REMEDIATING` |
| Wrong journey, content, data meaning, state, or workflow | `CONTENT.REMEDIATING` |
| Wrong runtime contract, integration boundary, or capability choice | `TECHNICAL_BASELINE.REMEDIATING` |
| Wrong visual hierarchy, interaction direction, or visual language | `VISUAL_DIRECTION.REMEDIATING` |
| Whole composition or target-runtime integration fails | `COMPOSITION_PROOF.REMEDIATING` |
| Core behavior, recovery, permission, or material state fails | `REPRESENTATIVE_V0.REMEDIATING` |
| Replication, regression, packaging, or final acceptance fails | `SCALE_DELIVERY.REMEDIATING` |

Use `superpowers:systematic-debugging` after a test, review, or runtime failure. Repeated local remediation that reveals cross-stage assumptions triggers `root_cause.upstream`, not another local patch.

## Invalidation Propagation

An approved upstream change enters `INVALIDATING`; it does not silently edit downstream artifacts in place.

| Changed authority | Mark `SUPERSEDED` |
|---|---|
| Intake/outcome | Content, technical baseline, visual direction, composition proof, V0, scale and acceptance |
| Content | Technical baseline, visual direction, composition proof, V0, scale and acceptance |
| Technical baseline | Visual direction where affected, composition proof, V0, scale and acceptance |
| Visual direction | Composition proof, V0, scale and acceptance |
| Composition proof | V0, scale and acceptance |
| Representative V0 | Scale and acceptance |

Before invalidation mutates artifacts, the parent requests cancellation of affected running executors. If cancellation fails, the workflow enters `BLOCKED(cancellation)` rather than allowing stale work to merge.

Evidence can also become stale without a formal decision change. Each project-generated acceptance contract names material freshness triggers, such as a relevant runtime configuration, application frame, selected system, or reviewed build changing. Stale evidence returns to `VERIFYING` or `WORKING`; it does not automatically invalidate unrelated upstream decisions.

## Companion Skill Semantics

Superpowers supplies local engineering protocols; Impeccable supplies bounded visual execution and review. Neither owns the parent lifecycle.

- `impeccable:init` may establish product design context inside the active phase.
- Impeccable visual generation, critique, audit, and polish return evidence to the parent.
- `superpowers:test-driven-development` governs approved behavior changes.
- `superpowers:systematic-debugging` governs unexpected failures.
- `superpowers:verification-before-completion` verifies claims with fresh evidence.
- Inside an active `solution-to-frontend` delivery, `superpowers:writing-plans` is allowed only after `REPRESENTATIVE_V0` approval, for `SCALE_DELIVERY`. This does not prevent maintainers from writing an implementation plan for the skill repository itself after this design specification is approved.
- `superpowers:subagent-driven-development` may execute an approved plan, but its task completion and code-review gates do not replace parent composition or V0 gates.

If generic `superpowers:brainstorming` recommends `writing-plans`, its local terminal state is treated as `executor.returned`. The parent moves to `VERIFYING`, evaluates its own gate, and ignores the recommendation when visual, composition, or V0 evidence is missing.

Unavailable companion skills use the documented fallback. `degraded` is a disclosure, not a passing state. The fallback must still satisfy the parent evidence contract, and material limitations require explicit stakeholder disposition.

## Temporary Progress and Recovery

`progress.md` is workspace-local temporary state, created from `assets/progress-template.md`, and never becomes the source of truth for approved facts.

It records:

- workflow lifecycle;
- current phase and stage sub-state;
- next expected event and exact resume action;
- formal artifacts with independent validity and approval references;
- evidence status with source, scope, runtime, freshness, and limitations;
- executor runs with identity, status, outputs, retry count, and cancellation state;
- blockers, clarification requests, and remediation attempts;
- tentative decisions and their formal promotion targets;
- invalidation events and downstream artifacts marked `SUPERSEDED`.

At startup, the parent reconciles the ledger against formal artifacts, git/workspace state, running executors where observable, and current evidence. It never trusts a claimed stage solely because it appears in `progress.md`.

Completion first reconciles every tentative decision, approval, artifact, limitation, and acceptance item. Only then does cleanup delete `progress.md`. Cleanup failure produces `CLEANUP_FAILED`, preserving a recoverable record rather than falsely reporting `COMPLETE`.

## Test Architecture

Skill tests follow three layers so reusable policy does not absorb one project's literals.

### Core Workflow Invariants

These apply to every implementation-bound workflow:

- child completion returns to parent verification and cannot advance a phase;
- incomplete, invalid, stale, or unapproved evidence blocks advancement;
- complete composition evidence is required before deeper implementation expands;
- isolated success cannot substitute for whole-experience evidence;
- upstream change stops affected executors and supersedes dependent artifacts;
- pause, retry, cancellation, recovery, and cleanup preserve consistent state;
- only successful reconciliation and cleanup produce `COMPLETE`.

### Conditional Stack Scenarios

These load only when observable predicates match:

- an existing framework without a capable component system still triggers capability evaluation;
- a complex React operations workflow evaluates Pro Components;
- an established capable alternative compares migration and coexistence cost;
- platform-incompatible or disproportionate candidates are excluded with evidence;
- selected component systems trigger their relevant integration checks without making those checks universal.

### Project-Generated Acceptance Checks

Each project records concrete values in its formal artifacts, such as canonical route, review runtime, viewport, device, authentication state, selected component system, content comprehension criteria, and evidence freshness triggers. Tests validate that these fields exist and are used; the reusable skill does not prescribe their literal values.

## Forward Scenarios

The edited skill must route at least these scenarios correctly:

| Scenario | Expected behavior |
|---|---|
| Written design is approved but no rendered visual evidence exists | Remain in `VISUAL_DIRECTION`; planning is blocked |
| Rendered direction exists but no complete target-runtime composition exists | Enter or remain in `COMPOSITION_PROOF`; deeper implementation is blocked |
| Isolated preview passes while the project-defined target runtime fails | Composition evidence is invalid; return to remediation |
| Local tasks pass but whole-experience evidence is absent | Parent gate remains blocked regardless of task status |
| Evidence refers to a stale or unidentified build | Return to `WORKING` or `VERIFYING`; approval cannot reuse stale evidence |
| Whole-experience review fails after downstream work exists | Enter `INVALIDATING`; mark dependent V0 and scale artifacts `SUPERSEDED` |
| Scope changes while a child executor is running | Cancel affected executor before invalidation and resume at the owning phase |
| Executor times out | Enter `RETRYABLE_FAILED`; retry must use recorded attempt and workspace evidence |
| Clarification changes an approved upstream decision | Enter `INVALIDATING`, not local remediation |
| Formal acceptance succeeds but progress cleanup fails | Enter `CLEANUP_FAILED`, not `COMPLETE` |
| Complex React operations workflow lacks a capable system | Evaluate Pro Components as a conditional candidate |
| Platform or scope makes that candidate unsuitable | Exclude it with evidence without changing the global workflow |

## Planned File Changes

### `SKILL.md`

- Rebuild as a thin parent coordinator over lifecycle, phase routing, evidence gates, and child-return semantics.
- Distinguish phase flow from state-machine state.
- Load and reconcile `progress.md` before acting.
- Make `TECHNICAL_BASELINE` and `COMPOSITION_PROOF` hard authorization boundaries.
- Name the parent as default experience integration owner.

### `references/workflow-protocol.md`

- Define lifecycle states, stage sub-states, events, guards, effects, recovery, and invalidation.
- Define executor cancellation and child-return behavior.

### `assets/progress-template.md` and validator

- Store the six orthogonal state dimensions.
- Validate legal state combinations, required recovery targets, executor attempts, evidence provenance, promotion targets, and cleanup conditions.

### Stage playbooks

- Give every phase explicit inputs, activity, evidence contract, approval, failure routing, and next legal transition.
- Add dedicated `technical-baseline` and `composition-proof` playbooks.

### Capability and integration policies

- Preserve concern-by-concern `Reuse / Adopt / Build` and conditional candidate routing.
- Add target-runtime, integration-impact, evidence-freshness, and project-generated acceptance contracts.

### Companion adapters

- Treat child completion as a parent verification event.
- Keep Superpowers leaf protocols and Impeccable visual work bounded by the active phase.

### Regression tests

- Test legal and illegal transitions, recovery, invalidation, cancellation, retry, cleanup, and child-return behavior.
- Separate core invariants, conditional stack scenarios, and project-generated acceptance fixtures.
- Use the observed implementation failure as a baseline pressure scenario without copying its project literals into global policy.

## Acceptance Criteria

- The happy-path sequence is explicitly distinguished from the state machine.
- Workflow lifecycle, stage execution, artifact validity, evidence status, approval status, and executor state are represented independently.
- Every transition has an event, source, guard, effects, destination, and recovery path.
- `TECHNICAL_BASELINE` covers target-runtime integration and capability architecture without hard-coding project values.
- `COMPOSITION_PROOF` blocks deeper behavior and replication until a complete representative composition passes in the project-defined runtime.
- One experience integration owner is accountable for whole-experience coherence.
- Child completion cannot advance the parent phase.
- Review rejection, clarification, retryable failure, pause, cancellation, invalidation, recovery, and cleanup failure have defined semantics.
- Upstream changes cancel affected executors before superseding dependent artifacts.
- Evidence provenance and freshness are required for approval.
- Superpowers remains a local engineering protocol, not the parent workflow.
- `progress.md` is retained for interruption and failure and deleted only after successful completion reconciliation.
- Tests distinguish core invariants, conditional policies, and project-generated acceptance values.
- The existing implementation plan is not executed until it is rewritten against this specification and explicitly reviewed.
