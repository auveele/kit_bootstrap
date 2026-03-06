# Architecture Overview

Project: Acme Portal
Version: 1.0
Status: Active

## Stack baseline

- Frontend: React in `frontend/`
- Backend: Flask in `backend/`
- ORM: SQLAlchemy
- Bootstrap DB: SQLite

## Component architecture

- React UI consumes Flask REST API.
- Flask service handles auth, request lifecycle, and assignment.
- SQLAlchemy maps domain entities to persistence.

## References

- `frontend-architecture-react.md`
- `backend-architecture-flask.md`
- `api-contracts.md`
