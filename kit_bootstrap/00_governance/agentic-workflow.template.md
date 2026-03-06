# Agentic Workflow (IDE + LLM)

Project: {{PROJECT_NAME}}
Version: {{DOC_VERSION}}
Status: Active

## 1. Objective

Run end-to-end execution with LLM support while preserving quality,
traceability, and delivery discipline.

## 2. Official phase model

1. F0 Discovery
2. F1 Planning
3. F2 Architecture
4. F3 Build
5. F4 QA
6. F5 Release

Do not advance with open `A0` questions.

## 3. Mandatory Task Packet

Every task must include:
1. objective
2. scope in/out
3. involved SoT
4. expected file-level changes
5. acceptance criteria
6. verification method
7. risk and rollback

## 4. Prompt template

```text
Objective:

Minimum context:

Source of Truth:
-

Change instructions:
-

Acceptance criteria:
- [ ]

Verification:
-

Do not:
-
```

## 5. Definition of Done for agent tasks

- [ ] acceptance criteria are met
- [ ] no SoT conflicts introduced
- [ ] related docs are updated
- [ ] verification evidence exists
- [ ] stack coherence kept (React + Flask + SQLAlchemy + SQLite)
