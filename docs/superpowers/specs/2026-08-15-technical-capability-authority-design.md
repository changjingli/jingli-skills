# Technical Capability Authority Design

Status: approved in conversation, awaiting written-spec review
Date: 2026-08-15
Scope: `skills/solution-to-frontend`

## Problem

The workflow treats `technical-baseline.md` as a fallback for projects without an evidenced frontend stack. This conflates the presence of an application framework or styling tool with a complete, capable frontend architecture.

A project with Next.js, React, and Tailwind can therefore bypass evaluation of UI primitives, admin workflow components, tables, forms, charts, data adapters, tests, and review runtime. Design brainstorming then starts without an approved implementation boundary and may propose custom components where a mature domain system should have been evaluated.

The missing concept is not a Pro Components recommendation. It is a first-class technical capability authority between approved content and visual production.

## Outcome

The skill will require an evidence-backed capability architecture for every implemented V0, including projects that already have a framework or CSS system.

The revised stage sequence is:

```text
Outcome
  -> Content and workflow requirements
  -> Technical capability architecture
  -> Visual direction and reviewable design evidence
  -> Representative runnable V0
  -> Scale implementation plan and delivery
```

No visual ideation or V0 implementation may begin until the material technical capabilities have an approved `Reuse`, `Adopt`, or `Build` decision. No scale implementation plan may begin until the representative V0 has been reviewed and approved.

## Workflow State and Temporary Progress

The workflow is modeled as a parent-owned state machine:

```text
BOOTSTRAP
  -> INTAKE
  -> CONTENT
  -> CAPABILITY
  -> VISUAL_DIRECTION
  -> REPRESENTATIVE_V0
  -> SCALE_DELIVERY
  -> COMPLETE
```

Each stage uses one of these statuses: `active`, `awaiting_approval`, `blocked`, `approved`, or `superseded`. A transition requires all three evidence classes:

- `Activity`: the stage work was actually performed;
- `Artifact`: the formal artifact and reviewable evidence exist;
- `Commitment`: the accountable stakeholder explicitly approved the gate.

The transition record is kept in a temporary workspace file, `progress.md`. It is not a formal project artifact and is not a source of truth for product facts or approved decisions. Formal facts and decisions must be promoted into their stage-owned files.

At startup, the orchestrator reads `progress.md` if present, reconciles it against formal artifacts and approvals, and downgrades any progress claim that lacks evidence. A child skill may append a result to the progress record, but only the parent orchestrator may update the current stage or satisfy a gate.

The temporary file contains only:

- current stage and status;
- next gate and exact recovery action;
- missing evidence and blockers;
- tentative decisions and their promotion targets;
- child-skill invocations and returned artifacts;
- invalidated downstream artifacts after an upstream change.

When the workflow reaches `COMPLETE`, the orchestrator first verifies that every tentative decision was promoted or closed, all formal artifacts and approvals are present, and the acceptance package is complete. It then deletes `progress.md`. An interrupted workflow retains it for recovery; it is never deleted merely because a child skill reports completion.

`progress.md` is created from `assets/progress-template.md`, remains workspace-local during execution, and is not committed as a project artifact.

## Gate and Invalidation Rules

The formal artifacts and minimum transition conditions are:

| Stage | Formal artifacts | Transition condition |
|---|---|---|
| `INTAKE` | `00-intake.md`, `01-outcome.md` | Value goal, audience, scope, facts, and assumptions approved |
| `CONTENT` | `02-content-design.md` | Journey, surfaces, data semantics, states, and workflow approved |
| `CAPABILITY` | `technical-capability.md` | Concern inventory, evidence grades, `Reuse / Adopt / Build`, candidates, and technical approach approved |
| `VISUAL_DIRECTION` | `03-visual-brief.md`, design authority, rendered preview or screenshots | Visual direction is reviewable and approved |
| `REPRESENTATIVE_V0` | `04-v0.md`, runnable preview, runtime evidence | High-risk representative slice passes checks and is approved |
| `SCALE_DELIVERY` | `05-scale-plan.md`, `06-acceptance.md` | Reuse boundaries, QA evidence, review package, and readiness approval complete |

