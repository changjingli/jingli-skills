# Product Content Design

Use this stage to decide what each screen or step must communicate or enable before choosing its visual style.

## Work Top Down

1. Map the end-to-end user or audience journey.
2. Give every screen or step one primary business question or job.
3. Define primary content, supporting content, detail, and actions.
4. Define data semantics, realistic ranges, states, and permissions.
5. Choose a presentation form only when it clarifies the business meaning.

## Content Matrix

Use a matrix adapted to the product type:

| Surface/step | User job or business question | Primary content/action | Supporting content | Detail | States | Acceptance |
|---|---|---|---|---|---|---|

For analytical surfaces, additionally specify:

| Metric/visual | Definition | Unit | Precision | Time grain | Dimensions | Calculation/source | Presentation form |
|---|---|---|---|---|---|---|---|

“Chart,” “trend,” and “distribution” are incomplete. Specify chart type, fields, comparison, time range, ranking limits, filters, tooltip/detail behavior, and empty/error states.

For transactional products, specify triggers, inputs, validation, permissions, confirmation, success, failure, retry, cancellation, and recovery.

## Mock Data Contract

For a static high-fidelity V0, mock data is part of the deliverable, not disposable decoration.

Define:

- entity names, fields, units, enum values, and relationships;
- minimum, typical, maximum, empty, error, and permission-limited examples where material;
- realistic ranges, precision, time windows, ranking limits, and formatting rules;
- which values are confirmed facts, plausible examples, or intentionally fictional;
- the future integration boundary: which mock modules, fixtures, or adapters should later be replaced by API responses.

Do not hard-code important business semantics only inside visual components. Keep data shapes explicit enough that engineering can connect real services without rediscovering the product meaning from screenshots.

## Integration Readiness

When the approved V0 is expected to become production frontend code later, define the integration boundary before visual production:

| Surface/data area | Entity or API concept | Fields and types | States | Mock source | Future replacement point |
|---|---|---|---|---|---|

For each important data area, record:

- whether the future data is read-only, user-submitted, calculated, imported, or event-driven;
- pagination, sorting, filtering, search, refresh, and drill-down behavior where material;
- loading, empty, error, permission-limited, stale, and partial-data states;
- client-side assumptions that must be confirmed before real API integration;
- which file, fixture, adapter, or component boundary should be replaced when connecting services.

Do not require real APIs for the static V0 unless explicitly in scope. The goal is to make future integration obvious, not to pretend integration is already complete.

## Quality Checks

- Every surface supports the confirmed value goal.
- Primary content is distinguishable from supporting detail.
- Repeated content has an explicit reason.
- Metric names, units, precision, calculations, and ranges are coherent.
- Examples and mock values are labeled and not presented as measured outcomes.
- Mock data has a realistic, typed, replaceable shape when implementation is in scope.
- Important data areas have an explicit future integration boundary.
- Minimum, typical, maximum, empty, loading, error, and permission states are covered where material.

## Gate

Review business correctness separately from visual quality. Obtain explicit approval for the journey, surface inventory, content matrix, data semantics, and material states before visual production.
