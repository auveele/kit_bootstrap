# Quickstart

1. Complete required project inputs in `INIT.md`.
2. Copy templates from `kit_bootstrap/` to `docs/`.
3. Generate core docs first (`document-index`, `prd`, `product-requirements`,
   `domain-model`, `architecture-overview`, `api-contracts`, roadmap/gates/
   backlog/status, open questions, traceability matrix).
4. Replace all placeholders `{{...}}` with project data.
5. Define SoT ownership in Document Index.
6. Confirm stack baseline references: React + Flask + SQLAlchemy + SQLite.
7. Define phase plan: F0 Discovery to F5 Release.
8. Build P0/P1/P2 backlog with acceptance criteria.
9. Add extended docs only when needed.
10. Run validation checks (links, duplication, coherence, traceability).
11. Update release notes with bootstrap initialization.

Suggested validation command:

```bash
python tools/validate_docs.py --root docs --profile project
```

Run full execution checks:

```bash
python tools/bootstrap.py check --root docs
```

Expected result:
- operational execution system,
- roadmap by phase,
- working gates and backlog,
- requirement traceability to gates and release,
- clear role ownership,
- reusable context packets for LLM tasks,
- traceability for future sessions.
