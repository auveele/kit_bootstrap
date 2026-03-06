---
doc_id: PRO-002
title: Product Requirements
owner: Product
status: Active
version: "1.0"
phase: F1
sot: true
depends_on: [PRO-001]
last_updated: 2026-03-06
---

# Product Requirements

Project: Acme Portal
Version: 1.0
Status: Active

## Functional requirements

| ID | Requirement | Priority | Acceptance criteria |
|---|---|---|---|
| FR-001 | User can sign in and sign out | P0 | Auth session works end-to-end |
| FR-002 | User can create and update requests | P0 | CRUD operations succeed via API |
| FR-003 | Team lead can assign request owner | P1 | Assignment visible in UI and API |

## Non-functional requirements

| ID | Requirement | Target |
|---|---|---|
| NFR-001 | API latency p95 | < 400ms in staging |
| NFR-002 | Availability | >= 99.5% monthly |

## References

- `prd.md`
- `../40_technical/api-contracts.md`
- `../50_delivery/priority-backlog.md`
