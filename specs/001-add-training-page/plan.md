# Implementation Plan: Add Training Page

**Branch**: `001-add-training-page` | **Date**: 2026-04-06 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-add-training-page/spec.md`

## Summary

Add a new "Training" static page to the site's top-level navigation,
listing 3 training courses Marco has delivered, each with a visual
element. Update the existing about page to reference the new
training page. The implementation follows the same Markdown-in-pages
pattern used by the bookshelf and about pages.

## Technical Context

**Language/Version**: Python (as specified in `pyproject.toml`)
**Primary Dependencies**: Pelican (static site generator)
**Storage**: Filesystem only — Markdown files in `content/pages/`
**Testing**: Manual build verification (`make html` or Pelican CLI)
**Target Platform**: Static file hosting (GitHub Pages)
**Project Type**: Static site / blog
**Performance Goals**: N/A — static HTML, no runtime processing
**Constraints**: All content MUST be Markdown; no external CMS or database
**Scale/Scope**: Single new page + minor edit to one existing page

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Static-First | ✅ PASS | Training page is a static Markdown page rendered to HTML. No server-side processing. |
| II. Markdown Content | ✅ PASS | New page authored as `.md` file with Pelican metadata header. |
| III. Pelican Pipeline | ✅ PASS | Page uses standard Pelican pages mechanism — no new generator or plugin needed. |
| IV. UV Dependency Management | ✅ PASS | No new dependencies required. |
| V. Simplicity | ✅ PASS | Reuses existing page pattern (same as bookshelf/about). One new file + one minor edit. No new plugins or structural changes. |

**Gate result**: ALL PASS — proceed to Phase 0.

## Project Structure

### Documentation (this feature)

```text
specs/001-add-training-page/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
└── tasks.md             # Phase 2 output (created by /speckit.tasks)
```

### Source Code (repository root)

```text
content/
├── pages/
│   ├── about.md           # Existing — update with training reference
│   ├── bookshelf.md       # Existing — no changes
│   └── training.md        # NEW — training page
└── images/
    └── training/          # NEW — training visuals directory
        ├── training-1.png # Placeholder names — actual images TBD
        ├── training-2.png
        └── training-3.png
```

**Structure Decision**: Follows the existing convention exactly.
New page goes in `content/pages/` (auto-added to nav by Pelican).
Images go in `content/images/training/` following the pattern used
by bookshelf images in `content/images/bookshelf/`.

## Complexity Tracking

No constitution violations. Table not applicable.
