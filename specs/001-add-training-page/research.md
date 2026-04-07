# Research: Add Training Page

**Feature**: 001-add-training-page
**Date**: 2026-04-06

## Research Questions

### R1: How do Pelican pages appear in the navigation menu?

- **Decision**: Pages placed in `content/pages/` with a `Title:`
  metadata header are automatically added to the site navigation.
  No configuration change to `pelicanconf.py` is required.
- **Rationale**: The existing `about.md` and `bookshelf.md` pages
  follow this pattern and appear in the menu without explicit
  `MENUITEMS` or `DISPLAY_PAGES_ON_MENU` configuration. Pelican's
  default behavior is to include all pages in the navigation.
- **Alternatives considered**: Explicitly adding the page via
  `MENUITEMS` in `pelicanconf.py` — rejected because it would
  deviate from the existing convention used by other pages.

### R2: How to add visuals to each training entry?

- **Decision**: Use inline HTML `<img>` tags within Markdown,
  following the exact pattern used on the bookshelf page. Images
  are stored in `content/images/training/` and referenced via
  relative paths.
- **Rationale**: The bookshelf page already uses this pattern
  successfully (e.g., `<img src="../images/bookshelf/deep_work.jpg"
  width="200" />`). Reusing it ensures visual consistency and
  avoids introducing new dependencies.
- **Alternatives considered**:
  - Standard Markdown image syntax (`![alt](path)`) — rejected
    because it does not allow width control, and the bookshelf
    precedent uses HTML for consistent sizing.
  - CSS-based image cards — rejected as it would require theme
    customization, violating the Simplicity principle.

### R3: Layout structure for 3 training entries

- **Decision**: Use a vertical list layout where each training
  has an image followed by title and description. This is simpler
  and more readable than the 2-column table grid used by bookshelf.
- **Rationale**: With only 3 entries (vs. 20+ books), a vertical
  layout gives each training more visual space and allows for
  longer descriptions. The bookshelf uses a compact grid because
  it lists many items with minimal text.
- **Alternatives considered**:
  - 2-column Markdown table (bookshelf style) — viable but
    constrains description length and wastes the second column
    with only 3 items.
  - Horizontal card layout — rejected as it requires CSS changes.

### R4: How to link from the about page to the training page?

- **Decision**: Add a short paragraph to `about.md` mentioning
  the training activity, with a standard Markdown link to the
  training page using Pelican's page URL pattern.
- **Rationale**: Minimal change, consistent with how the about
  page already links to external resources (podcast link).
- **Alternatives considered**: None — this is straightforward.

## Unresolved Items

None. All research questions are resolved.
