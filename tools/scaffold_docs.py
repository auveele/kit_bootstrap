#!/usr/bin/env python3
"""Scaffold docs/ from kit_bootstrap templates."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scaffold docs from templates")
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("kit_bootstrap"),
        help="Template source directory",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("docs"),
        help="Output docs directory",
    )
    parser.add_argument(
        "--project-name",
        required=True,
        help="Project name replacement for {{PROJECT_NAME}}",
    )
    parser.add_argument(
        "--doc-version",
        default="1.0",
        help="Document version replacement for {{DOC_VERSION}}",
    )
    parser.add_argument(
        "--status",
        default="Draft",
        choices=["Active", "Draft", "Archived"],
        help="Replacement for {{STATUS}}",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing markdown files",
    )
    return parser.parse_args()


def target_for_template(source_root: Path, out_root: Path, template_file: Path) -> Path:
    rel = template_file.relative_to(source_root)
    name = rel.name
    target_name = name.replace(".template.md", ".md")
    return out_root / rel.parent / target_name


def apply_replacements(
    content: str, project_name: str, doc_version: str, status: str
) -> str:
    replaced = content.replace("{{PROJECT_NAME}}", project_name)
    replaced = replaced.replace("{{DOC_VERSION}}", doc_version)
    replaced = replaced.replace("{{STATUS}}", status)
    return replaced


def main() -> int:
    args = parse_args()
    source_root = args.source.resolve()
    out_root = args.out.resolve()

    if not source_root.exists():
        print(f"ERROR: source path does not exist: {source_root}")
        return 2

    template_files = sorted(source_root.rglob("*.template.md"))
    if not template_files:
        print(f"ERROR: no template files found under: {source_root}")
        return 2

    out_root.mkdir(parents=True, exist_ok=True)

    created = 0
    overwritten = 0
    skipped = 0

    for template_file in template_files:
        target = target_for_template(source_root, out_root, template_file)
        target.parent.mkdir(parents=True, exist_ok=True)

        if target.exists() and not args.force:
            skipped += 1
            print(f"SKIP (exists): {target}")
            continue

        content = template_file.read_text(encoding="utf-8")
        rendered = apply_replacements(
            content,
            project_name=args.project_name,
            doc_version=args.doc_version,
            status=args.status,
        )

        if target.exists():
            overwritten += 1
        else:
            created += 1
        target.write_text(rendered, encoding="utf-8")
        print(f"WRITE: {target}")

    # Copy non-template helper markdown files at top-level (README/QUICKSTART).
    for helper in ("README.md", "QUICKSTART.md"):
        helper_src = source_root / helper
        if helper_src.exists():
            helper_dst = out_root / helper
            if helper_dst.exists() and not args.force:
                print(f"SKIP (exists): {helper_dst}")
                continue
            shutil.copy2(helper_src, helper_dst)
            print(f"COPY: {helper_dst}")

    print(
        "Scaffold complete: "
        f"created={created}, overwritten={overwritten}, skipped={skipped}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
