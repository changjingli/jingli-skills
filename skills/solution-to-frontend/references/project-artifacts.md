# Project Artifacts

Use existing project conventions first. When the workspace has no established location, write stage artifacts under `docs/solution-to-frontend/`.

```text
docs/solution-to-frontend/
├── 00-intake.md
├── 01-outcome.md
├── 02-content-design.md
├── 03-visual-brief.md
├── 04-v0.md
├── 05-scale-plan.md
└── 06-acceptance.md
```

Do not create every file preemptively. Create or update the artifact owned by the active stage.

## Required Header

Each artifact begins with:

```markdown
# <Artifact title>

Status: draft | awaiting approval | approved | superseded
Owner: <accountable role or person>
Sources: <workspace paths, conversations, systems, or evidence>
Last decision: <date and concise decision>
```

## Decision Record

Record material decisions in this shape:

| Decision | Evidence/rationale | Alternatives rejected | Owner | Status |
|---|---|---|---|---|

## Gate Record

When requesting or receiving a gate decision, add a compact record:

```markdown
## Gate: <stage>

Decision requested: <artifact and bounded decision>
Evidence reviewed: <paths, URLs, runtime evidence, or conversation reference>
Open assumptions and conditions: <list or none>
Approved by: <person or role, or pending>
Approved on: <YYYY-MM-DD, or pending>
Next work enabled: <specific next stage or task>
```

Use `pending` until an accountable stakeholder explicitly approves. Do not replace it with an inferred approval.

## Evidence Rules

- Link workspace sources by path when possible.
- Mark assumptions and examples explicitly.
- Record who approved a gate and what artifact/evidence they reviewed.
- Do not turn silence, generated output, or AI recommendations into approval.
- Do not copy project facts into the installed Skill directory.