An approved upstream change invalidates downstream decisions without deleting their files:

| Changed stage | Mark superseded |
|---|---|
| Outcome | Content, Capability, Visual, V0, Scale |
| Content | Capability, Visual, V0, Scale |
| Capability | Visual, V0, Scale |
| Visual direction | V0, Scale |
| Representative V0 | Scale and acceptance |

The orchestrator returns to the owning stage and records the invalidation in `progress.md`. It never silently reuses a downstream artifact whose inputs are superseded.

## Authority Model

The workflow distinguishes four authorities:

| Authority | Question answered | Primary artifact |
|---|---|---|
| Product/outcome | Why, for whom, and what success means | Existing intake and outcome artifacts |
| Content | What each surface communicates or enables | `02-content-design.md` |
| Technical capability | Which proven capabilities will carry the workflow | `technical-capability.md` |
| Visual | How the approved content and capabilities should be understood and operated, proven by a reviewable visual artifact | `03-visual-brief.md`, project design authority, and preview/screenshots |

`technical-capability.md` is independent rather than embedded in content or visual artifacts. Its stable unnumbered name avoids renumbering existing project artifacts and makes it reusable across later stages.

## Capability Inventory

Before content approval can enable visual production, inventory these concerns when material to the confirmed workflow:

- application framework and rendering model;
- styling and tokens;
- accessible UI primitives;
- operations/admin workflow components;
- navigation and application shell;
- tables and data grids;
- forms and validation;
- charts, maps, and other domain visualization;
- data adapters, state, and mock/API boundaries;
- authentication, permissions, and workflow states;
- unit, interaction, end-to-end, and visual testing;
- customer review runtime and deployment constraints.

Each concern receives an evidence grade:

| Grade | Meaning |
|---|---|
| Absent | No relevant capability is evidenced |
| Present but weak | Ad hoc, incomplete, duplicated, untested, or unable to cover the confirmed workflow |
| Established and capable | Shared, evidenced, maintained, and sufficient for the confirmed workflow |

Package presence alone is not capability evidence. A framework, utility CSS library, a few custom pages, or repeated ad hoc controls does not prove that a component or workflow system is established and capable.

## Reuse / Adopt / Build Decision

Every material concern receives one decision:

- `Reuse`: the incumbent capability is established, capable, and compatible with the confirmed workflow.
- `Adopt`: a mature ecosystem capability fits better than extending the incumbent implementation.
- `Build`: the workflow is sufficiently specialized that incumbent and mature candidates have concrete incompatibilities.

Custom construction is a positive architecture decision, not the default produced by missing evidence. A `Build` decision must name the incompatibility that prevents `Reuse` or `Adopt`.

The project artifact uses this required shape:

```markdown
## Technical Capability Decision

| Concern | Required capability | Incumbent evidence and grade | Reuse/Adopt/Build | Candidates compared | Selected solution | Rationale and boundary |
|---|---|---|---|---|---|---|
```

The artifact also records review runtime, migration cost, compatibility, accessibility, rendering/SSR constraints, bundle implications, theming, production reuse, rejected alternatives, approver, and approval date.

## Domain-Matched Candidate Routing

Candidate evaluation is conditional on observable workflow and platform evidence.

For React back-office workflows containing material list, search, filter, detail, edit, permission, batch-action, or approval behavior, Ant Design Pro Components is a required candidate. Evaluation must cover relevant components such as ProTable, ProForm, ProDescriptions, ProLayout, and ProCard.

This rule does not force selection:

- an established Ant Design admin surface normally reuses Ant Design and evaluates incremental Pro Components adoption;
- an established shadcn-based table, form, and shell system compares migration and coexistence cost before adopting Ant Design;
- a Vue application does not evaluate the React-only Pro Components implementation;
- two simple settings forms do not trigger a large admin framework solely because the product is called a back office;
- a specialized canvas or editor may reuse a mature admin shell while building the domain-specific editing surface.

Tailwind alone is never a reason to reject Pro Components. Rejection requires a concrete incompatibility or an established capable alternative.

