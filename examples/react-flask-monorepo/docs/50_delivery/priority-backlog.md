---
doc_id: DEL-003
title: Priority Backlog
owner: Product
status: Active
version: "1.0"
phase: F1
sot: true
depends_on: [PRO-002]
last_updated: 2026-03-06
---

# Priority Backlog

Project: Acme Portal
Version: 1.0
Status: Active

## P0
1. Implement auth flow (`FR-001`) - Open
2. Implement request CRUD (`FR-002`) - Open
3. Enforce API latency target (`NFR-001`) - Open

## P1
1. Implement assignment flow (`FR-003`) - Open
2. Add uptime monitoring (`NFR-002`) - Open

## P2
1. Improve bulk request editing - Open

## Rule

- If A0 exists, close A0 first.
- If no A0 exists, execute P0 first.
