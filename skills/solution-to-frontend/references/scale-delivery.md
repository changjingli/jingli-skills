# Scale Static V0 and Handoff

Use this stage only after the representative V0 is approved.

## Extract What Is Stable

Separate reusable capability from business-specific composition:

| Reuse when intent is stable | Keep local when meaning differs |
|---|---|
| design tokens and accessibility rules | page-specific narrative and reading order |
| proven component states and interaction primitives | domain-specific metrics, workflows, and visualizations |
| typed mock data schemas and calculation rules shared by the domain | context-specific labels, thresholds, and exceptions |
| test helpers and acceptance checks | one-off layouts or demonstrations |

Prefer a little duplication over an abstraction whose intent is not yet stable. Extract after repeated use or strong domain evidence, not because two elements look similar.

## Plan and Implement the Static V0

Create a scoped implementation plan that maps each remaining surface to approved content, shared capabilities, unique behavior, mock/data semantics, tests, and acceptance evidence. Preserve the repository's architecture and platform conventions.

Use engineering discipline appropriate to risk: stable component boundaries, typed data, predictable state handling, focused review, and static builds or previews. Keep real integrations, mock/demo paths, and future work visibly distinct.

## Definition of Done

A static high-fidelity V0 is customer-reviewable only when:

- the approved scope is implemented or explicitly marked out of scope;
- the core review paths are clickable and run without required live services;
- key default, loading, empty, error, and permission-limited states are represented where material;
- mock data is realistic, labeled, typed where the stack supports it, and replaceable through clear fixture or adapter boundaries;
- layout, hierarchy, responsiveness, overflow, text fitting, media/canvas rendering, and interaction feedback have been checked in the review runtime;
- console/runtime errors, failed required assets, and broken internal navigation are resolved or documented as review limitations;
- the prototype boundary is explicit: what is simulated, what is reusable, and what requires productionization.

Do not waive these checks because the V0 looks visually polished. Good taste is not the same thing as reusable frontend.

## Review Evidence

Verify as applicable:

- business rules, data semantics, permissions, and failure recovery;
- component, interaction, end-to-end, and visual behavior;
- accessibility, localization, compatibility, performance, and security;
- target devices, review runtimes, static export or preview hosting, configuration, and known integration boundaries;
- screenshots, recordings, reports, logs, or monitored outcomes that another person can review.

## Productionization Handoff

Before calling the V0 complete, record:

- what code, components, tokens, layouts, data types, and interaction patterns are intended for reuse;
- which mock data modules or adapters should be replaced by API integration;
- which permissions, authentication, observability, security, deployment, and operational concerns are intentionally out of scope for the static V0;
- which customer-approved decisions are binding inputs for production engineering.

## Customer Review Package

Package the V0 so an accountable stakeholder can review the intended decision, not merely admire screens.

Include:

- review URL, static build path, or local preview command;
- review scope, primary paths, target devices, and known limitations;
- links to the approved value goal, content matrix, visual authority, and representative V0 decision;
- mock/demo data disclosure and any fictional, masked, or estimated values;
- evidence summary: screenshots, recordings, automated checks, runtime notes, or browser/device coverage;
- open decisions requiring customer response;
- productionization notes, including integration boundaries and reusable code areas.

Ask for approval of the bounded V0 decision: approve for next-step production planning, reject, or request named changes. Do not treat a positive comment about visual quality as approval of business content, data semantics, or reuse readiness.

## Gate

Do not claim production delivery because code runs, tests pass, or a static build exists. State the demonstrated endpoint precisely: concept, static high-fidelity V0, customer-reviewable prototype, PoC, pilot, production release, or measured customer outcome.

After review, route feedback to the owning layer: value/scope, content/data, design/interaction, shared system, engineering, or productionization.