## Stage Gates

The main skill adds this non-negotiable gate:

```text
No approved technical capability architecture -> no visual ideation or V0 implementation
No reviewable visual artifact                  -> no visual approval
No approved representative V0                 -> no scale implementation plan
```

The content stage defines workflow capabilities and material states. The technical capability stage then evaluates implementation approaches. The visual stage consumes the approved decision and may refine visual integration, but it may not silently reopen or replace the selected component architecture.

Before the representative V0 is drawn, compare the applicable approaches:

1. Extend the incumbent component system.
2. Adopt a domain-matched mature system.
3. Build project-specific components.

Only applicable approaches must be evaluated; a platform-incompatible candidate is excluded with evidence. The comparison records compatibility, reuse, accessibility, rendering/SSR, bundle, theming, migration, and production-reuse trade-offs. The accountable stakeholder approves the selected approach before visual production.

Text is not visual evidence. A content matrix, layout description, component inventory, wireframe narrative, brainstorming summary, or written design specification cannot satisfy the visual gate by itself. The gate requires something the stakeholder can inspect as the intended interface: a rendered mockup, browser preview, or equivalent target-platform artifact at representative dimensions. For interaction-heavy work, it must demonstrate the material states and transitions needed to judge the direction.

The visual direction gate and representative V0 gate remain distinct. Direction approval authorizes building the selected high-risk slice; V0 approval authorizes replication and scale planning.

## Parent Workflow Sovereignty

`solution-to-frontend` owns stage state and gate transitions. Companion skills execute bounded work inside the active stage; they never decide that the parent workflow may advance.

If a host invokes `superpowers:brainstorming` despite this workflow's adapter policy, completion of that skill means only that its local discovery/specification task is complete and control returns to `solution-to-frontend`. It does not imply that visual direction, visual evidence, the representative V0, or customer-review readiness is approved.

After every companion skill returns, the orchestrator re-evaluates the parent gates from concrete artifacts and recorded approvals. A companion skill's recommended next action is advisory and is ignored when it conflicts with the active parent stage.

In particular, the generic brainstorming transition to `superpowers:writing-plans` is intercepted when visual evidence or V0 approval is missing. The workflow resumes the visual stage, produces the required reviewable artifact, obtains the corresponding approval, and only then advances.

## Companion Skill Contract

Impeccable visual work, approved Superpowers engineering leaf skills, `superpowers:writing-plans`, and V0 implementation consume the approved `technical-capability.md` as an input.

They may explore interaction, composition, and visual direction within its boundaries. They may not replace an approved `Reuse` or `Adopt` decision with custom components without returning to the technical capability gate, recording new evidence, and obtaining approval.

If a companion skill starts before the capability decision exists, the solution workflow pauses it at the technical capability gate rather than allowing unconstrained UI generation.

Superpowers is used as a source of engineering discipline, not as a second parent workflow. Do not compose its meta-workflow or brainstorming state machine into the pre-V0 stages. Use only the named leaf skills at explicit triggers: TDD for behavior changes, systematic debugging after failures, verification before claims, and `writing-plans` only in `SCALE_DELIVERY` after representative V0 approval. The visual stage may maintain a bounded build checklist for the representative slice, but that checklist is not the production or multi-screen implementation plan.

## File Changes

### `SKILL.md`

- Replace the single “no frontend stack” condition with an always-run concern inventory.
- Load `technical-baseline.md` whenever any material concern is absent, weak, or not evidenced.
- Add the technical capability authority to the stage sequence and non-negotiable gates.
- Clarify that incumbent conventions are preserved only when established and capable for the confirmed workflow.
- Require companion skills to consume the approved technical capability artifact.
- Declare parent workflow sovereignty and re-check parent gates after every companion skill returns.
- Move `superpowers:writing-plans` from pre-V0 implementation to post-V0 scale/delivery planning.
- Require reviewable visual evidence rather than accepting textual design output as visual approval.
- Make `solution-to-frontend` the sole parent orchestrator and state owner.
- Load, reconcile, update, and clean up temporary `progress.md` according to the state protocol.
- Treat Superpowers as leaf engineering practices rather than a competing workflow orchestrator.

