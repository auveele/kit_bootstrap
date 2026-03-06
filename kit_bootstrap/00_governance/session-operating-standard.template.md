# Session Operating Standard

Project: {{PROJECT_NAME}}
Version: {{DOC_VERSION}}
Status: Active

## 1. Objective

Define how development/documentation sessions operate with cross-session
continuity.

## 2. Official structure

- Root: `.run_cache/`, `backend/`, `docs/`, `frontend/`, `instance/`,
  `scripts/`, `tools/`, `.gitignore`, `README.md`.
- Backend virtualenv location: `backend/.venv`.
- Active documentation only in `docs/`.
- Historical docs in `docs/90_archive/`.

## 3. Phase flow

- Work runs by PASS/FAIL gates.
- Do not advance with open `A0` questions.

## 4. Prioritization

- P0 blocking
- P1 critical
- P2 incremental

## 5. New artifact intake

1. classify active vs archived,
2. move to correct domain,
3. update links,
4. update index/release notes,
5. track open questions.

## 6. Session close checklist

- [ ] links validated
- [ ] decision log updated
- [ ] release notes updated
- [ ] risks/questions refreshed
- [ ] phase and gate status refreshed
- [ ] repository layout matches operating standard
- [ ] backend virtualenv path is `backend/.venv`
