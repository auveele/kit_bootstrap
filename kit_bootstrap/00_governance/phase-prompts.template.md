# Phase Prompts

Status: Active
Version: {{DOC_VERSION}}

## Objective

Provide strict phase prompts so the LLM executes with predictable inputs,
outputs, and machine-readable results.

## Prompt contract (all phases)

```text
Task Packet:
- objective
- scope_in
- scope_out
- source_of_truth
- acceptance_criteria
- verification
- rollback

Return JSON:
{
  "phase": "F0|F1|F2|F3|F4|F5",
  "status": "pass|fail",
  "artifacts_updated": ["..."],
  "open_questions": ["OQ-..."],
  "risks": ["..."],
  "next_actions": ["..."]
}
```

## F0 Discovery prompt

- input docs: PRD draft, open questions log
- required output: confirmed vision/problem/users/KPI baseline

## F1 Planning prompt

- input docs: PRD, product requirements
- required output: prioritized backlog aligned to FR/NFR

## F2 Architecture prompt

- input docs: domain model, data dictionary, requirements
- required output: architecture and API contracts with tradeoffs

## F3 Build prompt

- input docs: architecture and API contracts
- required output: implemented scope with verification evidence

## F4 QA prompt

- input docs: backlog, gates, status
- required output: quality evidence and unresolved defect list

## F5 Release prompt

- input docs: QA evidence, release notes
- required output: go/no-go decision and rollback plan
