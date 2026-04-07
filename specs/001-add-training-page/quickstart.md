# Quickstart: Add Training Page

**Feature**: 001-add-training-page

## Prerequisites

- UV installed
- Repository cloned and on the `001-add-training-page` branch

## Steps

1. **Prepare training images**: Place 3 images (one per training)
   in `content/images/training/`. Use descriptive filenames
   (e.g., `data-engineering-training.png`).

2. **Create the training page**: Create `content/pages/training.md`
   with:
   - `Title: training` metadata header
   - Introductory paragraph about the training activity
   - 3 training entries, each with image, title, and description

3. **Update the about page**: Edit `content/pages/about.md` to add
   a sentence referencing the training activity with a link to the
   training page.

4. **Build and verify locally**:
   ```bash
   uv run pelican content
   ```
   Open `output/index.html` in a browser and verify:
   - "Training" appears in the top navigation menu
   - The training page shows 3 entries with images
   - The about page links to the training page

5. **Commit and deploy**: Follow the standard content workflow
   (commit, push, deployment triggers automatically).

## Verification Checklist

- [ ] Training page accessible from navigation menu
- [ ] 3 training entries visible with images
- [ ] About page references and links to training page
- [ ] All links work (navigation, about→training)
- [ ] Page renders correctly on mobile viewport
