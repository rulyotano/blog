#!/usr/bin/env python3
"""
Migrate posts from a Drupal 8/9/10 site to a Hugo content folder.

Source: Drupal's built-in JSON:API (enabled by default in Drupal 9+; in Drupal 8
        you may need to enable the `jsonapi` core module).
Target: Hugo content/posts/<slug>.md files with PaperMod-friendly front matter.

Usage
-----
    pip install -r requirements.txt
    python migrate_drupal.py \
        --base-url   https://your-drupal-site.example \
        --bundle     article \
        --out        ../content/posts \
        --static-dir ../static \
        [--user admin --password 'hunter2']      # optional, only needed for unpublished/private content

Notes
-----
* The script targets nodes of a single content type (--bundle), default "article".
  If your blog uses a different bundle name (e.g. "blog_post"), pass it.
* Body HTML is converted to Markdown via `markdownify`.
* Images referenced inside the body, plus the node's main `field_image` (if present),
  are downloaded into <static-dir>/images/<slug>/ and links rewritten.
* Tags from `field_tags` (taxonomy_term reference) become front-matter `tags`.
* `created` becomes `date`; `status: false` becomes `draft: true`.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import unicodedata
import urllib.parse
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

import requests
import yaml
from markdownify import markdownify as html_to_md
from requests.auth import HTTPBasicAuth


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
    """A boring, predictable slugifier — good enough for filenames."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    text = re.sub(r"[-\s]+", "-", text)
    return text or "untitled"


def index_included(included: list[dict]) -> dict[tuple[str, str], dict]:
    """Build a lookup of {(type, id): resource} from a JSON:API `included` array."""
    return {(r["type"], r["id"]): r for r in included or []}


def get_rel_ids(node: dict, field_name: str) -> list[tuple[str, str]]:
    """Return [(type, id), ...] for the relationship at `field_name`, if any."""
    rel = node.get("relationships", {}).get(field_name)
    if not rel:
        return []
    data = rel.get("data")
    if data is None:
        return []
    if isinstance(data, list):
        return [(d["type"], d["id"]) for d in data if d]
    return [(data["type"], data["id"])]


# ---------------------------------------------------------------------------
# Drupal client
# ---------------------------------------------------------------------------

@dataclass
class DrupalClient:
    base_url: str
    auth: HTTPBasicAuth | None = None
    session: requests.Session = field(default_factory=requests.Session)

    def get(self, path: str, params: dict | None = None) -> dict:
        url = path if path.startswith("http") else f"{self.base_url.rstrip('/')}{path}"
        r = self.session.get(
            url,
            params=params,
            auth=self.auth,
            headers={"Accept": "application/vnd.api+json"},
            timeout=30,
        )
        r.raise_for_status()
        return r.json()

    def fetch_all_nodes(self, bundle: str, page_size: int = 50) -> tuple[list[dict], list[dict]]:
        """Walk JSON:API pagination and return (nodes, included_resources)."""
        nodes: list[dict] = []
        included: list[dict] = []
        next_url: str | None = (
            f"/jsonapi/node/{bundle}"
            f"?include=field_tags,field_image"
            f"&page[limit]={page_size}"
            f"&sort=-created"
        )
        while next_url:
            payload = self.get(next_url)
            nodes.extend(payload.get("data", []))
            included.extend(payload.get("included", []))
            next_url = payload.get("links", {}).get("next", {}).get("href")
            # `next` from Drupal is an absolute URL; pass through unchanged
            if next_url and next_url.startswith(self.base_url):
                next_url = next_url[len(self.base_url):]
        return nodes, included

    def download(self, url: str, dest: Path) -> None:
        if dest.exists():
            return
        dest.parent.mkdir(parents=True, exist_ok=True)
        with self.session.get(url, auth=self.auth, stream=True, timeout=60) as r:
            r.raise_for_status()
            with open(dest, "wb") as f:
                for chunk in r.iter_content(chunk_size=64 * 1024):
                    f.write(chunk)


# ---------------------------------------------------------------------------
# Image rewriting
# ---------------------------------------------------------------------------

IMG_SRC_RE = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)


def rewrite_body_images(
    html: str,
    client: DrupalClient,
    static_dir: Path,
    slug: str,
) -> str:
    """Find <img src="..."> in the body, download each, and rewrite to a relative path."""
    matches = IMG_SRC_RE.findall(html or "")
    for src in matches:
        abs_src = src if src.startswith("http") else urllib.parse.urljoin(client.base_url + "/", src)
        filename = os.path.basename(urllib.parse.urlparse(abs_src).path) or "image"
        local_rel = f"images/{slug}/{filename}"
        local_abs = static_dir / local_rel
        try:
            client.download(abs_src, local_abs)
        except Exception as e:
            print(f"  ! failed to download {abs_src}: {e}", file=sys.stderr)
            continue
        # In Hugo, files under /static/ are served from site root.
        html = html.replace(src, f"/{local_rel}")
    return html


# ---------------------------------------------------------------------------
# Conversion
# ---------------------------------------------------------------------------

