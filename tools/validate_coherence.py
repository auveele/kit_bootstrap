#!/usr/bin/env python3
"""Cross-document coherence checks for the execution system."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQ_ID_RE = re.compile(r"\b(?:FR|NFR)-\d{3}\b")
PHASE_RE = re.compile(r"^###\s+(F\d+)\b", re.MULTILINE)
GATE_RE = re.compile(r"^##\s+Gate\s+(F\d+)\b", re.MULTILINE)
STATUS_PHASE_RE = re.compile(r"\|\s*(F\d+)\s+[A-Za-z]+\s*\|")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate cross-doc coherence")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path("docs"),
        help="Docs root path",
    )
    return parser.parse_args()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def existing(path: Path, errors: list[str]) -> bool:
    if path.exists():
        return True
    errors.append(f"Missing required file: {path}")
    return False


def parse_requirement_ids(requirements_doc: str) -> set[str]:
    return set(REQ_ID_RE.findall(requirements_doc))


def parse_backlog_refs(backlog_doc: str) -> set[str]:
    return set(REQ_ID_RE.findall(backlog_doc))


def parse_phases(roadmap_doc: str) -> set[str]:
    return set(PHASE_RE.findall(roadmap_doc))


def parse_gates(gates_doc: str) -> set[str]:
    return set(GATE_RE.findall(gates_doc))


def parse_status_phases(status_doc: str) -> set[str]:
    return set(STATUS_PHASE_RE.findall(status_doc))


def has_open_a0(open_questions_doc: str) -> bool:
    for line in open_questions_doc.splitlines():
        lowered = line.lower()
        if "|" not in line:
            continue
        if "a0" in lowered and "open" in lowered:
            return True
    return False


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    errors: list[str] = []

    required = {
        "requirements": root / "10_product" / "product-requirements.md",
        "roadmap": root / "50_delivery" / "phase-roadmap.md",
        "gates": root / "50_delivery" / "phase-gates.md",
        "backlog": root / "50_delivery" / "priority-backlog.md",
        "status": root / "50_delivery" / "project-status.md",
        "open_questions": root / "60_open-questions" / "open-questions-log.md",
    }

    if not root.exists():
        print(f"ERROR: docs root does not exist: {root}")
        return 2

    for p in required.values():
        existing(p, errors)

    if errors:
        print("Coherence validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    requirements_doc = read_text(required["requirements"])
    roadmap_doc = read_text(required["roadmap"])
    gates_doc = read_text(required["gates"])
    backlog_doc = read_text(required["backlog"])
    status_doc = read_text(required["status"])
    open_questions_doc = read_text(required["open_questions"])

    requirement_ids = parse_requirement_ids(requirements_doc)
    backlog_refs = parse_backlog_refs(backlog_doc)
    phases = parse_phases(roadmap_doc)
    gates = parse_gates(gates_doc)
    status_phases = parse_status_phases(status_doc)

    if not requirement_ids:
        errors.append("No FR/NFR IDs found in product-requirements.md")

    missing_req_in_backlog = sorted(requirement_ids - backlog_refs)
    if missing_req_in_backlog:
        errors.append(
            "Requirements missing in backlog references: "
            + ", ".join(missing_req_in_backlog)
        )

    missing_gates = sorted(phases - gates)
    if missing_gates:
        errors.append(
            "Roadmap phases missing gate definitions: " + ", ".join(missing_gates)
        )

    missing_status_phases = sorted(phases - status_phases)
    if missing_status_phases:
        errors.append(
            "Roadmap phases missing in project status table: "
            + ", ".join(missing_status_phases)
        )

    if has_open_a0(open_questions_doc):
        errors.append("Open A0 question detected in open-questions-log.md")

    if errors:
        print("Coherence validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Coherence validation passed")
    print(f"- requirements tracked: {len(requirement_ids)}")
    print(f"- phases tracked: {len(phases)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
