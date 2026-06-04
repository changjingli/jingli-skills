#!/usr/bin/env python3
"""Pre-flight checks for Context-Aligner drafts and skill files."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


BANNED_PATTERNS = [
    (re.compile(r"带有\s*0\s*行"), "Avoid literal `带有 0 行`; use `没写过一行` or `没有一行...`."),
    (re.compile(r"具有[^。；，,]*性能"), "Avoid `具有...性能`; restructure into natural Chinese."),
    (re.compile(r"的其中之一"), "Avoid `...的其中之一`; use `之一` or rewrite directly."),
    (re.compile(r"对于[^。；，,]*而言"), "Avoid stiff `对于...而言` unless contrast requires it."),
    (re.compile(r"建立这个"), "Avoid vague `建立这个`; decode `build this` by scene."),
    (re.compile(r"野心勃勃的[^。；，,]*(团队|工程师|创始人)"), "Avoid pejorative `野心勃勃`; use `有野心/敢破局`."),
]

REQUIRED_OUTPUT_SECTIONS = ["一、源码重构", "二、意象对齐", "三、终极通透版"]


def read_input(args: argparse.Namespace) -> str:
    if args.file:
        return Path(args.file).read_text(encoding="utf-8")
    return sys.stdin.read()


def check_text(text: str, require_sections: bool) -> list[str]:
    issues: list[str] = []
    for pattern, message in BANNED_PATTERNS:
        if pattern.search(text):
            issues.append(message)

    if require_sections:
        for section in REQUIRED_OUTPUT_SECTIONS:
            if section not in text:
                issues.append(f"Missing required output section: {section}")

    return issues


def check_skill_root(root: Path) -> list[str]:
    issues: list[str] = []
    required = [
        root / "SKILL.md",
        root / "references" / "domain-tone-guide.md",
        root / "references" / "terminology-guide.md",
        root / "references" / "bad-good-examples.md",
        root / "references" / "evaluation-rubric.md",
    ]
    for path in required:
        if not path.exists():
            issues.append(f"Missing required skill asset: {path}")

    skill_md = root / "SKILL.md"
    if skill_md.exists():
        text = skill_md.read_text(encoding="utf-8")
        for phrase in ["Trigger Rules", "Lifecycle & Loop Rules", "Required References"]:
            if phrase not in text:
                issues.append(f"SKILL.md missing section: {phrase}")

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Context-Aligner drafts for obvious translationese and missing structure.")
    parser.add_argument("file", nargs="?", help="Draft file to check. Reads stdin when omitted.")
    parser.add_argument("--require-sections", action="store_true", help="Require the standard three output sections.")
    parser.add_argument("--skill-root", help="Validate required skill assets under this root.")
    args = parser.parse_args()

    issues: list[str] = []
    if args.skill_root:
        issues.extend(check_skill_root(Path(args.skill_root)))
    else:
        issues.extend(check_text(read_input(args), args.require_sections))

    if issues:
        for issue in issues:
            print(f"FAIL: {issue}", file=sys.stderr)
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
