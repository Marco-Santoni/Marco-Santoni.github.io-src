<!--
  Sync Impact Report
  ===========================
  Version change: (new) → 1.0.0
  Modified principles: N/A (initial ratification)
  Added sections:
    - Core Principles (5 principles)
    - Technology Constraints
    - Content Workflow
    - Governance
  Removed sections: N/A
  Templates requiring updates:
    - .specify/templates/plan-template.md — ✅ no changes needed
      (Constitution Check section is dynamic)
    - .specify/templates/spec-template.md — ✅ no changes needed
    - .specify/templates/tasks-template.md — ✅ no changes needed
  Follow-up TODOs: none
-->

# Marco Santoni Blog Constitution

## Core Principles

### I. Static-First

All site output MUST be pre-rendered static HTML, CSS, and
JavaScript. No server-side processing, no runtime databases, and
no external CMS integrations are permitted. Every page MUST be
servable from a plain file host (e.g., GitHub Pages) with zero
backend dependencies.

### II. Markdown Content

All content files MUST be authored in Markdown (`.md`). No other
authoring format (reStructuredText, HTML-only pages, Jupyter
notebooks as source) is permitted for published content. Metadata
MUST use Pelican's Markdown metadata header format.

### III. Pelican Pipeline

Pelican is the sole static-site generator. The build pipeline
MUST rely exclusively on Pelican and its plugin ecosystem for
content processing, templating, and output generation. Introducing
an additional or replacement generator requires a constitution
amendment.

### IV. UV Dependency Management

All Python dependencies MUST be managed via UV. The `pyproject.toml`
and `uv.lock` files are the single source of truth for the
dependency graph. Direct `pip install` usage is not permitted for
project dependencies.

### V. Simplicity

Keep the site minimal. New features, plugins, or structural changes
MUST demonstrate clear value before adoption. Prefer fewer moving
parts over richer tooling. YAGNI applies: do not add capabilities
until they are actually needed.

## Technology Constraints

- **Language**: Python (version specified in `pyproject.toml`)
- **Generator**: Pelican
- **Package manager**: UV
- **Content format**: Markdown (`.md`)
- **Storage**: Filesystem only — no database, no headless CMS
- **Hosting**: Static file hosting (GitHub Pages)
- **Source control**: Git, with `master` as the main branch

## Content Workflow

1. Author new content as a Markdown file under `content/`.
2. Use Pelican metadata headers (`Title`, `Date`, `Category`,
   `Tags`, etc.) at the top of each file.
3. Build locally with `make` or Pelican CLI to verify rendering.
4. Commit and push to trigger deployment.

All content changes MUST be reviewable as plain-text diffs in Git.

## Governance

- This constitution supersedes ad-hoc decisions when conflicts
  arise.
- Amendments MUST be documented with a version bump, rationale,
  and updated date.
- Versioning follows semantic versioning:
  - **MAJOR**: Principle removal or backward-incompatible
    redefinition.
  - **MINOR**: New principle or materially expanded guidance.
  - **PATCH**: Clarifications, wording, or typo fixes.
- Compliance is verified during plan and spec reviews via the
  Constitution Check gate.

**Version**: 1.0.0 | **Ratified**: 2026-04-05 | **Last Amended**: 2026-04-05
