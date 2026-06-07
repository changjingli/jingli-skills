#!/usr/bin/env python3
"""Pre-flight checks for Context-Aligner drafts and skill files."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


BANNED_PATTERNS = [
    (re.compile(r"(带有\s*)?(0|零)\s*行(?:手动编写|人工编写|手写)?(?:的)?代码"), "Avoid literal zero-line phrasing; use `没写过一行` or `没有一行...`."),
    (re.compile(r"具有[^。；，,]*性能"), "Avoid `具有...性能`; restructure into natural Chinese."),
    (re.compile(r"是[^。；，,]*的其中之一"), "Avoid `是...的其中之一`; use `之一` or rewrite directly."),
    (re.compile(r"被认为"), "Avoid passive translationese `被认为`; name the viewpoint or state the judgment directly."),
    (re.compile(r"被期望"), "Avoid passive translationese `被期望`; state who expects what or rewrite directly."),
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
        for phrase in [
            "Domain Gateway",
            "通道 A：闪电响应",
            "通道 B：重型重构",
            "通道 C：异常拦截",
            "认知熵减协议",
            "Lifecycle & Loop Rules",
            "沉淀资产建议",
            "Required References",
        ]:
            if phrase not in text:
                issues.append(f"SKILL.md missing section: {phrase}")

    reference_requirements = {
        root / "references" / "domain-tone-guide.md": [
            "触发边界与智能路由",
            "Freedom Decision Matrix",
            "通道 A：闪电响应",
            "通道 B：重型重构",
            "通道 C：异常拦截",
        ],
        root / "references" / "bad-good-examples.md": [
            "否定转化规约",
            "意象重构规约",
            "结构重排规约",
            "认知审计",
        ],
    }
    for path, phrases in reference_requirements.items():
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                issues.append(f"{path.name} missing required phrase: {phrase}")

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
