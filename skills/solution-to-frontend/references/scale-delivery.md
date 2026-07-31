# Scale and Delivery

Use this stage only after the representative V0 is approved.

## Extract What Is Stable

Separate reusable capability from business-specific composition:

| Reuse when intent is stable | Keep local when meaning differs |
|---|---|
| design tokens and accessibility rules | page-specific narrative and reading order |
| proven component states and interaction primitives | domain-specific metrics, workflows, and visualizations |
| data schemas and calculation rules shared by the domain | context-specific labels, thresholds, and exceptions |
| test helpers and acceptance checks | one-off layouts or demonstrations |

Prefer a little duplication over an abstraction whose intent is not yet stable. Extract after repeated use or strong domain evidence, not because two elements look similar.

## Plan and Implement

Create a scoped implementation plan that maps each remaining surface to approved content, shared capabilities, unique behavior, tests, and acceptance evidence. Preserve the repository's architecture and platform conventions.

Use engineering discipline appropriate to risk: tests before behavior changes, systematic debugging, focused review, and production builds. Keep real integrations, mock/demo paths, and future work visibly distinct.

## Production Evidence

Verify as applicable:

- business rules, data semantics, permissions, and failure recovery;
- component, integration, end-to-end, and visual behavior;
- accessibility, localization, compatibility, performance, and security;
- target devices/runtimes, real integrations, configuration, observability, deployment, and rollback;
- screenshots, recordings, reports, logs, or monitored outcomes that another person can review.

## Gate

Do not claim delivery complete because code runs, tests pass, or a static build exists. State the demonstrated endpoint precisely: concept, runnable prototype, PoC, pilot, production release, or measured customer outcome.

After release, route feedback to the owning layer: value/scope, content/data, design/interaction, shared system, engineering, or operations.