### `references/technical-baseline.md`

- Expand its applicability beyond greenfield projects.
- Add the concern inventory, evidence grades, and `Reuse / Adopt / Build` contract.
- Add domain-matched candidate routing and the React back-office Pro Components evaluation rule.
- Replace the current baseline record with the required technical capability decision table and approval evidence.

### `references/content-design.md`

- Require content design to identify the workflow capabilities that the technical stage must satisfy.
- Make an approved technical capability artifact a prerequisite for visual production when implementation is in scope.

### `references/visual-v0.md`

- Require the approved technical capability artifact before visual ideation.
- Add the implementation-approach comparison and approval check.
- Prevent visual work from silently substituting custom architecture.
- Define qualifying visual evidence and keep visual-direction approval separate from representative-V0 approval.
- Block implementation planning until the representative V0 is approved.

### `references/project-artifacts.md`

- Add `technical-capability.md` to the artifact map.
- Define it as the technical capability authority without renumbering existing artifacts.
- Mark `progress.md` as workspace-local temporary state, not a formal artifact; point to `assets/progress-template.md`.

### `assets/progress-template.md`

- Define the structured temporary state fields and recovery sections.
- Require tentative decisions to name a formal promotion target.

### `references/workflow-protocol.md`

- Define the parent-owned state machine, Activity/Artifact/Commitment transition rule, invalidation rules, and cleanup gate.
- Define child-executor return semantics and forbid child-driven stage transitions.

### `scripts/validate-progress.mjs`

- Validate progress frontmatter, stage names, statuses, promotion targets, and transition prerequisites when the runtime supports local scripts.
- Keep Markdown instructions as the portable fallback when scripts are unavailable.

## Forward Tests

The edited skill must route these scenarios as follows:

| Scenario | Expected decision behavior |
|---|---|
| Next.js and Tailwind, no component library, complex admin workflow | Detect missing domain component capability; explicitly evaluate and normally recommend Pro Components |
| Existing Ant Design admin | Reuse Ant Design; evaluate incremental Pro Components adoption |
| Mature shadcn tables, forms, and shell | Treat as capability evidence; compare migration/coexistence cost and do not mechanically introduce Ant Design |
| Vue admin | Exclude React Pro Components as platform-incompatible; evaluate Vue-matched mature systems |
| Two simple settings forms | Avoid over-adopting an admin framework; reuse capable primitives or adopt only the narrow capability needed |
| Highly customized canvas/editor | Separate generic admin shell from the specialized editor; reuse/adopt the shell and permit evidence-backed custom core UI |
| Brainstorming produces a written UI specification and recommends `writing-plans`, but no design artifact exists | Return control to the parent visual stage; create reviewable visual evidence and obtain approval before planning |
| Workflow is interrupted with `progress.md` present and formal artifacts partially complete | Reconcile evidence, resume at the owning stage, and delete `progress.md` only after formal acceptance is complete |

Regression checks must also verify that an existing framework or Tailwind alone cannot satisfy the component-system concern, that no visual ideation begins without the approved capability decision, and that a child skill's local completion cannot advance the parent stage.

## Acceptance Criteria

- Every implementation-bound V0 inventories material frontend capabilities by concern.
- Missing or weak concerns route to `technical-baseline.md` even when a framework and styling system exist.
- Every material concern has evidence, a grade, a `Reuse / Adopt / Build` decision, and a selected boundary.
- React complex admin workflows cannot skip Pro Components evaluation.
- Platform-incompatible or disproportionate solutions are not recommended mechanically.
- Existing conventions are preserved only when established and capable.
- Technical selection is approved before visual ideation and implementation.
- Companion skills receive and respect the approved technical capability decision.
- Written design material cannot substitute for a rendered, reviewable visual artifact.
- `superpowers:writing-plans` cannot run before representative V0 approval.
- `progress.md` is removed only after the formal acceptance package is complete.
- All eight forward tests produce the expected routing behavior.
