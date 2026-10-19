# AGENTS.md

Shared context for AI coding tools (Claude Code, Copilot, Cursor, Codex, etc.).
Single source of truth — tool-specific files (e.g. `CLAUDE.md`) should point here.

## Project overview

This project is a Blog made using Hugo/Go tech.
Has the following sections:
- Blog
  - Articles written by me
- Books
  - Books I've read

## Commands

All commands run through Docker (Docker daemon must be running). See `Makefile` / `docker-compose.yml`.

- `make dev` — dev server with drafts at http://localhost:1313 (same as `docker compose up hugo`)
- `make build` — production build into `./public` (`--minify`)
- `make shell` — shell inside the Hugo container

## Content conventions

### Locations
- Blog articles: `content/blog/<slug>.md`
- Books: `content/books/<slug>.md`
- Images: `static/images/<slug>/<file>` (folder named after the post's file slug), referenced as `/images/<slug>/<file>`

### Front matter — Book
```yaml
---
title: 'Book Title'
date: 'YYYY-MM-DDTHH:MM:SS+00:00'
draft: false
tags:
- Books
url: /books/<short-slug>
cover:
  image: /images/<slug>/<cover-file>.jpg
  alt: 'Book Title'
  relative: true
---
```

### Front matter — Blog article
```yaml
---
title: Article Title
date: 'YYYY-MM-DDTHH:MM:SS+00:00'
draft: false
author: Raul
tags:
- Blog
- <Topic>
url: /blog/article/<slug>
cover:
  image: /images/<slug>/cover.png
  alt: Short description of the cover
---
```

### Gotchas
- `hugo.toml` has `buildFuture = false`: posts dated in the future are not published. Use today's date or earlier.
- Dates are quoted ISO-8601 strings with `+00:00` offset.

## Writing style

### For Books
- Write a short but meaningful summary
- Then write each section summary. If there are too many chapters, take the main ones, and just mention the rest.
- Try to find and download a book image.
- Add links to the book (publisher page, Amazon, official site if any), placed at the top, before the summary.

### Researching books
- O'Reilly, many retailers and Google Books API often block automated fetching; fall back to other listings.
- Cover image by ISBN-10 from Amazon works well: `https://images-na.ssl-images-amazon.com/images/P/<ISBN10>.01.L.jpg`. Verify the image is the right edition before using it.
- Don't invent chapter details that can't be verified. Keep unverified parts general and tell the user what needs checking.

## Theme & layouts

- Theme: PaperMod, loaded as a Hugo module (`hugo.toml` → `[module.imports]`).
- Local overrides in `layouts/partials/` (currently `extend_head.html`). Prefer overriding via partials over editing theme files.

## Do / Don't

- Don't edit `public/` or `resources/` — they are build output (git-ignored).
- Don't commit without asking.
