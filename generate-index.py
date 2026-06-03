#!/usr/bin/env python3
"""
generate-index.py

Sucht rekursiv nach article.json-Dateien und erzeugt:
- index.html
- search.json

Zusätzlich:
- Liest optional site-config.json
- Rendert daraus auf der Startseite einen Footer mit Blogs, Social Links und Rechtlichem
"""

from __future__ import annotations

import argparse
import html
import json
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any


SITE_TITLE = "Benjamin Lam – Veröffentlichungsarchiv"
SITE_DESCRIPTION = (
    "Archivierte Veröffentlichungen von Benjamin Lam: Artikel, Posts und Essays "
    "aus LinkedIn, Medium, dev.to, eigenen Blogs und weiteren Quellen."
)
SITE_URL = "https://benjamin-lam.github.io/"
CSS_PATH = "/assets/css/archive.css"

SOURCE_LABELS = {
    "linkedin": "LinkedIn",
    "medium": "Medium",
    "devto": "dev.to",
    "blog": "Blog",
    "heise": "Heise",
    "other": "Weitere Veröffentlichungen",
}

SOURCE_ORDER = ["linkedin", "medium", "devto", "blog", "heise", "other"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generiert index.html und search.json für das Veröffentlichungsarchiv."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Root-Verzeichnis des GitHub-Pages-Repositories. Standard: aktuelles Verzeichnis.",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="Optionale site-config.json. Standard: {root}/site-config.json",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any] | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as exc:
        print(f"[WARN] Ungültiges JSON: {path} ({exc})")
        return None
    except OSError as exc:
        print(f"[WARN] Konnte Datei nicht lesen: {path} ({exc})")
        return None


def load_site_config(root: Path, config_path: Path | None) -> dict[str, Any]:
    path = config_path or (root / "site-config.json")
    data = load_json(path)
    if not data:
        return {}
    return data


def is_article_json(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)

    ignored_parts = {
        ".git",
        "assets",
        "local-raw",
        "raw-archive",
        "archive",
        "failed",
        "processing",
        "inbox",
        "node_modules",
        "__pycache__",
    }

    return not any(part in ignored_parts for part in rel.parts)


def format_date_de(value: str) -> str:
    try:
        year, month, day = value.split("-")
        return f"{day}.{month}.{year}"
    except Exception:
        return value


def normalize_article(data: dict[str, Any], article_json_path: Path, root: Path) -> dict[str, Any] | None:
    required = ["title", "source_slug", "first_published", "path"]
    missing = [key for key in required if not data.get(key)]

    if missing:
        print(f"[WARN] Übersprungen wegen fehlender Felder {missing}: {article_json_path}")
        return None

    article_path = str(data.get("path", "")).strip()

    if not article_path.startswith("/"):
        article_path = "/" + article_path

    if not article_path.endswith("/"):
        article_path += "/"

    canonical_url = data.get("canonical_url") or f"{SITE_URL.rstrip('/')}{article_path}"

    tags = data.get("tags", [])
    if not isinstance(tags, list):
        tags = []

    title = str(data.get("title", "")).strip()
    source_slug = str(data.get("source_slug", "")).strip().lower()
    source = str(data.get("source") or SOURCE_LABELS.get(source_slug, source_slug)).strip()
    first_published = str(data.get("first_published", "")).strip()
    archived_at = str(data.get("archived_at", "")).strip()
    status = str(data.get("status", "aktuell")).strip()
    description = str(data.get("description") or "").strip()

    if not description:
        description = (
            f"Archivierte Veröffentlichung von Benjamin Lam. "
            f"Erstveröffentlicht am {format_date_de(first_published)} auf {source}."
        )

    return {
        "title": title,
        "slug": str(data.get("slug", "")).strip(),
        "source": source,
        "source_slug": source_slug,
        "source_url": str(data.get("source_url", "")).strip(),
        "first_published": first_published,
        "archived_at": archived_at,
        "status": status,
        "tags": [str(tag).strip() for tag in tags if str(tag).strip()],
        "path": article_path,
        "canonical_url": canonical_url,
        "description": description,
        "_article_json": str(article_json_path.relative_to(root)),
    }


