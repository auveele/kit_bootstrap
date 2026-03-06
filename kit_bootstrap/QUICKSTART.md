# Quickstart

1. Complete required project inputs in `INIT.md`.
2. Copy templates from `kit_bootstrap/` to `docs/`.
3. Replace all placeholders `{{...}}` with real project data.
4. Define SoT ownership in Document Index.
5. Confirm stack baseline references: React + Flask + SQLAlchemy + SQLite.
6. Define phase plan: F0 Discovery to F5 Release.
7. Build P0/P1/P2 backlog with acceptance criteria.
8. Run validation checks (links, duplication, coherence).
9. Update release notes with bootstrap initialization.

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
- clear role ownership,
- reusable context packets for LLM tasks,
- traceability for future sessions.
