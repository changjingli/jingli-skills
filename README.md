# Skills

This repository is a home for personal Codex skills: small, reusable workflows that teach an AI agent how to do a specific job in your preferred way.

It is structured like a lightweight open-source skill collection. Each skill lives in its own folder under `skills/` and contains a required `SKILL.md`.

## Repository Layout

```text
.
├── .codex-plugin/
│   └── plugin.json
├── .github/
│   └── workflows/
│       └── validate.yml
├── scripts/
│   └── validate-skills.mjs
└── skills/
    ├── skill-repo-maintainer/
    │   ├── SKILL.md
    │   └── agents/openai.yaml
    └── prompt-polisher/
        ├── SKILL.md
        └── agents/openai.yaml
```

## Add A Skill

Create a new folder:

```bash
mkdir -p skills/my-skill
```

Add `skills/my-skill/SKILL.md`:

```markdown
---
name: my-skill
description: Use when the user wants ...
---

# My Skill

## Workflow

1. Gather the minimum context needed.
2. Follow the user's existing conventions.
3. Validate the output before responding.
```

Good skill descriptions are specific about when the skill should trigger. The body should stay concise and move long references, scripts, or assets into subfolders only when they are genuinely useful.

## Validate

Run:

```bash
npm run validate
```

The validator checks that each skill has valid YAML frontmatter, required `name` and `description` fields, and a hyphen-case folder/name match.

## Install Locally

For local Codex use, copy or symlink the skills into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/* ~/.codex/skills/
```

If you prefer symlinks while editing:

```bash
ln -s "$PWD/skills/my-skill" ~/.codex/skills/my-skill
```

## Publish To GitHub

From this folder:

```bash
git init
git add .
git commit -m "Initial personal skills"
gh repo create skills --public --source=. --remote=origin --push
```

After publishing, update `.codex-plugin/plugin.json` with your GitHub URL and author name if needed.

## License

MIT
