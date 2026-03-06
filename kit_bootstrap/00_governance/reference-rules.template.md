# Reference Rules

Project: {{PROJECT_NAME}}
Version: {{DOC_VERSION}}
Status: Active

## 1. Objective

Define global rules to prevent duplication and preserve traceability.

## 2. Global rules

- 1 topic = 1 Source of Truth.
- If SoT exists, summarize and link.
- Do not copy large blocks across documents.
- Newest approved version has priority.
- Keep stack assumptions aligned with React + Flask + SQLAlchemy + SQLite.

## 3. Duplication control (mandatory)

Before publishing any document:

- [ ] Existing SoT for this topic was checked.
- [ ] If SoT exists, this document links and does not duplicate.
- [ ] Tables/formulas from other SoT are not repeated.
- [ ] Document Index was updated when applicable.

Decision rule:
- If SoT exists -> do not create a new SoT.
- If SoT does not exist -> create one and register it.

## 4. Reference rules

- Use links to real `.md` files.
- Avoid ambiguous references.
- Revalidate links after moves/renames.

## 5. Traceability

- Structural changes -> decision log.
- Version changes -> release notes.

## 6. Schema rule

- Core docs must include the frontmatter contract from
  `docs/00_governance/docs-schema.md`.
