# Convenience wrapper around docker compose so common workflows are short.
#
#   make init        # one-time: clone PaperMod theme into ./themes/PaperMod
#   make dev         # run hugo dev server (http://localhost:1313)
#   make build       # static build into ./public
#   make new SLUG=my-post-title
#   make migrate URL=https://yoursite BUNDLE=article [DUSER=admin DPASS=hunter2]
#   make shell       # interactive shell inside the Hugo container
#   make clean       # remove ./public and ./resources

DC ?= docker compose
PAPERMOD_REPO ?= https://github.com/adityatelange/hugo-PaperMod

.PHONY: init dev build new migrate shell clean help

help:
	@awk 'BEGIN{FS=":.*##"; printf "\nTargets:\n"} /^[a-zA-Z_-]+:.*##/ {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

init: ## Clone PaperMod theme on first run (idempotent)
	@if [ ! -d themes/PaperMod ]; then \
		echo "-> Cloning PaperMod into themes/PaperMod"; \
		$(DC) run --rm hugo sh -c "git clone --depth=1 $(PAPERMOD_REPO) themes/PaperMod"; \
	else \
		echo "-> themes/PaperMod already present, skipping."; \
	fi

dev: init ## Run the Hugo dev server with drafts (http://localhost:1313)
	$(DC) up hugo

build: init ## Build the static site into ./public
	$(DC) run --rm hugo --minify

new: ## Create a new post: make new SLUG=my-post-title
	@if [ -z "$(SLUG)" ]; then echo "Usage: make new SLUG=my-post-title"; exit 1; fi
	$(DC) run --rm hugo new content/posts/$(SLUG).md

migrate: ## Pull posts from Drupal: make migrate URL=https://site BUNDLE=article [DUSER=... DPASS=...]
	@if [ -z "$(URL)" ]; then echo "Usage: make migrate URL=https://site [BUNDLE=article] [DUSER=... DPASS=...]"; exit 1; fi
	$(DC) --profile tools run --rm migrate \
		--base-url $(URL) \
		--bundle $(or $(BUNDLE),article) \
		--out ../content/posts \
		--static-dir ../static \
		$(if $(DUSER),--user $(DUSER)) \
		$(if $(DPASS),--password $(DPASS))

shell: ## Open a shell inside the Hugo container
	$(DC) run --rm --entrypoint sh hugo

clean: ## Remove build artifacts
	rm -rf public resources .hugo_build.lock