def find_articles(root: Path) -> list[dict[str, Any]]:
    articles: list[dict[str, Any]] = []

    for path in sorted(root.rglob("article.json")):
        if not is_article_json(path, root):
            continue

        data = load_json(path)
        if not data:
            continue

        article = normalize_article(data, path, root)
        if article:
            articles.append(article)

    articles.sort(
        key=lambda item: (
            item.get("first_published", ""),
            item.get("title", "").lower(),
        ),
        reverse=True,
    )

    return articles


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def render_tag_list(tags: list[str]) -> str:
    if not tags:
        return ""
    return ", ".join(esc(tag) for tag in tags)


def render_article_item(article: dict[str, Any]) -> str:
    title = esc(article["title"])
    url = esc(article["path"])
    source = esc(article["source"])
    date_label = esc(format_date_de(article["first_published"]))
    status = esc(article["status"])
    tags = render_tag_list(article["tags"])
    description = esc(article["description"])
    data_tags = esc(" ".join(article["tags"]).lower())

    meta_parts = [source, date_label, f"Status: {status}"]
    if tags:
        meta_parts.append(f"Tags: {tags}")

    meta = " · ".join(meta_parts)

    return f"""      <li class="archive-item" data-source="{esc(article["source_slug"])}" data-tags="{data_tags}" data-status="{status.lower()}">
        <a href="{url}">{title}</a>
        <span class="meta">{meta}</span>
        <p class="summary">{description}</p>
      </li>"""


def render_source_section(source_slug: str, articles: list[dict[str, Any]]) -> str:
    if not articles:
        return ""

    source_label = SOURCE_LABELS.get(source_slug, articles[0].get("source", source_slug))
    items = "\n".join(render_article_item(article) for article in articles)

    return f"""    <section class="archive-section" id="{esc(source_slug)}">
      <h2>{esc(source_label)}</h2>
      <ul class="article-list">
{items}
      </ul>
    </section>"""


def render_footer(config: dict[str, Any]) -> str:
    footer = config.get("footer", {})
    if not isinstance(footer, dict):
        return ""

    intro = str(footer.get("intro", "")).strip()
    sections = footer.get("sections", [])

    if not intro and not sections:
        return ""

    section_html = []

    if isinstance(sections, list):
        for section in sections:
            if not isinstance(section, dict):
                continue

            title = str(section.get("title", "")).strip()
            links = section.get("links", [])

            if not title and not links:
                continue

            link_items = []

            if isinstance(links, list):
                for link in links:
                    if not isinstance(link, dict):
                        continue

                    label = str(link.get("label", "")).strip()
                    url = str(link.get("url", "")).strip()

                    if not label or not url:
                        continue

                    link_items.append(
                        f'          <li><a href="{esc(url)}" rel="me noopener">{esc(label)}</a></li>'
                    )

            links_html = "\n".join(link_items)

            section_html.append(f"""      <section class="archive-footer-section">
        <h2>{esc(title)}</h2>
        <ul class="archive-footer-list">
{links_html}
        </ul>
      </section>""")

    intro_html = f'      <p class="archive-footer-intro">{esc(intro)}</p>\n' if intro else ""
    sections_html = "\n".join(section_html)

    return f"""    <footer class="archive-footer">
{intro_html}      <div class="archive-footer-grid">
{sections_html}
      </div>
    </footer>"""


