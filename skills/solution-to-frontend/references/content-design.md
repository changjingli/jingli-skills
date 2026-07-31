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

## Quality Checks

- Every surface supports the confirmed value goal.
- Primary content is distinguishable from supporting detail.
- Repeated content has an explicit reason.
- Metric names, units, precision, calculations, and ranges are coherent.
- Examples and mock values are labeled and not presented as measured outcomes.
- Minimum, typical, maximum, empty, loading, error, and permission states are covered where material.

## Gate

Review business correctness separately from visual quality. Obtain explicit approval for the journey, surface inventory, content matrix, data semantics, and material states before visual production.
