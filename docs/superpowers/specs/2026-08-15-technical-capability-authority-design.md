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
  -> Visual authority
  -> Representative V0
  -> Scale and delivery
```

No visual ideation or V0 implementation may begin until the material technical capabilities have an approved `Reuse`, `Adopt`, or `Build` decision.

## Authority Model

The workflow distinguishes four authorities:

| Authority | Question answered | Primary artifact |
|---|---|---|
| Product/outcome | Why, for whom, and what success means | Existing intake and outcome artifacts |
| Content | What each surface communicates or enables | `02-content-design.md` |
| Technical capability | Which proven capabilities will carry the workflow | `technical-capability.md` |
| Visual | How the approved content and capabilities should be understood and operated | `03-visual-brief.md` and project design authority |

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
```

The content stage defines workflow capabilities and material states. The technical capability stage then evaluates implementation approaches. The visual stage consumes the approved decision and may refine visual integration, but it may not silently reopen or replace the selected component architecture.

Before the representative V0 is drawn, compare the applicable approaches:

1. Extend the incumbent component system.
2. Adopt a domain-matched mature system.
3. Build project-specific components.

Only applicable approaches must be evaluated; a platform-incompatible candidate is excluded with evidence. The comparison records compatibility, reuse, accessibility, rendering/SSR, bundle, theming, migration, and production-reuse trade-offs. The accountable stakeholder approves the selected approach before visual production.

## Companion Skill Contract

`superpowers:brainstorming`, Impeccable visual work, `superpowers:writing-plans`, and V0 implementation consume the approved `technical-capability.md` as an input.

They may explore interaction, composition, and visual direction within its boundaries. They may not replace an approved `Reuse` or `Adopt` decision with custom components without returning to the technical capability gate, recording new evidence, and obtaining approval.

If a companion skill starts before the capability decision exists, the solution workflow pauses it at the technical capability gate rather than allowing unconstrained UI generation.

## File Changes

### `SKILL.md`

- Replace the single “no frontend stack” condition with an always-run concern inventory.
- Load `technical-baseline.md` whenever any material concern is absent, weak, or not evidenced.
- Add the technical capability authority to the stage sequence and non-negotiable gates.
- Clarify that incumbent conventions are preserved only when established and capable for the confirmed workflow.
- Require companion skills to consume the approved technical capability artifact.

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

### `references/project-artifacts.md`

- Add `technical-capability.md` to the artifact map.
- Define it as the technical capability authority without renumbering existing artifacts.

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

Regression checks must also verify that an existing framework or Tailwind alone cannot satisfy the component-system concern, and that no visual ideation begins without the approved capability decision.

## Acceptance Criteria

- Every implementation-bound V0 inventories material frontend capabilities by concern.
- Missing or weak concerns route to `technical-baseline.md` even when a framework and styling system exist.
- Every material concern has evidence, a grade, a `Reuse / Adopt / Build` decision, and a selected boundary.
- React complex admin workflows cannot skip Pro Components evaluation.
- Platform-incompatible or disproportionate solutions are not recommended mechanically.
- Existing conventions are preserved only when established and capable.
- Technical selection is approved before visual ideation and implementation.
- Companion skills receive and respect the approved technical capability decision.
- All six forward tests produce the expected routing behavior.