def build_index_html(articles: list[dict[str, Any]], config: dict[str, Any]) -> str:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for article in articles:
        grouped[article["source_slug"]].append(article)

    known_sections = [
        render_source_section(source_slug, grouped[source_slug])
        for source_slug in SOURCE_ORDER
        if grouped.get(source_slug)
    ]

    unknown_source_slugs = sorted(
        source_slug for source_slug in grouped.keys() if source_slug not in SOURCE_ORDER
    )

    unknown_sections = [
        render_source_section(source_slug, grouped[source_slug])
        for source_slug in unknown_source_slugs
    ]

    sections = "\n\n".join(section for section in known_sections + unknown_sections if section)

    source_options = "\n".join(
        f'        <option value="{esc(source_slug)}">{esc(SOURCE_LABELS.get(source_slug, source_slug))}</option>'
        for source_slug in SOURCE_ORDER
        if grouped.get(source_slug)
    )

    footer = render_footer(config)

    today = date.today().isoformat()
    article_count_label = "archivierte Veröffentlichung" if len(articles) == 1 else "archivierte Veröffentlichungen"

    return f"""<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>{esc(SITE_TITLE)}</title>
  <meta name="description" content="{esc(SITE_DESCRIPTION)}">
  <link rel="canonical" href="{esc(SITE_URL)}">

  <meta name="author" content="Benjamin Lam">
  <meta name="robots" content="index,follow">

  <meta property="og:type" content="website">
  <meta property="og:title" content="{esc(SITE_TITLE)}">
  <meta property="og:description" content="{esc(SITE_DESCRIPTION)}">
  <meta property="og:url" content="{esc(SITE_URL)}">
  <meta property="og:site_name" content="{esc(SITE_TITLE)}">

  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{esc(SITE_TITLE)}">
  <meta name="twitter:description" content="{esc(SITE_DESCRIPTION)}">

  <link rel="stylesheet" href="{esc(CSS_PATH)}">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    "name": "{esc(SITE_TITLE)}",
    "description": "{esc(SITE_DESCRIPTION)}",
    "url": "{esc(SITE_URL)}",
    "dateModified": "{today}",
    "author": {{
      "@type": "Person",
      "name": "Benjamin Lam",
      "url": "{esc(SITE_URL)}"
    }}
  }}
  </script>
</head>
<body>
  <main class="page archive-page">
    <header class="site-header">
      <h1 class="site-title">Veröffentlichungsarchiv</h1>
      <p class="site-description">{esc(SITE_DESCRIPTION)}</p>
      <p class="archive-meta">{len(articles)} {article_count_label}</p>
    </header>

    <section class="archive-controls" aria-label="Archiv filtern">
      <label>
        Suche
        <input type="search" id="archive-search" placeholder="Titel, Beschreibung oder Tag suchen">
      </label>

      <label>
        Veröffentlichungsort
        <select id="archive-source">
          <option value="">Alle Quellen</option>
{source_options}
        </select>
      </label>
    </section>

{sections}

    <p id="archive-empty" class="visually-muted" hidden>Keine passenden Veröffentlichungen gefunden.</p>

{footer}
  </main>

  <script>
    const searchInput = document.getElementById('archive-search');
    const sourceSelect = document.getElementById('archive-source');
    const items = Array.from(document.querySelectorAll('.archive-item'));
    const emptyState = document.getElementById('archive-empty');

    function normalize(value) {{
      return (value || '').toLowerCase().trim();
    }}

    function applyFilters() {{
      const query = normalize(searchInput.value);
      const source = normalize(sourceSelect.value);
      let visibleCount = 0;

      for (const item of items) {{
        const text = normalize(item.textContent);
        const itemSource = normalize(item.dataset.source);
        const matchesQuery = !query || text.includes(query);
        const matchesSource = !source || itemSource === source;
        const visible = matchesQuery && matchesSource;

        item.hidden = !visible;

        if (visible) {{
          visibleCount++;
        }}
      }}

      emptyState.hidden = visibleCount !== 0;
    }}

    searchInput.addEventListener('input', applyFilters);
    sourceSelect.addEventListener('change', applyFilters);
  </script>
</body>
</html>
"""


def build_search_json(articles: list[dict[str, Any]]) -> str:
    public_articles = []
    for article in articles:
        public_articles.append({
            "title": article["title"],
            "source": article["source"],
            "source_slug": article["source_slug"],
            "first_published": article["first_published"],
            "status": article["status"],
            "tags": article["tags"],
            "path": article["path"],
            "canonical_url": article["canonical_url"],
            "description": article["description"],
        })

    return json.dumps(public_articles, ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    args = parse_args()
    root = args.root.expanduser().resolve()

    if not root.exists():
        print(f"[ERROR] Root-Verzeichnis existiert nicht: {root}")
        return 1

    config_path = args.config.expanduser().resolve() if args.config else None
    config = load_site_config(root, config_path)

    articles = find_articles(root)

    index_path = root / "index.html"
    search_path = root / "search.json"

    index_path.write_text(build_index_html(articles, config), encoding="utf-8")
    search_path.write_text(build_search_json(articles), encoding="utf-8")

    print(f"[OK] {len(articles)} Artikel gefunden.")
    print(f"[OK] Geschrieben: {index_path}")
    print(f"[OK] Geschrieben: {search_path}")

    if config:
        print("[OK] site-config.json geladen.")
    else:
        print("[INFO] Keine site-config.json gefunden oder Datei leer/ungültig.")

    if not articles:
        print("[WARN] Keine article.json-Dateien gefunden.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())