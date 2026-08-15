---
name: solution-to-frontend
description: Use when turning pre-sales proposals, solution documents, business diagrams, KPI lists, reference images, or loosely defined customer needs into a customer-reviewable static high-fidelity frontend V0 that can later be reused by engineering.
---

# Solution to Frontend

## Overview

Convert ambiguous solution material into a validated, customer-reviewable static high-fidelity frontend V0 from the top down.

**Core principle:** A V0 is not production delivery, but it must be engineered so customer-approved structure, components, content, and interaction expectations can survive into production development.

## Project Isolation

Treat bundled references as process guidance only. Never import their examples as project facts.

Discover every project fact from the current workspace or confirmed user input. Write project artifacts into the workspace, never into the installed skill directory.

Respect existing project conventions. When none exist, use `docs/solution-to-frontend/`; see [references/project-artifacts.md](references/project-artifacts.md).

## Companion Skill Orchestration

This workflow actively composes the following companion skill collections when they are installed. Do not rely on passive skill discovery or a generic "available and useful" decision:

- [Superpowers](https://github.com/obra/superpowers)
- [Impeccable](https://github.com/pbakaus/impeccable/)

Invoke the named skill at its stage trigger and record its output in the active project artifact: normally `03-visual-brief.md` for design-direction evidence, `04-v0.md` for implementation and review evidence, and `06-acceptance.md` for final readiness evidence. If a named skill is not installed, state that fact, use the listed fallback, and mark the resulting evidence as degraded; its absence never grants approval or bypasses a gate.

| Trigger | Direct invocation | Required output | Fallback when unavailable |
|---|---|---|---|
| First visual work in a project without Impeccable product context | `impeccable:init` | Captured product context | Complete intake outcome and record the missing Impeccable context |
| Before implementing the representative V0 slice | `superpowers:writing-plans` | Bounded implementation plan tied to approved content and visual direction | Record the same plan in the active project artifact |
| Before each new or changed behavior or interaction | `superpowers:test-driven-development` | Failing test, minimal implementation, passing verification | Use the project test convention; state that TDD specialist guidance was unavailable |
| Runnable V0 ready for visual review | `impeccable:critique`, then `impeccable:audit` | Design findings, detector/browser evidence, remediation decision, and re-review evidence after material fixes | Use `references/visual-v0.md` plus platform QA evidence; mark visual review degraded |
| A test, review, or runtime check fails | `superpowers:systematic-debugging` | Root cause, corrective change, and regression evidence | Classify and return to the owning stage under Approval Protocol |
| Before claiming customer-review readiness | `impeccable:polish`, then `superpowers:verification-before-completion` | Final visual findings, fresh verification evidence, and explicit disposition for every material finding | Complete the review package and disclose the unavailable checks |

`impeccable:init` runs once only when its product context is absent. All other invocations run at their stated trigger; they are not deferred because another general-purpose skill happened to load. A material finding must be fixed and re-checked, or explicitly accepted by the accountable stakeholder with its limitation recorded; unresolved findings block a customer-review-ready claim.

## Start

1. Inspect solution material, product/design documents, code, tests, deployment files, and recent history.
2. Determine the latest completed stage using concrete artifacts and approvals, not file names alone.
3. State the current stage, missing inputs, and next gate.
4. Before creating or updating a project artifact, load [references/project-artifacts.md](references/project-artifacts.md).
5. Load only the reference for the active stage.

When no established frontend stack is evidenced, load [references/technical-baseline.md](references/technical-baseline.md) during intake and before the first implementation change. Record the selected baseline and any justified deviation in the active project artifact.

| Stage | Load | Required result |
|---|---|---|
| Intake and outcome | [references/intake-outcome.md](references/intake-outcome.md) | Confirmed value goal, audience, scope, facts, assumptions |
| Product content | [references/content-design.md](references/content-design.md) | Screen/flow content, data semantics, states, acceptance criteria |
| Visual baseline and V0 | [references/visual-v0.md](references/visual-v0.md) and the triggered companion skills above | Approved visual direction, reviewed runnable slice, and companion-skill evidence |
| Scale and delivery | [references/scale-delivery.md](references/scale-delivery.md) and the triggered companion skills above | Reusable static prototype, final verification evidence, productionization handoff |

For the full journey, proceed stage by stage and stop at each approval gate. For one stage, verify upstream inputs and stay within scope.

## Non-Negotiable Gates

```text
No confirmed value goal  -> no screen inventory
No approved content      -> no visual production
No approved V0           -> no multi-screen replication
No review-runtime proof  -> no customer-reviewable V0 claim
```

Only the user or named accountable stakeholder may approve value, content, visual direction, V0, or customer-review readiness. AI may gather evidence and recommend; it must not approve itself.

## Approval Protocol

At every gate, present a bounded approval request instead of asking for generic confirmation:

1. Name the artifact and decision being approved.
2. List its confirmed facts, material assumptions, unresolved decisions, and links to evidence.
3. State the exact next work enabled by approval and what remains out of scope.
4. Ask the accountable stakeholder to approve, reject, or request a named change.
5. Record the approver, date, decision, reviewed artifact, and any conditions in the project artifact.

Approval may be a direct user instruction in the current conversation when its scope is unambiguous. Silence, a new unrelated request, a runnable demo, or a vague acknowledgement is not approval. If approval is absent, complete only evidence gathering and the active stage's draft; do not advance the gate.

When a review fails, classify the failure and return to its owning stage:

- wrong goal or scope -> intake and outcome;
- wrong content, metric, state, or workflow -> product content;
- wrong hierarchy, interaction, or visual language -> visual baseline;
- implementation, review-runtime, performance, or reuse defect -> engineering/delivery.

## Composition

Compose the required companion skills according to the orchestration table instead of duplicating their methods. Then compose other specialist skills as needed:

- use KPI/data-analysis skills for metric definitions and validation;
- use the bundled [design-authority bootstrap](references/design-authority-bootstrap.md) when no approved design authority exists;
- use platform QA and deployment skills for review-runtime evidence when a hosted or shared preview is needed.

These tools assist a stage; they never waive its inputs or approval gate.

## Completion

Report outcomes as an evidence chain:

`source -> decision -> rationale -> artifact -> approval/evidence -> next stage`

Separate confirmed facts, assumptions, examples, mock/demo behavior, and unresolved decisions. Never present a static V0, mock-backed demo, or passing test suite as production readiness. Instead, state what can be reused directly, what needs API/data integration, and what remains a productionization task.

For a customer-facing V0, include the review package: preview path or URL, review scope, mock/demo disclosure, evidence summary, open decisions, reusable code areas, integration boundaries, and productionization notes.
