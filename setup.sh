#!/usr/bin/env bash
# One-shot setup for the Hugo blog: install PaperMod and start the dev server.
# Run from the project root (the directory containing hugo.toml).

set -euo pipefail

# 1. Make sure Hugo is installed.
if ! command -v hugo >/dev/null 2>&1; then
  echo "Hugo not found. Install it first:"
  echo "  macOS:   brew install hugo"
  echo "  Linux:   https://gohugo.io/installation/linux/"
  exit 1
fi

# 2. Initialize git if this isn't a repo yet (PaperMod is added as a submodule).
if [ ! -d .git ]; then
  git init -q
fi

# 3. Add PaperMod as a submodule (idempotent).
if [ ! -d themes/PaperMod ]; then
  echo "-> Adding PaperMod theme as a git submodule..."
  git submodule add --depth=1 https://github.com/adityatelange/hugo-PaperMod themes/PaperMod
  git submodule update --init --recursive
else
  echo "-> PaperMod already present, skipping clone."
fi

# 4. Start the dev server with drafts visible.
echo "-> Starting Hugo dev server at http://localhost:1313 (Ctrl+C to stop)"
hugo server -D
