---
name: prompt-polisher
description: Use when the user wants to turn a rough request, agent instruction, system prompt, or repeatable workflow note into a clearer prompt while preserving their intent and voice.
---

# Prompt Polisher

## Workflow

1. Identify the user's real objective, expected output, constraints, and any missing context.
2. Preserve the user's intent and voice; improve structure and specificity.
3. Remove ambiguity that would cause an agent to make brittle assumptions.
4. Prefer concrete acceptance criteria over broad adjectives.
5. Return a ready-to-use prompt, plus a short note only when a tradeoff or assumption matters.

## Output Pattern

Use this structure unless the user asks for a different format:

```text
Prompt:
[rewritten prompt]

Notes:
[1-3 short bullets, only if useful]
```

## Good Prompt Ingredients

- Role or context the agent should assume
- Task objective
- Inputs and where to find them
- Constraints and non-goals
- Desired output format
- Validation steps or acceptance criteria
