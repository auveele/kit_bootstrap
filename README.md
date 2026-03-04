# Kit Bootstrap

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Docs: Markdown](https://img.shields.io/badge/docs-markdown-informational.svg)](#)
[![Workflow: Agent-First](https://img.shields.io/badge/workflow-agent--first-0a7ea4.svg)](#agent-first-default)

Documentation bootstrap for software projects executed primarily by an
autonomous agent, with optional human review.

## 30-second pitch

If your project runs with AI in the loop, this repo gives you a practical
operating system for documentation:

- one Source of Truth per topic,
- phase-based execution with `PASS/FAIL` gates,
- explicit open-question tracking (`A0/A1/A2`),
- decision and release traceability,
- reusable context packets for consistent LLM execution.

It is domain-agnostic, but defaults to web/app product work
(frontend + backend) out of the box.

## Copy-paste quick start

```bash
# from your target project root
mkdir -p docs
cp -r path/to/kit_bootstrap/kit_bootstrap/* docs/

# then use path/to/kit_bootstrap/INIT.md as your bootstrap prompt
# and replace all {{...}} placeholders in docs/
```

PowerShell variant:

```powershell
# from your target project root
New-Item -ItemType Directory -Force docs | Out-Null
Copy-Item -Recurse -Force path\to\kit_bootstrap\kit_bootstrap\* docs\

# then use path\to\kit_bootstrap\INIT.md as your bootstrap prompt
# and replace all {{...}} placeholders in docs\
```

## Why this exists

Agentic software workflows often fail in predictable ways:

- decisions are made but not auditable,
- docs duplicate each other and drift,
- prompts are ambiguous or overloaded,
- roadmap/backlog lose alignment with real execution.

`kit_bootstrap` is an opinionated baseline to avoid that from day one.

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
- `kit_bootstrap/`: template library to generate your `docs/`.
- Governance templates: document index, reference rules, editorial QA,
  decision log, release notes.
- Product templates: PRD, lightweight design docs, core loops.
- Systems templates: data dictionary, detailed model, balance sheet.
- Experience templates: UI/UX, localization, content operations, narrative.
- Technical templates: architecture decision docs and technical specs.
- Delivery templates: roadmap, phase gates, backlog, status, meeting templates.
- LLM templates: info capsules and role-oriented context packs.

## Repository structure

```text
.
|- INIT.md
|- LICENSE
|- README.md
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

See `kit_bootstrap/QUICKSTART.md` for the compact checklist.

## Who this is for

- GitHub-native builders working in Markdown.
- Projects using LLMs to drive planning + execution.
- Teams or solo operators who want disciplined delivery without heavyweight process.

## License

Apache 2.0. See `LICENSE`.
