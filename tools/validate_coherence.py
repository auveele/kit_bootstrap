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
TRACE_ROW_RE = re.compile(
    r"^\|\s*((?:FR|NFR)-\d{3})\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|",
    re.MULTILINE,
)

FRONTMATTER_REQUIRED_FIELDS = {
    "doc_id",
    "title",
    "owner",
    "status",
    "version",
    "phase",
    "sot",
    "depends_on",
    "last_updated",
}

REQUIRED_ROOT_DIRS = [
    ".run_cache",
    "backend",
    "docs",
    "frontend",
    "instance",
    "scripts",
    "tools",
]

REQUIRED_ROOT_FILES = [
    ".gitignore",
    "README.md",
]


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


def parse_frontmatter(doc: str) -> dict[str, str]:
    lines = doc.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        return {}

    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def validate_frontmatter(required_path: Path, content: str, errors: list[str]) -> None:
    fields = parse_frontmatter(content)
    if not fields:
        errors.append(f"Missing frontmatter in core doc: {required_path}")
        return

    missing = sorted(FRONTMATTER_REQUIRED_FIELDS - set(fields.keys()))
    if missing:
        errors.append(
            f"Missing frontmatter fields in {required_path}: {', '.join(missing)}"
        )

    status = fields.get("status", "")
    if status not in {"Active", "Draft", "Archived"}:
        errors.append(f"Invalid frontmatter status in {required_path}: {status}")

    phase = fields.get("phase", "")
    if phase not in {"F0", "F1", "F2", "F3", "F4", "F5"}:
        errors.append(f"Invalid frontmatter phase in {required_path}: {phase}")


def parse_traceability(trace_doc: str) -> list[tuple[str, str, str, str, str]]:
    rows: list[tuple[str, str, str, str, str]] = []
    for match in TRACE_ROW_RE.finditer(trace_doc):
        req_id, backlog_item, gate, evidence, release_note = (
            match.group(1).strip(),
            match.group(2).strip(),
            match.group(3).strip(),
            match.group(4).strip(),
            match.group(5).strip(),
        )
        rows.append((req_id, backlog_item, gate, evidence, release_note))
    return rows


def validate_repository_layout(docs_root: Path, errors: list[str]) -> None:
    repo_root = docs_root.parent

    for dir_name in REQUIRED_ROOT_DIRS:
        dir_path = repo_root / dir_name
        if not dir_path.exists() or not dir_path.is_dir():
            errors.append(f"Missing required root directory: {dir_path}")

    for file_name in REQUIRED_ROOT_FILES:
        file_path = repo_root / file_name
        if not file_path.exists() or not file_path.is_file():
            errors.append(f"Missing required root file: {file_path}")

    backend_venv = repo_root / "backend" / ".venv"
    if not backend_venv.exists() or not backend_venv.is_dir():
        errors.append(f"Missing required backend virtualenv directory: {backend_venv}")


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
        "traceability": root / "50_delivery" / "traceability-matrix.md",
        "open_questions": root / "60_open-questions" / "open-questions-log.md",
    }

    if not root.exists():
        print(f"ERROR: docs root does not exist: {root}")
        return 2

    validate_repository_layout(root, errors)

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
    traceability_doc = read_text(required["traceability"])

    for req_name, req_path in required.items():
        if req_name == "open_questions":
            continue
        content = read_text(req_path)
        validate_frontmatter(req_path, content, errors)

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

    trace_rows = parse_traceability(traceability_doc)
    if not trace_rows:
        errors.append("No traceability rows found in traceability-matrix.md")

    traced_req_ids = {row[0] for row in trace_rows}
    missing_in_traceability = sorted(requirement_ids - traced_req_ids)
    if missing_in_traceability:
        errors.append(
            "Requirements missing in traceability matrix: "
            + ", ".join(missing_in_traceability)
        )

    for req_id, backlog_item, gate, evidence, release_note in trace_rows:
        if not backlog_item:
            errors.append(f"Traceability row missing backlog item for {req_id}")
        if gate not in phases:
            errors.append(f"Traceability row has unknown gate '{gate}' for {req_id}")
        if not evidence:
            errors.append(f"Traceability row missing evidence for {req_id}")
        if not release_note:
            errors.append(
                f"Traceability row missing release note reference for {req_id}"
            )

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
