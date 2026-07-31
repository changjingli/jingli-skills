# Visual Baseline and Representative V0

Use this stage after product content is approved. Decide how the confirmed content should be understood and operated, then validate the direction on one high-risk slice.

## Establish Visual Authority

Inspect existing brand/design systems, incumbent UI, references explicitly selected by the user, target devices, viewing distance, input methods, accessibility needs, and content ranges.

Translate subjective direction into executable decisions:

- information hierarchy and reading order;
- layout topology and responsive behavior;
- typography, color, spacing, density, and motion;
- component states and interaction feedback;
- imagery, charts, maps, tables, forms, and detail patterns;
- explicit anti-references and prohibited patterns.

Persist durable rules in the project design authority, normally `DESIGN.md` or the existing equivalent.

## Select the V0

Choose the smallest representative slice that covers the greatest combined risk, not the easiest screen.

Examples:

- dashboard: a screen containing core KPIs, primary visualization, detail, filters, and risky interaction;
- mini program: one complete core journey from entry through success and recovery;
- admin system: list/filter/detail/edit/permission/submit loop;
- H5: entry, core interaction, conversion, sharing or recovery.

Label examples as illustrative; never make their layouts defaults.

## Validate

Run the V0 in the actual target runtime and relevant original dimensions. Check content correctness, hierarchy, overflow, overlap, responsiveness, interactions, states, accessibility, console/runtime errors, failed requests, and nonblank rendered media or canvases.

Automated checks and screenshots provide evidence; they do not approve taste or business suitability.

## Gate

Present the runnable V0 and evidence. Record explicit approval or classify failures back to content, visual design, or engineering. Do not extract or replicate an unapproved V0.
