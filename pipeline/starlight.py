"""Generowanie treści Starlight (Astro) z danych CNCF Landscape — struktura domenowa."""

from __future__ import annotations

import json
import logging
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import requests

from pipeline.config import DATA_DIR, REQUEST_TIMEOUT, SITE_DIR, USER_AGENT
from pipeline.domains import (
    DOMAINS,
    category_slug,
    doc_slug,
    domain_for_category,
    project_url,
)
from pipeline.enrichment import generate_alternatives, generate_use_cases, openapi_placeholder
from pipeline.guide import load_guide_intros
from pipeline.parser import category_filename

logger = logging.getLogger(__name__)

DOCS_DIR = SITE_DIR / "src" / "content" / "docs"
PUBLIC_LOGOS = SITE_DIR / "public" / "logos"
LANDSCAPE_PATH = DATA_DIR / "landscape.json"
SIDEBAR_MODULE = SITE_DIR / "starlight.sidebar.mjs"
KEEP_DOC_ENTRIES = {"contributing", "index.mdx"}


def logo_public_path(project: dict[str, Any]) -> str | None:
    if not project.get("logo"):
        return None
    return f"/logos/{Path(project['logo']).name}"


def maturity_badge(maturity: str | None) -> str | None:
    if not maturity:
        return None
    return {
        "graduated": "success",
        "incubating": "caution",
        "sandbox": "note",
        "archived": "danger",
    }.get(maturity, "default")


