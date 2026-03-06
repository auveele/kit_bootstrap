# Backend Architecture (Flask)

Project: Acme Portal
Version: 1.0
Status: Active

## Service structure

- `app/api` for HTTP endpoints
- `app/services` for business rules
- `app/models` for SQLAlchemy models

## Persistence

- SQLAlchemy models for User, Request, Assignment.
- SQLite for bootstrap and local development.

## References

- `api-contracts.md`
- `../20_systems/data-dictionary-complete.md`
