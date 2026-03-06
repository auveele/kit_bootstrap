# Tools Reference

This folder contains the validation and execution wrappers used by the
bootstrap system.

## Files

### `bootstrap.py`

Command wrapper to run all project-level checks in sequence.

Current command:

```bash
python tools/bootstrap.py check --root docs
```

Scaffold command:

```bash
python tools/bootstrap.py scaffold --project-name "My Project" --out docs
```

What it runs:
- `validate_docs.py` with `--profile project`
- `validate_coherence.py`

For `scaffold`, it delegates to `scaffold_docs.py`.

### `scaffold_docs.py`

Generator that creates `docs/` from `kit_bootstrap/*.template.md` files.

Features:
- converts `*.template.md` to `.md`,
- preserves folder structure,
- replaces `{{PROJECT_NAME}}`, `{{DOC_VERSION}}`, `{{STATUS}}`,
- optionally overwrites existing files with `--force`.

Example:

```bash
python tools/scaffold_docs.py --project-name "My Project" --out docs --status Draft
```

Use it as the default gate command in local work and CI.

### `validate_docs.py`

Markdown validator for structure-level quality.

Checks:
- broken local markdown links,
- unresolved placeholders (`{{...}}`) in project profile,
- banned domain terms (legacy gaming vocabulary).

Profiles:
- `templates`: allows unresolved `docs/*` links and placeholders.
- `project`: requires all links/placeholders to be resolved.

Examples:

```bash
python tools/validate_docs.py --root . --profile templates
python tools/validate_docs.py --root docs --profile project
```

### `validate_coherence.py`

Cross-document consistency validator for delivery flow.

Checks:
- target repository layout exists at root (`.run_cache`, `backend`, `docs`,
  `frontend`, `instance`, `scripts`, `tools`, `.gitignore`, `README.md`),
- backend virtualenv path exists at `backend/.venv`,
- required files exist,
- core docs include required frontmatter fields,
- FR/NFR IDs in `10_product/product-requirements.md` are referenced in
  `50_delivery/priority-backlog.md`,
- phases in `50_delivery/phase-roadmap.md` exist in
  `50_delivery/phase-gates.md` and `50_delivery/project-status.md`,
- FR/NFR IDs are present in `50_delivery/traceability-matrix.md`,
- each traceability row has backlog item, valid phase gate, evidence, and
  release note,
- no open `A0` item remains in `60_open-questions/open-questions-log.md`.

Example:

```bash
python tools/validate_coherence.py --root docs
```

## Recommended usage pattern

1. During template maintenance:
   `python tools/validate_docs.py --root . --profile templates`
2. During project execution:
   `python tools/bootstrap.py check --root docs`
3. For the included example:
   `python tools/bootstrap.py check --root examples/react-flask-monorepo/docs`