def _download_logo(project: dict[str, Any], dest: Path, session: requests.Session) -> bool:
    logo_url = project.get("logo_url")
    if not logo_url or not project.get("logo"):
        return False
    path = dest / Path(project["logo"]).name
    if path.exists():
        return True
    try:
        response = session.get(logo_url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        path.write_bytes(response.content)
        return True
    except Exception:  # noqa: BLE001
        return False


def download_logos(projects: list[dict[str, Any]], workers: int = 16) -> dict[str, int]:
    PUBLIC_LOGOS.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers["User-Agent"] = USER_AGENT
    stats = {"ok": 0, "fail": 0}

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {
            pool.submit(_download_logo, p, PUBLIC_LOGOS, session): p
            for p in projects
            if p.get("logo_url")
        }
        for future in as_completed(futures):
            project = futures[future]
            if (PUBLIC_LOGOS / Path(project["logo"]).name).exists():
                stats["ok"] += 1
            else:
                stats["fail"] += 1
    return stats


def yaml_quote(value: str | None, limit: int = 200) -> str:
    if not value:
        return '""'
    text = value.replace("\n", " ").replace('"', "'").strip()
    if len(text) > limit:
        text = text[: limit - 1] + "…"
    return json.dumps(text, ensure_ascii=False)


def render_project_page(
    project: dict[str, Any],
    domain: str,
    cat_slug: str,
    use_cases: list[str],
    alternatives: list[dict[str, str]],
    openapi: dict[str, str | None],
) -> str:
    logo = logo_public_path(project)
    logo_md = f"![{project['name']}]({logo})\n\n" if logo else ""
    maturity = project.get("maturity")
    category = project.get("category") or ""
    badge_yaml = ""
    if maturity:
        badge_yaml = f"""
sidebar:
  badge:
    text: {maturity.capitalize()}
    variant: {maturity_badge(maturity)}"""

    use_cases_md = "\n".join(f"- {c}" for c in use_cases)
    alts_md = "\n".join(
        f"- [{a['name']}]({a['url']}) — {a['note']}"
        for a in alternatives
    ) or "- _Brak bliskich alternatyw w tej subkategorii — uzupełnij ręcznie._"

    github = project.get("github") or {}
    github_lines = []
    if github.get("stars") is not None:
        github_lines.append(f"- Gwiazdki GitHub: **{github['stars']:,}**")
    if github.get("license"):
        github_lines.append(f"- Licencja: **{github['license']}**")
    if github.get("topics"):
        github_lines.append("- Tematy: " + ", ".join(f"`{t}`" for t in github["topics"]))

    repos_md = "\n".join(
        f"- [{repo['url'].rstrip('/').split('/')[-1]}]({repo['url']})"
        for repo in project.get("repositories") or []
        if repo.get("url")
    ) or "- _Brak publicznego repozytorium_"

    links = [
        ("Strona główna", project.get("homepage_url")),
        ("DevStats CNCF", project.get("devstats_url")),
        ("Blog", project.get("blog_url")),
        ("Slack", project.get("slack_url")),
        ("Artwork", project.get("artwork_url")),
        ("Annual review", project.get("latest_annual_review_url")),
    ]
    links_md = "\n".join(f"- [{label}]({url})" for label, url in links if url) or "- _—_"
    desc = project.get("description") or "_Brak opisu w landscape._"

    return f"""---
title: {project['name']}
description: {yaml_quote(project.get('description'))}
domain: {json.dumps(domain)}
category: {json.dumps(category)}
subcategory: {json.dumps(project.get('subcategory'))}
project_id: {json.dumps(project['id'])}
maturity: {json.dumps(maturity)}
openapi_status: todo{badge_yaml}
---

# {project['name']}

{logo_md}**Domena:** [{DOMAINS[domain]['label']}](../index.md) · **Kategoria:** [{category}](index.md) · {project.get('subcategory')}  
**Open source:** {'tak' if project.get('oss') else 'nie' if project.get('oss') is False else '—'}

## Opis

{desc}

## Use cases

{use_cases_md}

_Sekcja wygenerowana heurystycznie — popraw według własnego doświadczenia._

## Alternatywy

{alts_md}

## Dokumentacja

{links_md}

### Repozytoria

{repos_md}

## OpenAPI

> **TODO:** Pełna specyfikacja w submodule `{openapi['submodule_path']}` — aktualizacja przez CI/CD.

| | |
|---|---|
| Status | `{openapi['status']}` |
| Docelowy URL | [{openapi['public_url']}]({openapi['public_url']}) |
| Submodule | `{openapi['submodule_path']}` |
| Szukaj w repo | {f"[źródło]({openapi['repo_search']})" if openapi.get('repo_search') else '—'} |

## Metadane CNCF

| Pole | Wartość |
|------|---------|
| Accepted | {project.get('accepted_at') or '—'} |
| Graduated | {project.get('graduated_at') or '—'} |
| Incubating | {project.get('incubating_at') or '—'} |
| Archived | {project.get('archived_at') or '—'} |
| CLOMonitor | {project.get('clomonitor_name') or '—'} |

## GitHub

{chr(10).join(github_lines) if github_lines else '_Brak danych GitHub_'}
"""


def render_category_index(
    category: str,
    domain: str,
    cat_slug: str,
    subcategories: dict[str, list[dict[str, Any]]],
    intro: str | None,
) -> str:
    total = sum(len(v) for v in subcategories.values())
    cncf = sum(1 for items in subcategories.values() for p in items if p.get("maturity"))
    intro_block = f"{intro}\n\n" if intro else ""
    sections: list[str] = []

    for subcategory, projects in sorted(subcategories.items()):
        rows: list[str] = []
        for p in sorted(projects, key=lambda x: x["name"].lower()):
            logo = logo_public_path(p)
            img = f'<img src="{logo}" alt="" width="40" height="40" />' if logo else "—"
            mat = f"`{p['maturity']}`" if p.get("maturity") else "—"
            desc = (p.get("description") or "—").replace("|", "/").replace("\n", " ")
            if len(desc) > 90:
                desc = desc[:87] + "…"
            link = project_url(domain, category, p["id"])
            rows.append(f"| {img} | [{p['name']}]({link}) | {desc} | {mat} |")
        sections.append(
            f"### {subcategory}\n\n*{len(projects)} projektów*\n\n"
            f"| Logo | Projekt | Opis | CNCF |\n|------|---------|------|------|\n"
            + "\n".join(rows)
        )

    return f"""---
title: {category}
description: Przegląd {total} projektów — {category} (CNCF Landscape).
template: doc
---

# {category}

{intro_block}**{total}** projektów · **{cncf}** w programie CNCF

[Domena: {DOMAINS[domain]['label']}](../index.md)

{chr(10).join(sections)}
"""


def render_domain_index(
    domain_id: str,
    by_category: dict[str, dict[str, list[dict[str, Any]]]],
) -> str:
    info = DOMAINS[domain_id]
    categories = info["categories"]  # type: ignore[assignment]
    rows: list[str] = []
    total = 0
    cncf = 0

    for category in categories:
        if category not in by_category:
            continue
        subs = by_category[category]
        cat_total = sum(len(v) for v in subs.values())
        cat_cncf = sum(1 for items in subs.values() for p in items if p.get("maturity"))
        total += cat_total
        cncf += cat_cncf
        slug = category_slug(category)
        rows.append(
            f"| [{category}]({slug}/) | {cat_total} | {cat_cncf} |"
        )

    return f"""---
title: {info['label']}
description: {info['description']}
template: doc
---

# {info['label']}

{info['description']}

**{total}** projektów · **{cncf}** CNCF

| Kategoria | Projektów | CNCF |
|-----------|-----------|------|
{chr(10).join(rows)}
"""


def render_home_index(
    by_category: dict[str, dict[str, list[dict[str, Any]]]],
    metadata: dict[str, Any],
) -> str:
    maturity = metadata.get("maturity_counts", {})
    domain_sections: list[str] = []

    for domain_id, info in DOMAINS.items():
        cards: list[str] = []
        for category in info["categories"]:  # type: ignore[union-attr]
            if category not in by_category:
                continue
            subs = by_category[category]
            slug = category_slug(category)
            total = sum(len(v) for v in subs.values())
            cncf = sum(1 for items in subs.values() for p in items if p.get("maturity"))
            cards.append(
                f'  <Card title="{category}" icon="document">\n'
                f"    **{total}** projektów"
                + (f" · **{cncf}** CNCF" if cncf else "")
                + f"\n\n    [Przegląd](/{domain_id}/{slug}/)\n"
                f"  </Card>"
            )
        if cards:
            domain_sections.append(
                f"### {info['label']}\n\n"
                f"{info['description']}\n\n"
                f"[Przegląd domeny](/{domain_id}/)\n\n"
                f"<CardGrid>\n{chr(10).join(cards)}\n</CardGrid>"
            )

    return f"""---
title: CNCF Cloud Native Knowledge Base
description: Baza wiedzy CNCF Landscape — domeny, use cases, alternatywy, OpenAPI.
template: splash
hero:
  tagline: Spójne spojrzenie na narzędzia cloud native
  actions:
    - text: Przeglądaj domeny
      link: "#domeny"
      icon: right-arrow
    - text: CNCF Landscape
      link: https://landscape.cncf.io
      icon: external
      variant: minimal
---

import {{ Card, CardGrid }} from '@astrojs/starlight/components';

Wiki o **{metadata.get('total_projects')}** projektach z [CNCF Landscape](https://landscape.cncf.io).
Ostatnia synchronizacja: `{metadata.get('scraped_at')}`.

| Maturity | Liczba |
|----------|--------|
| Graduated | {maturity.get('graduated', 0)} |
| Incubating | {maturity.get('incubating', 0)} |
| Sandbox | {maturity.get('sandbox', 0)} |
| Archived | {maturity.get('archived', 0)} |

<h2 id="domeny">Domeny</h2>

{chr(10).join(domain_sections)}
"""


def write_sidebar_module(active_categories: set[str]) -> None:
    lines = [
        "/** Auto-generated by scripts/generate_docs.py */",
        "export const sidebar = [",
        "  { label: 'Start', link: '/' },",
        "  { label: 'Katalog', link: '/catalog/' },",
        "  {",
        "    label: 'Contributing',",
        "    collapsed: true,",
        "    items: [{ autogenerate: { directory: 'contributing' } }],",
        "  },",
    ]
    for domain_id, info in DOMAINS.items():
        cat_dirs = [
            f"{domain_id}/{category_slug(c)}"
            for c in info["categories"]  # type: ignore[union-attr]
            if c in active_categories
        ]
        if not cat_dirs:
            continue
        lines.append("  {")
        lines.append(f"    label: {json.dumps(info['label'])},")
        lines.append("    collapsed: true,")
        lines.append("    items: [")
        for path in cat_dirs:
            lines.append(f"      {{ autogenerate: {{ directory: {json.dumps(path)} }} }},")
        lines.append("    ],")
        lines.append("  },")
    lines.append("];")
    lines.append("")
    SIDEBAR_MODULE.write_text("\n".join(lines), encoding="utf-8")


def merge_sections(existing: str, generated: str, headings: tuple[str, ...]) -> str:
    for heading in headings:
        if heading not in existing:
            continue
        start = existing.find(heading)
        nxt = len(existing)
        for marker in ("\n## ", "\n### "):
            pos = existing.find(marker, start + len(heading))
            if pos != -1:
                nxt = min(nxt, pos)
        preserved = existing[start:nxt]
        if "_wygenerowana heurystycznie" in preserved and "popraw według" not in preserved:
            continue
        if "_Do uzupełnienia" in preserved:
            continue
        gen_start = generated.find(heading)
        if gen_start == -1:
            continue
        gen_nxt = len(generated)
        for marker in ("\n## ", "\n### "):
            pos = generated.find(marker, gen_start + len(heading))
            if pos != -1:
                gen_nxt = min(gen_nxt, pos)
        generated = generated[:gen_start] + preserved + generated[gen_nxt:]
    return generated


def _clean_generated_docs() -> None:
    for child in list(DOCS_DIR.iterdir()):
        if child.name in KEEP_DOC_ENTRIES:
            continue
        if child.is_dir():
            shutil.rmtree(child)
        elif child.suffix in (".md", ".mdx") and child.name != "index.mdx":
            child.unlink()


def _alternatives_with_urls(
    project: dict[str, Any],
    peers: list[dict[str, Any]],
) -> list[dict[str, str]]:
    category = project.get("category") or ""
    domain = domain_for_category(category)
    alts = generate_alternatives(project, peers)
    for alt in alts:
        alt_project = next((p for p in peers if p["id"] == alt["slug"]), None)
        if alt_project:
            alt["url"] = project_url(domain, category, alt_project["id"])
        else:
            alt["url"] = project_url(domain, category, alt["slug"])
    return alts


def generate_starlight(
    *,
    landscape_path: Path = LANDSCAPE_PATH,
    preserve_manual: bool = False,
    download_images: bool = True,
) -> dict[str, int]:
    with landscape_path.open(encoding="utf-8") as handle:
        payload = json.load(handle)

    projects = payload["projects"]
    metadata = payload["metadata"]
    guide_intros = load_guide_intros()

    by_category: dict[str, dict[str, list[dict[str, Any]]]] = {}
    for project in projects:
        cat = project.get("category") or "Unknown"
        sub = project.get("subcategory") or "General"
        by_category.setdefault(cat, {}).setdefault(sub, []).append(project)

    stats = {"domains": 0, "categories": 0, "projects": 0, "logos": 0, "preserved": 0}

    if download_images:
        logo_stats = download_logos(projects)
        stats["logos"] = logo_stats["ok"]
        logger.info("Logo: %d OK, %d brak", logo_stats["ok"], logo_stats["fail"])

    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    _clean_generated_docs()

    (DOCS_DIR / "index.mdx").write_text(
        render_home_index(by_category, metadata),
        encoding="utf-8",
    )
    write_sidebar_module(set(by_category.keys()))

    for domain_id in DOMAINS:
        domain_dir = DOCS_DIR / domain_id
        domain_dir.mkdir(parents=True, exist_ok=True)
        (domain_dir / "index.md").write_text(
            render_domain_index(domain_id, by_category),
            encoding="utf-8",
        )
        stats["domains"] += 1

    for category, subcategories in sorted(by_category.items()):
        domain = domain_for_category(category)
        cat_slug = category_slug(category)
        category_dir = DOCS_DIR / domain / cat_slug
        category_dir.mkdir(parents=True, exist_ok=True)

        (category_dir / "index.md").write_text(
            render_category_index(
                category, domain, cat_slug, subcategories, guide_intros.get(category)
            ),
            encoding="utf-8",
        )
        stats["categories"] += 1

        for sub_projects in subcategories.values():
            for project in sub_projects:
                use_cases = generate_use_cases(project)
                alternatives = _alternatives_with_urls(project, sub_projects)
                openapi = openapi_placeholder(project)
                content = render_project_page(
                    project, domain, cat_slug, use_cases, alternatives, openapi
                )
                path = category_dir / f"{doc_slug(project['id'])}.md"
                if preserve_manual and path.exists():
                    old = path.read_text(encoding="utf-8")
                    merged = merge_sections(
                        old, content, ("## Use cases", "## Alternatywy", "## OpenAPI")
                    )
                    if merged != content:
                        stats["preserved"] += 1
                    content = merged
                path.write_text(content, encoding="utf-8")
                stats["projects"] += 1

    openapi_root = SITE_DIR / "public" / "openapi"
    openapi_root.mkdir(parents=True, exist_ok=True)
    (openapi_root / "README.md").write_text(
        "# OpenAPI (TODO)\n\nSpecyfikacje — git submodules + CI/CD.\n",
        encoding="utf-8",
    )
    return stats
