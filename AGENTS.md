# Agent Skills Repository

This repository stores reusable skills for multiple AI coding agents.

## Skill Contract

- Treat `skills/<skill-name>/SKILL.md` as the source of truth.
- Use the YAML frontmatter `name` and `description` to decide whether a skill applies.
- Load the skill body only after it applies.
- Preserve any optional resources under the skill folder, such as `references/`, `scripts/`, `assets/`, `agents/`, or client-specific manifests.

## Client Adapters

- `agents/openai.yaml` is OpenAI/Codex UI metadata.
- `manifest.json`, when present, is cross-agent metadata for discovery and compatibility.
- Do not duplicate the skill workflow into client-specific files unless that client requires it.

## Current Compatibility Target

Skills in this repository are written to be usable by Codex, Claude Code, Claude AI, Cursor, Hermes, OpenClaw, and other agents that can read Markdown skill folders.
