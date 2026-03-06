#!/usr/bin/env python3
"""Bootstrap command wrapper for validation workflows."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Bootstrap command wrapper")
    subparsers = parser.add_subparsers(dest="command", required=True)

    check = subparsers.add_parser("check", help="Run all validation checks")
    check.add_argument(
        "--root",
        type=Path,
        default=Path("docs"),
        help="Docs root path",
    )

    return parser.parse_args()


def run(cmd: list[str]) -> int:
    print("$", " ".join(cmd))
    completed = subprocess.run(cmd, check=False)
    return completed.returncode


def main() -> int:
    args = parse_args()

    if args.command == "check":
        docs_root = args.root
        checks = [
            [
                sys.executable,
                "tools/validate_docs.py",
                "--root",
                str(docs_root),
                "--profile",
                "project",
            ],
            [sys.executable, "tools/validate_coherence.py", "--root", str(docs_root)],
        ]

        for cmd in checks:
            code = run(cmd)
            if code != 0:
                return code

        print("All bootstrap checks passed")
        return 0

    return 2


if __name__ == "__main__":
    sys.exit(main())