def node_to_post(
    node: dict,
    by_id: dict[tuple[str, str], dict],
    client: DrupalClient,
    static_dir: Path,
) -> tuple[str, str]:
    """Return (filename, file_contents) for a single node."""
    attrs = node.get("attributes", {})
    title = attrs.get("title") or "Untitled"
    slug = slugify(title)

    # Body
    body_html = ""
    body_field = attrs.get("body")
    if isinstance(body_field, dict):
        body_html = body_field.get("value") or body_field.get("processed") or ""

    body_html = rewrite_body_images(body_html, client, static_dir, slug)
    body_md = html_to_md(body_html, heading_style="ATX", strip=["script", "style"]) if body_html else ""

    # Tags
    tags: list[str] = []
    for t_type, t_id in get_rel_ids(node, "field_tags"):
        term = by_id.get((t_type, t_id))
        if term:
            name = term.get("attributes", {}).get("name")
            if name:
                tags.append(name)

    # Featured image — surface the URL into front matter as `cover.image` for PaperMod
    cover_image = ""
    for img_type, img_id in get_rel_ids(node, "field_image"):
        media_or_file = by_id.get((img_type, img_id))
        if not media_or_file:
            continue
        # In Drupal, field_image can point at a `file--file` directly OR a `media--image`
        # which itself wraps a file. Handle both.
        file_resource = media_or_file
        if media_or_file.get("type", "").startswith("media--"):
            for f_type, f_id in get_rel_ids(media_or_file, "field_media_image"):
                file_resource = by_id.get((f_type, f_id), file_resource)
        uri = file_resource.get("attributes", {}).get("uri", {})
        url = uri.get("url") if isinstance(uri, dict) else None
        if url:
            abs_url = url if url.startswith("http") else urllib.parse.urljoin(client.base_url + "/", url)
            filename = os.path.basename(urllib.parse.urlparse(abs_url).path)
            local_rel = f"images/{slug}/{filename}"
            try:
                client.download(abs_url, static_dir / local_rel)
                cover_image = f"/{local_rel}"
            except Exception as e:
                print(f"  ! failed to download cover image {abs_url}: {e}", file=sys.stderr)

    # Front matter
    front: dict[str, Any] = {
        "title": title,
        "date": attrs.get("created") or attrs.get("changed"),
        "draft": not attrs.get("status", True),
        "tags": tags,
    }
    summary = attrs.get("field_summary") or attrs.get("field_excerpt")
    if isinstance(summary, dict):
        summary = summary.get("value")
    if summary:
        front["summary"] = re.sub(r"<[^>]+>", "", summary).strip()
    if cover_image:
        front["cover"] = {"image": cover_image, "alt": title, "relative": False}

    fm = yaml.safe_dump(front, sort_keys=False, allow_unicode=True).strip()
    contents = f"---\n{fm}\n---\n\n{body_md.strip()}\n"
    return f"{slug}.md", contents


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main() -> int:
    p = argparse.ArgumentParser(description="Migrate Drupal posts to Hugo Markdown.")
    p.add_argument("--base-url", required=True, help="e.g. https://your-drupal-site.example")
    p.add_argument("--bundle", default="article", help="Drupal content type (default: article)")
    p.add_argument("--out", required=True, help="Hugo content/posts directory to write into")
    p.add_argument("--static-dir", required=True, help="Hugo static/ directory for downloaded images")
    p.add_argument("--user", help="Optional Drupal username (for unpublished content)")
    p.add_argument("--password", help="Optional Drupal password")
    p.add_argument("--dry-run", action="store_true", help="Print what would happen, write nothing")
    p.add_argument("--from-file", help="Skip the network — read a saved JSON:API response from a file")
    args = p.parse_args()

    out = Path(args.out).resolve()
    static_dir = Path(args.static_dir).resolve()
    if not args.dry_run:
        out.mkdir(parents=True, exist_ok=True)
        static_dir.mkdir(parents=True, exist_ok=True)

    auth = HTTPBasicAuth(args.user, args.password) if args.user else None
    client = DrupalClient(base_url=args.base_url.rstrip("/"), auth=auth)

    if args.from_file:
        with open(args.from_file, "r", encoding="utf-8") as f:
            payload = json.load(f)
        nodes = payload.get("data", [])
        included = payload.get("included", [])
    else:
        print(f"-> Fetching nodes of bundle '{args.bundle}' from {args.base_url} ...")
        t0 = time.time()
        nodes, included = client.fetch_all_nodes(args.bundle)
        print(f"   got {len(nodes)} nodes in {time.time() - t0:.1f}s")

    by_id = index_included(included)

    written = 0
    for node in nodes:
        try:
            filename, contents = node_to_post(node, by_id, client, static_dir)
        except Exception as e:
            nid = node.get("id", "<unknown>")
            print(f"  ! failed to convert node {nid}: {e}", file=sys.stderr)
            continue
        target = out / filename
        if args.dry_run:
            print(f"   [dry-run] would write {target} ({len(contents)} bytes)")
        else:
            target.write_text(contents, encoding="utf-8")
            print(f"   wrote {target}")
        written += 1

    print(f"-> Done. {written} post(s) processed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
