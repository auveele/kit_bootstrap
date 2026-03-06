# Kit Bootstrap

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Docs: Markdown](https://img.shields.io/badge/docs-markdown-informational.svg)](#)
[![Workflow: Agent-First](https://img.shields.io/badge/workflow-agent--first-0a7ea4.svg)](#agent-first-default)

Execution system bootstrap for software projects run primarily by an
autonomous agent, with optional human review.

## 30-second pitch

If your project runs with AI in the loop, this repo gives you a practical
operating system for end-to-end execution:

- one Source of Truth per topic,
- phase-based execution with `PASS/FAIL` gates,
- explicit open-question tracking (`A0/A1/A2`),
- decision and release traceability,
- reusable context packets for consistent LLM execution,
- built-in defaults for React frontend + Flask backend.
- core-first documentation model (mandatory + optional layers).

It is focused on web product delivery with a fixed stack baseline:
React frontend + Flask backend + SQLAlchemy ORM + SQLite bootstrap DB.

## Quick start

The minimal flow is intentionally simple:

1. Copy this kit into your project root.
2. Ask your LLM to read `INIT.md` and proceed.

That is enough to start.

If you need to fetch the kit first, use one of these options.

Clone the repo:

```bash
git clone https://github.com/auveele/kit_bootstrap.git
```

Or download files only (no `.git`, no git metadata) directly into your project root:

```bash
curl -L https://github.com/auveele/kit_bootstrap/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=1
```

## Why this exists

Agentic software workflows often fail in predictable ways:

- decisions are made but not auditable,
- docs duplicate each other and drift,
- prompts are ambiguous or overloaded,
- roadmap/backlog lose alignment with real execution.

`kit_bootstrap` is an opinionated baseline to avoid that from day one and
move from planning to delivery with a single operating model.

## Agent-first default

- One agent plans, phases, executes, validates, and updates docs.
- Human input is optional and focused on constraints/approval.
- If no human input is available, the agent continues with explicit
  assumptions tracked in open questions + decision log.

## Core principles

- One topic = one Source of Truth (SoT).
- If a SoT exists, summarize + link; do not duplicate.
- Work in phases with explicit `PASS/FAIL` gates.
- `A0` open questions block phase progression.
- Priority model: `P0` blocking, `P1` critical, `P2` incremental.
- Structural changes must be tracked in decision log and release notes.

## What you get

- `INIT.md`: master bootstrap prompt.
- `kit_bootstrap/`: execution-system templates to generate your `docs/`.
- Governance templates: document index, reference rules, editorial QA,
  decision log, release notes.
- Execution templates: phase prompts, LLM execution protocol, docs schema.
- Product templates: PRD, requirements, MVP scope, user flows.
- Systems templates: domain model, data dictionary, detailed model.
- Experience templates: UI/UX, localization, content operations, narrative.
- Technical templates: React/Flask architecture, API contracts, security, deployment.
- Delivery templates: roadmap, phase gates, backlog, status, meeting templates.
- Delivery assurance templates: traceability matrix.
- LLM templates: info capsules and role-oriented context packs.
- Validation tooling: markdown checks + CI gate workflow.
- Example project docs: ready-to-run React + Flask monorepo sample.

## Repository structure

```text
.
|- INIT.md
|- LICENSE
|- README.md
|- tools/
|  |- bootstrap.py
|  |- validate_docs.py
|  `- validate_coherence.py
|- examples/
|  `- react-flask-monorepo/
|     `- docs/
`- kit_bootstrap/
   |- 00_governance/
   |- 10_product/
   |- 20_systems/
   |- 30_experience/
   |- 40_technical/
   |- 50_delivery/
   |- 60_open-questions/
   |- 90_archive/
   |- QUICKSTART.md
   `- README.md
```

## Suggested generation order

1. `docs/00_governance/*`
2. `docs/10_product/*`
3. `docs/20_systems/*`
4. `docs/30_experience/*`
5. `docs/40_technical/*`
6. `docs/50_delivery/*`
7. `docs/60_open-questions/*`

Final checks:

- no critical duplication,
- no broken links,
- PRD/roadmap/backlog/gates coherence,
- `A0` questions resolved or explicitly documented.
- stack coherence for React + Flask + SQLAlchemy + SQLite bootstrap.
- FR/NFR traceability to gates and release.

See `kit_bootstrap/QUICKSTART.md` for the compact checklist.

Template validation command:

```bash
python tools/validate_docs.py --root . --profile templates
```

Project validation command:

```bash
python tools/validate_docs.py --root docs --profile project
```

Unified check command:

```bash
python tools/bootstrap.py check --root docs
```

Core-first rollout:

- Core docs are mandatory and should be generated first.
- Extended docs are optional and should only be created when needed.

Check the included example end-to-end:

```bash
python tools/bootstrap.py check --root examples/react-flask-monorepo/docs
```

Tooling reference:

- `tools/README.md`

## Who this is for

- GitHub-native builders working in Markdown.
- Projects using LLMs to drive planning + execution.
- Teams or solo operators who want disciplined delivery without heavyweight process.

## License

Apache 2.0. See `LICENSE`.
