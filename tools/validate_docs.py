#!/usr/bin/env python3
"""Validate markdown docs for the execution system."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
PLACEHOLDER_RE = re.compile(r"\{\{[^{}]+\}\}")

BANNED_TERMS = [
    "gdd",
    "tournament",
    "multiplayer",
    "monetization",
    "fantasia del jugador",
    "core loops",
    "loop jugable",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate markdown docs")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path("."),
        help="Root folder to validate",
    )
    parser.add_argument(
        "--profile",
        choices=["templates", "project"],
        default="templates",
        help=(
            "templates: allow placeholders and unresolved docs/* links. "
            "project: fail placeholders and unresolved local links"
        ),
    )
    return parser.parse_args()


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if p.is_file())


def normalize_link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    return target


def is_external_link(target: str) -> bool:
    lowered = target.lower()
    return lowered.startswith(("http://", "https://", "mailto:"))


def resolve_local_target(file_path: Path, target: str) -> Path:
    if target.startswith("/"):
        return file_path.anchor and Path(target) or Path(target)
    return (file_path.parent / target).resolve()


def should_skip_target_check(target: str, profile: str) -> bool:
    if target.startswith("#"):
        return True
    if is_external_link(target):
        return True
    if profile == "templates" and target.startswith("docs/"):
        return True
    return False


def validate_file(file_path: Path, profile: str) -> list[str]:
    errors: list[str] = []
    content = file_path.read_text(encoding="utf-8")
    lowered = content.lower()

    for term in BANNED_TERMS:
        if term in lowered:
            errors.append(f"{file_path}: banned term detected -> '{term}'")

    if profile == "project":
        placeholders = PLACEHOLDER_RE.findall(content)
        if placeholders:
            errors.append(
                f"{file_path}: unresolved placeholders -> {sorted(set(placeholders))}"
            )

    for match in MARKDOWN_LINK_RE.finditer(content):
        raw_target = match.group(1)
        target = normalize_link_target(raw_target)
        target_no_anchor = target.split("#", 1)[0]

        if not target_no_anchor:
            continue
        if should_skip_target_check(target_no_anchor, profile):
            continue

        resolved = resolve_local_target(file_path, target_no_anchor)
        if not resolved.exists():
            errors.append(f"{file_path}: broken local link -> '{target_no_anchor}'")

    return errors


def main() -> int:
    args = parse_args()
    root = args.root.resolve()

    if not root.exists():
        print(f"ERROR: root path does not exist: {root}")
        return 2

    md_files = iter_markdown_files(root)
    if not md_files:
        print(f"No markdown files found under: {root}")
        return 0

    all_errors: list[str] = []
    for file_path in md_files:
        all_errors.extend(validate_file(file_path, args.profile))

    if all_errors:
        print("Validation failed:")
        for err in all_errors:
            print(f"- {err}")
        return 1

    print(f"Validation passed ({len(md_files)} files, profile={args.profile})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
