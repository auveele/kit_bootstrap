# API Contracts

Project: Acme Portal
Version: 1.0
Status: Active

## Endpoints

| Endpoint | Method | Input | Output | Errors |
|---|---|---|---|---|
| `/api/auth/login` | POST | email/password | token + user | 401, 422 |
| `/api/requests` | POST | request payload | request record | 400, 422 |
| `/api/requests/{id}` | PATCH | status/owner fields | updated request | 404, 422 |

## References

- `backend-architecture-flask.md`
- `../10_product/product-requirements.md`
