---
name: solution-to-frontend
description: Use when turning pre-sales proposals, solution documents, business diagrams, KPI lists, reference images, or loosely defined customer needs into a frontend product, representative prototype, multi-page implementation, or production delivery.
---

# Solution to Frontend

## Overview

Convert ambiguous solution material into validated frontend delivery from the top down.

**Core principle:** Team size and AI leverage may change; professional responsibilities and approval gates do not disappear.

## Project Isolation

Treat bundled references as process guidance only. Never import their examples as project facts.

Discover every project fact from the current workspace or confirmed user input. Write project artifacts into the workspace, never into the installed skill directory.

Respect existing project conventions. When none exist, use `docs/solution-to-frontend/`; see [references/project-artifacts.md](references/project-artifacts.md).

## Start

1. Inspect solution material, product/design documents, code, tests, deployment files, and recent history.
2. Determine the latest completed stage using concrete artifacts and approvals, not file names alone.
3. State the current stage, missing inputs, and next gate.
4. Before creating or updating a project artifact, load [references/project-artifacts.md](references/project-artifacts.md).
5. Load only the reference for the active stage.

| Stage | Load | Required result |
|---|---|---|
| Intake and outcome | [references/intake-outcome.md](references/intake-outcome.md) | Confirmed value goal, audience, scope, facts, assumptions |
| Product content | [references/content-design.md](references/content-design.md) | Screen/flow content, data semantics, states, acceptance criteria |
| Visual baseline and V0 | [references/visual-v0.md](references/visual-v0.md) | Approved visual direction and representative runnable slice |
| Scale and delivery | [references/scale-delivery.md](references/scale-delivery.md) | Reusable system, complete implementation, production evidence |

For the full journey, proceed stage by stage and stop at each approval gate. For one stage, verify upstream inputs and stay within scope.

## Non-Negotiable Gates

```text
No confirmed value goal  -> no screen inventory
No approved content      -> no visual production
No approved V0           -> no multi-screen replication
No target-runtime proof  -> no delivery-complete claim
```

Only the user or named accountable stakeholder may approve value, content, visual direction, V0, or release. AI may gather evidence and recommend; it must not approve itself.

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
- implementation, integration, performance, or runtime defect -> engineering/delivery.

## Composition

Compose available specialist skills instead of duplicating them:

- use KPI/data-analysis skills for metric definitions and validation;
- use Impeccable or equivalent design skills for visual shaping, critique, extraction, and polish;
- use Superpowers or equivalent engineering skills for plans, TDD, debugging, and verification;
- use platform QA and deployment skills for target-runtime evidence.

These tools assist a stage; they never waive its inputs or approval gate.

## Completion

Report outcomes as an evidence chain:

`source -> decision -> rationale -> artifact -> approval/evidence -> next stage`

Separate confirmed facts, assumptions, examples, and unresolved decisions. Never present a prototype, mock-backed demo, or passing test suite as proof of customer value or production readiness.
