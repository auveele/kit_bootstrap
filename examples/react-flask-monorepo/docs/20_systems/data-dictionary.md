# Data Dictionary

Project: Acme Portal
Version: 1.0
Status: Active

## Key entities

| Entity | Description |
|---|---|
| User | system account |
| Request | customer request |
| Assignment | request owner mapping |

## Key fields

| Entity | Field | Logical type | Notes |
|---|---|---|---|
| User | email | string | unique |
| Request | status | enum | open/in_progress/done |
| Assignment | owner_id | uuid | references user |

## References

- `data-dictionary-complete.md`
- `../40_technical/backend-architecture-flask.md`
