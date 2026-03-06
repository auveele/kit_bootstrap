# Document Index

Project: {{PROJECT_NAME}}
Version: {{DOC_VERSION}}
Status: Active

## 1. Purpose

Master map of active documentation and dependencies.

## 2. Recommended reading order

1. `docs/50_delivery/project-status.md`
2. `docs/50_delivery/phase-roadmap.md`
3. `docs/10_product/prd.md`
4. `docs/10_product/product-requirements.md`
5. `docs/20_systems/domain-model.md`
6. `docs/40_technical/architecture-overview.md`

## 3. Core catalog (mandatory)

| Document | Primary role | SoT | Do not duplicate with |
|---|---|---|---|
| PRD | vision, scope, KPI | yes | Product Requirements |
| Product Requirements | functional and non-functional requirements | yes | PRD |
| User Flows | critical journeys and UX outcomes | yes | UI UX Spec |
| Domain Model | domain boundaries and entities | yes | Data Dictionary Complete |
| Architecture Overview | full technical architecture | yes | Frontend/Backend architecture |
| API Contracts | request/response contracts | yes | Backend Architecture |
| Traceability Matrix | requirement-to-delivery mapping | yes | Priority Backlog |
| Roles and Rituals | role model and lightweight rituals | yes | RACI Matrix |
| Role RACI Matrix | ownership per workflow | yes | Roles and Rituals |
| Info Capsules | reusable context summaries | yes | LLM Context Packs |
| LLM Context Packs | role-based context bundles | yes | Info Capsules |

## 4. Extended catalog (optional)

| Document | Purpose |
|---|---|
| UI UX Spec | deeper UX specifications |
| Localization Spec | multilingual delivery rules |
| Content Operations | content lifecycle and QA |
| Narrative README | non-technical positioning docs |
| Meeting Templates | operational facilitation templates |

## 5. Critical dependencies

- product -> systems -> technical -> delivery

## 6. Update policy

- Every new document must be registered here.
- Every structural change must be tracked in release notes.

## 7. Checklist

- [ ] docs are listed
- [ ] dependencies are coherent
- [ ] links are valid
- [ ] stack baseline is coherent (React + Flask + SQLAlchemy + SQLite)
- [ ] every core doc has frontmatter schema
