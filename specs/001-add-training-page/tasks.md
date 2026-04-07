# Tasks: Add Training Page

**Input**: Design documents from `/specs/001-add-training-page/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Exact file paths included in descriptions

---

## Phase 1: Setup

**Purpose**: Create the directory structure for training images

- [x] T001 [US1] Create directory `content/images/training/` for training visuals

**Checkpoint**: Image directory exists; ready for content creation.

---

## Phase 2: User Story 1 — Browse the Training Page (Priority: P1) 🎯 MVP

**Goal**: A new "Training" page appears in the top-level navigation, showing an intro paragraph and 3 training entries each with a visual.

**Independent Test**: Build the site (`uv run pelican content`), open the output, and verify "Training" appears in the nav menu. Click it and confirm the page shows an intro paragraph and 3 training entries, each with an image, title, and description.

### Implementation for User Story 1

- [x] T002 [P] [US1] Add 3 training images to `content/images/training/` — one image per training course. Use descriptive filenames (e.g., `data-engineering.png`). Acceptable formats: PNG, JPEG, SVG.

- [x] T003 [US1] Create `content/pages/training.md` with:
  - Pelican metadata header (`Title: training`)
  - Introductory paragraph explaining Marco's activity as a tech trainer (side project / side job)
  - 3 training entries, each containing:
    - An `<img>` tag referencing the image in `content/images/training/` (use `width="300"` for consistent sizing, following the bookshelf `<img>` pattern)
    - A heading or bold title for the training name
    - A short description of the training content and target audience
  - Use vertical layout (one entry per section, not a table grid) per research decision R3

  **Depends on**: T001, T002

- [x] T004 [US1] Build the site locally (`uv run pelican content`) and verify:
  - "Training" link appears in top-level navigation menu
  - Training page renders with intro text and 3 entries
  - All 3 images load correctly
  - Page is accessible via direct URL (`/pages/training.html`)
  - Content is readable on a narrow browser window (mobile check)

  **Depends on**: T003

**Checkpoint**: Training page is live and fully functional. US1 is independently complete and demoable.

---

## Phase 3: User Story 2 — Update the About Page (Priority: P2)

**Goal**: The about page references Marco's training activity and links to the training page.

**Independent Test**: Navigate to the about page and verify it mentions training with a working link to the training page.

### Implementation for User Story 2

- [x] T005 [US2] Edit `content/pages/about.md` to add a short paragraph (1-2 sentences) mentioning Marco's training activity as a side project/side job, with a Markdown link to the training page (e.g., `[training](/pages/training.html)` or `{filename}/pages/training.md` using Pelican's internal linking).

  **Depends on**: T003 (training page must exist to link to it)

- [x] T006 [US2] Build the site locally (`uv run pelican content`) and verify:
  - About page displays the new training reference paragraph
  - The link navigates to the training page correctly
  - Existing about page content (bio, LinkedIn badge, podcast) is unchanged

  **Depends on**: T005

**Checkpoint**: About page updated. Both US1 and US2 are complete.

---

## Phase 4: Polish & Final Verification

**Purpose**: End-to-end validation across both user stories

- [x] T007 Full site build and cross-page verification:
  - Build with `uv run pelican content`
  - Verify all navigation links (about, bookshelf, training) work from every page
  - Verify about → training link works
  - Verify no broken images across the site
  - Verify training page renders legibly at mobile-width viewport

  **Depends on**: T004, T006

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **US1 (Phase 2)**: Depends on Phase 1 (directory exists)
- **US2 (Phase 3)**: Depends on T003 (training page must exist before linking)
- **Polish (Phase 4)**: Depends on Phases 2 and 3

### Within Phases

```
T001 (create dir) ──▶ T002 (add images) ─┐
                                          ├──▶ T003 (create training.md) ──▶ T004 (verify US1)
                                          │
                                          └──▶ T005 (edit about.md) ──▶ T006 (verify US2)
                                                                              │
T004 + T006 ──────────────────────────────────────────────────────────────────▶ T007 (final check)
```

### Parallel Opportunities

- T001 and T002 can overlap (create directory, then immediately add images)
- T004 and T005 can run in parallel if T003 is done (verify US1 while editing about page)

---

## Implementation Strategy

### MVP First (US1 Only)

1. Complete Phase 1: Setup (T001)
2. Complete Phase 2: US1 (T002 → T003 → T004)
3. **STOP and VALIDATE**: Training page is independently functional
4. Deploy if ready — about page update can follow later

### Full Delivery

1. Phase 1 → Phase 2 → Phase 3 → Phase 4
2. Total: 7 tasks, estimated effort: small (content authoring + one file edit)

---

## Notes

- Marco MUST provide the actual training names, descriptions, and images for T002/T003. The plan assumes placeholder content will be replaced with real content.
- No `pelicanconf.py` changes are needed — pages auto-appear in navigation.
- No new dependencies or plugins required.
- Commit after T004 (US1 complete) and after T006 (US2 complete).
