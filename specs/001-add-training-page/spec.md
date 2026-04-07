# Feature Specification: Add Training Page

**Feature Branch**: `001-add-training-page`
**Created**: 2026-04-05
**Status**: Draft
**Input**: User description: "add a new section at the root level of the menu. This new section is called 'training'. I explain there my activity as tech trainer as side project or as side job. In that page, I list the 3 trainings I have lectured. Each should have some visual to make it more appealing. Update the 'about' page accordingly to reference the new 'training' page"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Browse the Training Page (Priority: P1)

As a visitor, I want to find a "Training" page in the site's
top-level navigation so that I can learn about Marco's activity
as a tech trainer and see the trainings he has delivered.

**Why this priority**: The training page is the core deliverable
of this feature. Without it, nothing else makes sense.

**Independent Test**: Can be fully tested by navigating to the
site, clicking "Training" in the menu, and verifying the page
displays an introductory description of the training activity
plus 3 training entries, each with a visual element.

**Acceptance Scenarios**:

1. **Given** the site is built and deployed,
   **When** a visitor opens the site,
   **Then** a "Training" link appears in the top-level navigation
   menu alongside the existing pages (about, bookshelf).

2. **Given** a visitor clicks on "Training" in the menu,
   **When** the training page loads,
   **Then** they see an introductory paragraph explaining Marco's
   activity as a tech trainer (side project / side job), followed
   by a list of exactly 3 trainings.

3. **Given** the training page is displayed,
   **When** a visitor scrolls through the 3 trainings,
   **Then** each training entry includes a visual element (image
   or graphic) that makes the listing visually appealing, along
   with a description of the training.

---

### User Story 2 - Update the About Page (Priority: P2)

As a visitor reading the about page, I want to see a reference
to Marco's training activity so that I can discover the training
page and learn more.

**Why this priority**: This is a cross-linking update that depends
on the training page existing first (US1). It improves
discoverability but is not the core deliverable.

**Independent Test**: Can be tested by navigating to the about
page and verifying it contains a mention of the training activity
with a link to the training page.

**Acceptance Scenarios**:

1. **Given** a visitor is reading the about page,
   **When** they look at the page content,
   **Then** they see a mention of Marco's training activity with a
   clickable link that navigates to the training page.

2. **Given** a visitor clicks the training link on the about page,
   **When** the link is followed,
   **Then** they arrive at the training page.

---

### Edge Cases

- What happens if a visitor accesses the training page URL directly
  (not via menu)? It MUST render correctly as a standalone page.
- What happens if images for a training entry fail to load? The
  page MUST still display the training text content legibly.
- What happens on small screens? The training entries with visuals
  MUST remain readable (no horizontal overflow that hides content).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The site MUST include a new "Training" page accessible
  from the top-level navigation menu.
- **FR-002**: The training page MUST contain an introductory section
  explaining Marco's activity as a tech trainer (side project /
  side job).
- **FR-003**: The training page MUST list exactly 3 training courses
  that Marco has lectured.
- **FR-004**: Each training entry MUST include a visual element
  (image or graphic) to make it visually appealing.
- **FR-005**: Each training entry MUST include a text description
  of the training (title and summary at minimum).
- **FR-006**: The about page MUST be updated to reference the
  training activity and link to the training page.
- **FR-007**: The training page MUST be a static page (not a blog
  post) consistent with existing pages (about, bookshelf).

### Key Entities

- **Training Entry**: A training course Marco has delivered.
  Attributes: title, description/summary, visual (image).
  Exactly 3 entries on the page.
- **Training Page**: A standalone static page containing the intro
  text and the 3 training entries. Appears in the site navigation.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The "Training" link is visible in the top-level
  navigation on every page of the site.
- **SC-002**: The training page displays all 3 trainings, each
  with a visual and descriptive text, in under 3 seconds on a
  standard connection.
- **SC-003**: A visitor can navigate from the about page to the
  training page in one click.
- **SC-004**: The training page content is fully readable on both
  desktop and mobile viewports.

## Assumptions

- Marco will provide the specific names, descriptions, and images
  for the 3 trainings during implementation (the spec does not
  prescribe the actual training content).
- The visual style for training entries follows the same approach
  used on the bookshelf page (inline images in Markdown), unless
  a different approach is chosen during implementation.
- The training page is authored as a single Markdown file in the
  pages directory, consistent with the existing about and bookshelf
  pages.
- The about page update is a minor text addition (1-2 sentences
  with a link), not a redesign of the page.
- No new navigation mechanism is needed — the page appears in the
  menu automatically by being a page, consistent with how about
  and bookshelf pages already work.
