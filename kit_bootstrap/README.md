# Kit Bootstrap

Execution-system templates to bootstrap a complete project operating model.

Goal:
- define one Source of Truth per domain,
- prevent duplication,
- run work by phases with gates,
- keep traceability for human + LLM execution,
- drive delivery from planning to release.
- keep a core-first structure to minimize context noise.

Fixed stack baseline:
- frontend: React
- backend: Flask
- ORM: SQLAlchemy
- bootstrap DB: SQLite (`sqlite3`)

Recommended usage:
1. Complete `INIT.md` with project inputs.
2. Generate final docs in `docs/` using these templates.
3. Validate links, SoT ownership, and gate readiness.

Suggested validation command:

```bash
python tools/validate_docs.py --root docs --profile project
```

Unified check command:

```bash
python tools/bootstrap.py check --root docs
```

Structure:
- `00_governance/`: rules, index, decisions, QA, releases, role ops.
- `10_product/`: vision, PRD, requirements, user flows.
- `20_systems/`: domain model and data definitions.
- `30_experience/`: UI/UX, localization, content operations.
- `40_technical/`: React/Flask architecture, APIs, security, deployment.
- `50_delivery/`: roadmap, status, gates, backlog, meeting templates.
- `60_open-questions/`: unresolved questions and tracking.
- `90_archive/`: historical, not active SoT.

Core-first policy:
- Core docs are mandatory for execution.
- Extended docs are optional by project need.

LLM optimization docs:
- `00_governance/docs-schema.template.md`
- `00_governance/phase-prompts.template.md`
- `00_governance/llm-execution-protocol.template.md`

Note:
- This kit is not a passive template library.
- It is an execution system for LLM-driven planning and delivery.
