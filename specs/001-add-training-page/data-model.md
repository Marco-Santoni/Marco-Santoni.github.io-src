# Data Model: Add Training Page

**Feature**: 001-add-training-page
**Date**: 2026-04-06

## Entities

### Training Page

A standalone static page in the Pelican site.

| Attribute       | Description                                    |
|-----------------|------------------------------------------------|
| Title           | Page title: "training"                         |
| Intro text      | 1-2 paragraphs about Marco's training activity |
| Training entries | Exactly 3 training entry blocks (see below)   |

**Storage**: Single Markdown file at `content/pages/training.md`.

### Training Entry

An inline content block within the training page. Not a separate
file — embedded directly in `training.md`.

| Attribute   | Description                                      |
|-------------|--------------------------------------------------|
| Image       | Visual for the training (stored in `content/images/training/`) |
| Title       | Name of the training course                      |
| Description | Short summary of the training content/audience   |

**Validation rules**:
- Exactly 3 entries MUST be present on the page.
- Each entry MUST have an image, title, and description.
- Images MUST be placed in `content/images/training/`.

### About Page (modified)

Existing page at `content/pages/about.md`.

| Attribute added | Description                                  |
|-----------------|----------------------------------------------|
| Training ref    | 1-2 sentences + link to `/pages/training.html` |

## Relationships

```
Training Page (1) ──contains──▶ Training Entry (3)
About Page (1) ──links to──▶ Training Page (1)
```

## State Transitions

Not applicable — all content is static.
