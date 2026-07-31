# Design Authority Bootstrap

Use this reference only when the visual stage has begun and no approved project design authority exists.

This workflow is an adaptation of the visual-authority and new-work routing concepts in [pbakaus/impeccable](https://github.com/pbakaus/impeccable), licensed under Apache-2.0. It is deliberately narrowed for this skill: it does not require installing Impeccable, invoking its scripts, or adopting its broader design workflow.

## Discover Before Creating

Inspect the strongest available visual evidence: approved brand assets, design systems, shipped product surfaces, tokens, themes, shared components, CSS, design files, and user-selected references. Treat visual authority as evidence, not as a filename.

When sources conflict, apply this precedence:

```text
approved brand or design specification
  > explicit user instruction for the current work
  > shipped product surface
  > shared tokens, themes, components, or CSS
  > a single-page reference image or isolated example
```

More recent evidence wins only within the same precedence level. If two sources at the same level conflict materially, record the conflict as an open decision and request a ruling; do not merge them into an invented middle ground.

Classify the project before writing `DESIGN.md`:

| Condition | Route | Allowed action |
|---|---|---|
| An incumbent visual world has credible evidence | Preserve and document | Extract durable rules; do not redesign by default |
| No credible visual world exists | Establish | Create a new draft authority from approved content and explicit references |
| The user explicitly requests a new visual world | Replace | Record the decision and anti-references before designing |

A missing `DESIGN.md` alone is not evidence for the second route. If the evidence is mixed or insufficient, state the ambiguity and request the decision that changes the route.

## Create the Authority

Write `DESIGN.md` in the workspace root unless the repository has an established equivalent. Set its status to `draft` until the visual gate is approved.

The document must capture:

1. sources of visual truth and their precedence;
2. target surfaces, devices, input methods, and accessibility constraints;
3. intended audience, operating mode, and information-density rationale;
4. information hierarchy, reading order, layout topology, breakpoints, and content constraints;
5. typography, color, spacing, density, imagery, data-display, motion, and interaction-state rules;
6. reusable component or token candidates, plus what must stay surface-specific;
7. anti-references, prohibited patterns, and known deviations from the incumbent;
8. assumptions, unresolved choices, and the evidence required to validate them.

For an incumbent product, record observed rules separately from proposed changes. For a replacement, preserve factual content and functional constraints while treating the old visual language as an anti-reference only after explicit approval.

## Confirm the Baseline

Present a bounded visual-baseline confirmation with the draft authority:

```text
Decision requested: approve the visual authority for <surfaces>.
Visual evidence reviewed: <paths, screenshots, references, or runtime URLs>.
Rules being approved: <short list of hierarchy, layout, visual, and interaction decisions>.
Open assumptions and known deviations: <list or none>.
V0 enabled by approval: <representative slice and target runtime>.
```

The accountable stakeholder may approve the baseline, request named changes, or approve the baseline while reserving V0 approval. Record the result using the project Gate Record. Do not start visual production, treat draft rules as durable, or replicate them across surfaces without the required approval.
