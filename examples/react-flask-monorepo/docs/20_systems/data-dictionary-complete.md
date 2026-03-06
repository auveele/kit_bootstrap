# Data Dictionary Complete

Project: Acme Portal
Version: 1.0
Status: Active

## Detailed model

| Table | Field | Type | Null | PK/FK | Index |
|---|---|---|---|---|---|
| users | id | uuid | no | PK | yes |
| users | email | varchar(255) | no | - | yes |
| requests | id | uuid | no | PK | yes |
| requests | status | varchar(32) | no | - | yes |
| assignments | request_id | uuid | no | FK | yes |
| assignments | owner_id | uuid | no | FK | yes |

## ORM notes

- SQLAlchemy declarative models are source for persistence mappings.
- SQLite is bootstrap DB for local and CI smoke tests.

## References

- `data-dictionary.md`
- `../40_technical/backend-architecture-flask.md`
