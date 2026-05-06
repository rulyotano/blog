---
title: "Hello, Hugo"
date: 2026-04-28T09:00:00-05:00
draft: false
tags: ["meta"]
summary: "First post on the new Hugo + PaperMod setup."
---

This blog now runs on **Hugo** with the **PaperMod** theme. Posts are plain
Markdown files committed to git — no database, no admin panel.

## Why I switched

Drupal was overkill for what is essentially a list of articles. With Hugo:

- Posts are `.md` files I can edit in any text editor.
- The site builds in milliseconds and deploys as static HTML.
- Versioning, drafts, and rollbacks are just `git`.

## Code blocks work out of the box

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

```bash
# Create a new post
hugo new content posts/my-post.md
```

That's it. Real posts go in `content/posts/`.
