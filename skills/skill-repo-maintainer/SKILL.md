---
name: skill-repo-maintainer
description: Use when maintaining a repository of Codex skills, including adding new skills, reviewing SKILL.md structure, validating metadata, preparing releases, or keeping README and plugin metadata aligned.
---

# Skill Repo Maintainer

## Workflow

1. Inspect the repository structure before editing.
2. Keep each skill self-contained under `skills/<skill-name>/`.
3. Make `SKILL.md` concise and specific; move long examples, references, scripts, and assets into subfolders only when they will actually be used.
4. Ensure frontmatter includes `name` and `description`, and that `name` matches the folder.
5. Update repository-level docs or plugin metadata when adding, removing, or renaming skills.
6. Run the repository validator before finishing.

## Review Checklist

- Skill names are lower hyphen-case.
- Descriptions explain when the skill should trigger.
- Skill bodies describe the operational workflow rather than marketing the skill.
- No private tokens, credentials, or personal data are committed.
- Examples are realistic and reusable.
- Scripts are deterministic, executable, and documented only where necessary.

## Release Prep

Before publishing a change:

1. Run `npm run validate`.
2. Confirm README examples still match the repository structure.
3. Update `.codex-plugin/plugin.json` if repository URL, author, or high-level skill set changed.
4. Commit with a message that names the skill or workflow changed.
