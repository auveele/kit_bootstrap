# Reference Rules

Project: Acme Portal
Version: 1.0
Status: Active

## Rules

- One topic has one Source of Truth.
- Summarize and link instead of duplicating content.
- All structural changes go to decision log and release notes.
- Stack assumptions are fixed: React + Flask + SQLAlchemy + SQLite.

## Validation

- Run `python tools/bootstrap.py check --root examples/react-flask-monorepo/docs`.
