# Documentation Schema

Status: Active
Version: {{DOC_VERSION}}

## 1. Objective

Define a machine-readable contract for every active document.

## 2. Required frontmatter

Every active document must start with this YAML block:

```yaml
---
doc_id: DOC-XXX
title: Document Title
owner: Product|Tech|UX|QA-Docs|Ops-PM
status: Active|Draft|Archived
version: "1.0"
phase: F0|F1|F2|F3|F4|F5
sot: true|false
depends_on: []
last_updated: YYYY-MM-DD
---
```

## 3. ID convention

- Governance: GOV-XXX
- Product: PRO-XXX
- Systems: SYS-XXX
- Technical: TEC-XXX
- Delivery: DEL-XXX
- Open questions: OQ-XXX

## 4. Validation rules

- Missing required fields fails validation.
- `status` must be one of Active, Draft, Archived.
- `phase` must map to F0..F5.
- `depends_on` must only contain existing `doc_id` values.

## 5. Scope

- Core documents: mandatory schema compliance.
- Extended documents: recommended schema compliance.
