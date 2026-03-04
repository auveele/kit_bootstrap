# Kit Bootstrap

Bootstrap your project documentation system for teams where humans and LLMs
work together on product, technical, and delivery decisions.

`kit_bootstrap` gives you a practical structure to create a high-signal `docs/`
workspace with clear ownership, phase gates, and reusable context for AI-assisted
execution.

## Why this exists

Most projects with AI-assisted workflows hit the same issues:

- key decisions are made but not traceable,
- docs drift or duplicate each other,
- prompts are either missing critical context or overloaded,
- roadmap and backlog become disconnected from actual progress.

This kit provides an opinionated baseline to prevent that from day one.

## Core principles

- One topic = one Source of Truth (SoT).
- If a SoT already exists, summarize and link; do not duplicate.
- Move in phases with explicit `PASS/FAIL` gates.
- `A0` open questions block phase advancement.
- Prioritize continuously: `P0` blocking, `P1` critical, `P2` incremental.
- Track structural changes in decision log and release notes.

## What you get

- `INIT.md`: master prompt for bootstrapping complete project docs.
- `kit_bootstrap/`: template library to generate your `docs/` folder.
- Governance templates: document index, reference rules, editorial QA,
  decision log, release notes.
- Product templates: PRD, GDD-lite, core loops.
- Systems templates: balance sheet, data dictionary, detailed data model.
- Experience templates: UI/UX, localization, event/content bible, narrative.
- Technical templates: ADD and domain specs.
- Delivery templates: phase roadmap, phase gates, backlog, project status,
  meeting templates.
- AI collaboration templates: info capsules and LLM context packs by role.
- Operational role templates: ultralight roles, RACI matrix, role playbooks.

## Repository structure

```text
.
|- INIT.md
|- LICENSE
|- README.md
`- kit_bootstrap/
   |- 00_governance/
   |- 10_product/
   |- 20_systems/
   |- 30_experience/
   |- 40_technical/
   |- 50_delivery/
   |- 60_open-questions/
   |- 90_archive/
   |- QUICKSTART.md
   `- README.md
```

## Quick start

1. Fill project inputs in `INIT.md`.
2. Copy templates from `kit_bootstrap/` into your target project's `docs/`.
3. Replace all `{{...}}` placeholders with project-specific data.
4. Build docs in this order:
   - `docs/00_governance/*`
   - `docs/10_product/*`
   - `docs/20_systems/*`
   - `docs/30_experience/*`
   - `docs/40_technical/*`
   - `docs/50_delivery/*`
   - `docs/60_open-questions/*`
5. Run final validation:
   - no critical duplication,
   - no broken links,
   - PRD, roadmap, backlog, and gates are coherent,
   - `A0` questions are resolved or explicitly documented.

For a shorter setup checklist, see `kit_bootstrap/QUICKSTART.md`.

## Human + LLM workflow (recommended)

For each task, prepare a compact task packet with:

- objective,
- in/out scope,
- involved SoTs,
- expected file-level changes,
- acceptance criteria,
- verification steps,
- risk and rollback.

This keeps prompts focused and improves consistency across contributors
(both human and AI).

## Template domains

- `00_governance`: operating rules, quality checks, and traceability.
- `10_product`: product vision, value loops, and MVP boundaries.
- `20_systems`: entities, data model, and balancing rules.
- `30_experience`: UX, content operations, localization, narrative.
- `40_technical`: architecture decisions and technical specs.
- `50_delivery`: roadmap, gates, priorities, and execution status.
- `60_open-questions`: unresolved decisions and closure tracking.
- `90_archive`: historical docs that are not active SoT.

## Intended audience

- GitHub-native teams documenting decisions in Markdown.
- Builders shipping with IDE + LLM workflows.
- Early-stage projects needing structure without heavyweight process.

## License

Apache 2.0. See `LICENSE`.
