# Domain Model

Project: Acme Portal
Version: 1.0
Status: Active

## Bounded contexts

| Context | Responsibility | Owner |
|---|---|---|
| Identity | user auth and session state | Backend |
| Requests | lifecycle of support requests | Product + Backend |
| Assignment | ownership and team routing | Ops |

## Core entities

| Entity | Purpose |
|---|---|
| User | authenticated actor |
| Request | work item to process |
| Assignment | ownership relation |

## References

- `data-dictionary.md`
- `../40_technical/architecture-overview.md`
