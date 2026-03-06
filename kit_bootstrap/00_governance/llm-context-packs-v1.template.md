# LLM Context Packs v1

Project: {{PROJECT_NAME}}
Version: {{DOC_VERSION}}
Status: Active

## 1. Objective

Define minimal context bundles by role for IDE + LLM tasks.

## 2. Global rule

- Each prompt includes only 2-4 capsules + 2-4 SoT docs.
- Avoid oversized and ambiguous context.
- Prefer core SoT docs before extended docs.

## 3. Suggested packs

### Product Pack

- CAP-001 (MVP Scope)
- CAP-003 (KPI and Gates)
- `docs/10_product/prd.md`
- `docs/50_delivery/phase-roadmap.md`

### Tech Pack

- CAP-002 (Stack)
- CAP-004 (API and Data)
- `docs/40_technical/architecture-overview.md`
- `docs/40_technical/api-contracts.md`

### UX Pack

- CAP-001 (MVP Scope)
- CAP-005 (Risks)
- `docs/10_product/user-flows.md`
- `docs/30_experience/ui-ux.md`

### QA/Docs Pack

- CAP-003 (KPI and Gates)
- CAP-005 (Risks)
- `docs/00_governance/reference-rules.md`
- `docs/50_delivery/phase-gates.md`
