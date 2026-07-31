# Skills

This repository is a home for personal multi-agent skills: small, reusable workflows that teach an AI agent how to do a specific job in your preferred way.

It is structured like a lightweight open-source skill collection. Each skill lives in its own folder under `skills/` and contains a required `SKILL.md`. Client-specific files are thin adapters around that shared source.

## Repository Layout

```text
.
├── AGENTS.md
├── CLAUDE.md -> AGENTS.md
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
    │   ├── manifest.json
    │   └── agents/openai.yaml
    ├── prompt-polisher/
    │   ├── SKILL.md
    │   ├── manifest.json
    │   └── agents/openai.yaml
    ├── en-zh-context-aligner/
        ├── SKILL.md
        ├── manifest.json
        └── agents/openai.yaml
    └── solution-to-frontend/
        ├── SKILL.md
        ├── manifest.json
        ├── agents/openai.yaml
        └── references/
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

## Multi-Agent Compatibility

`SKILL.md` is the portable source of truth. Keep the workflow there so Codex, Claude Code, Claude AI, Cursor, Hermes, OpenClaw, and other Markdown-reading agents can share the same behavior.

Optional adapter files:

- `agents/openai.yaml`: OpenAI/Codex UI metadata.
- `manifest.json`: cross-agent discovery metadata, including `compat`.
- `AGENTS.md`: repository-level guidance for generic agents.
- `CLAUDE.md`: symlink to `AGENTS.md` for Claude-style agents.

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

For Claude and Cursor, use the same `skills/<skill-name>/SKILL.md` folders:

```bash
mkdir -p ~/.claude/skills ~/.cursor/skills
cp -R skills/* ~/.claude/skills/
cp -R skills/* ~/.cursor/skills/
```

For frameworks such as Hermes, OpenClaw, or cc-switch style launchers, point the launcher at this repository's `skills/` directory or copy the same folders into that framework's skills directory. The skill behavior should stay in `SKILL.md`; only add a new adapter file when the framework requires one.

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
