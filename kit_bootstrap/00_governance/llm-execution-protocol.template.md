# LLM Execution Protocol

Status: Active
Version: {{DOC_VERSION}}

## 1. Objective

Optimize context usage, reduce ambiguity, and preserve continuity across LLM
sessions.

## 2. Context budgets

- Planning tasks: 2-3 capsules + 2-3 SoT docs.
- Architecture tasks: 2-4 capsules + 3-4 SoT docs.
- Build tasks: 1-2 capsules + 2-3 SoT docs.
- QA tasks: 2 capsules + 2-4 SoT docs.

If context exceeds budget, summarize first and link SoT.

## 3. Session handoff format

```text
Session Handoff
- Current phase:
- Last completed task:
- Active blockers:
- Open A0/A1:
- Top 3 next actions:
- Risks:
- Files updated this session:
```

## 4. Anti-drift rules

- If API contracts change, review requirements and backlog references.
- If architecture changes, review deployment and security docs.
- If PRD scope changes, refresh roadmap and gates.

## 5. Stop conditions

- Open A0 in current phase.
- Missing SoT for requested change.
- Failing gate with no approved waiver.
