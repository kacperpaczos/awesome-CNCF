"""Wspólny katalog tabel (README + strona wiki) — jedno źródło: data/landscape.json + wiki."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from pipeline.config import DATA_DIR, PROJECT_ROOT, SITE_DIR
from pipeline.domains import DOMAINS, category_slug, doc_slug, domain_for_category, project_url
from pipeline.enrichment import generate_use_cases, openapi_placeholder

DOCS_DIR = SITE_DIR / "src" / "content" / "docs"
LANDSCAPE_PATH = DATA_DIR / "landscape.json"
README_PATH = PROJECT_ROOT / "README.md"
CATALOG_MD_PATH = PROJECT_ROOT / "CATALOG.md"
README_MARKER_START = "<!-- cncf-kb:catalog:start -->"
README_MARKER_END = "<!-- cncf-kb:catalog:end -->"


def _wiki_page_path(domain: str, category: str, project_id: str) -> Path:
    return DOCS_DIR / domain / category_slug(category) / f"{doc_slug(project_id)}.md"


def _extract_bullets(markdown: str, heading: str) -> list[str]:
    if heading not in markdown:
        return []
    start = markdown.find(heading) + len(heading)
    end = len(markdown)
    for marker in ("\n## ", "\n### ", "\n---"):
        pos = markdown.find(marker, start)
        if pos != -1:
            end = min(end, pos)
    block = markdown[start:end]
    items: list[str] = []
    for line in block.splitlines():
        line = line.strip()
        if line.startswith("- ") and not line.startswith("- _"):
            text = line[2:].strip()
            if text and "Do uzupełnienia" not in text and "wygenerowana heurystycznie" not in text:
                items.append(text)
    return items


def _extract_openapi_link(markdown: str) -> str | None:
    if "## OpenAPI" not in markdown:
        return None
    block = markdown.split("## OpenAPI", 1)[1].split("\n## ", 1)[0]
    match = re.search(r"\[([^\]]+)\]\(([^)]+)\)", block)
    if match and "todo" not in match.group(2).lower():
        return match.group(2)
    match = re.search(r"Docelowy URL \| \[([^\]]+)\]\(([^)]+)\)", block)
    if match:
        return match.group(2)
    return None


def project_row_fields(
    project: dict[str, Any],
    *,
    read_wiki: bool = True,
    for_starlight: bool = False,
) -> dict[str, str]:
    category = project.get("category") or ""
    domain = domain_for_category(category)
    wiki_path = _wiki_page_path(domain, category, project["id"])

    use_cases = generate_use_cases(project)
    openapi = openapi_placeholder(project)
    openapi_href = openapi["public_url"] or "—"

    if read_wiki and wiki_path.exists():
        wiki_md = wiki_path.read_text(encoding="utf-8")
        wiki_cases = _extract_bullets(wiki_md, "## Use cases")
        if wiki_cases:
            use_cases = wiki_cases
        wiki_openapi = _extract_openapi_link(wiki_md)
        if wiki_openapi:
            openapi_href = wiki_openapi

    logo_file = ""
    if project.get("logo"):
        logo_name = Path(project["logo"]).name
        logo_file = f"/logos/{logo_name}" if for_starlight else f"site/public/logos/{logo_name}"

    docs_url = project.get("homepage_url") or ""
    wiki_rel = (
        f"site/src/content/docs/{domain}/{category_slug(category)}/{doc_slug(project['id'])}.md"
    )
    wiki_site_url = project_url(domain, category, project["id"])

    use_cases_cell = " · ".join(use_cases[:3])
    if len(use_cases) > 3:
        use_cases_cell += " …"

    maturity = project.get("maturity")
    name = project.get("name") or project["id"]
    if maturity:
        name = f"{name} `{maturity}`"

    return {
        "icon": logo_file,
        "name": name,
        "use_cases": use_cases_cell or "—",
        "docs": docs_url,
        "openapi": openapi_href,
        "wiki_rel": wiki_rel,
        "wiki_site": wiki_site_url,
    }


def _cell(text: str) -> str:
    return text.replace("|", "/").replace("\n", " ").strip()


def _render_table_rows(
    projects: list[dict[str, Any]], *, read_wiki: bool, for_starlight: bool
) -> list[str]:
    rows: list[str] = []
    for project in sorted(projects, key=lambda p: (p.get("name") or "").lower()):
        f = project_row_fields(project, read_wiki=read_wiki, for_starlight=for_starlight)
        icon = (
            f'<img src="{f["icon"]}" width="32" alt="">'
            if f["icon"]
            else "—"
        )
        docs = f'[docs]({f["docs"]})' if f["docs"] else "—"
        openapi = f'[OpenAPI]({f["openapi"]})' if f["openapi"] != "—" else "TODO"
        if for_starlight:
            name_link = f'**[{_cell(project["name"])}]({f["wiki_site"]})**'
        else:
            name_link = f'**[{_cell(project["name"])}]({f["wiki_rel"]})**'
        rows.append(
            f"| {icon} | {name_link} | {_cell(f['use_cases'])} | {docs} | {openapi} |"
        )
    return rows


def render_catalog_markdown(
    projects: list[dict[str, Any]],
    metadata: dict[str, Any],
    *,
    read_wiki: bool = True,
    for_starlight: bool = False,
) -> str:
    by_category: dict[str, list[dict[str, Any]]] = {}
    for project in projects:
        cat = project.get("category") or "Unknown"
        by_category.setdefault(cat, []).append(project)

    lines = [
        f"**Ostatnia aktualizacja:** `{metadata.get('scraped_at', '—')}`  ",
        f"**Projektów:** {metadata.get('total_projects', len(projects))}  ",
        "",
        "Kolumny zsynchronizowane z [wiki Starlight](site/) — ten sam pipeline `generate_docs.py`.",
        "",
    ]

    if for_starlight:
        lines[2] = "Katalog wygenerowany z `data/landscape.json` — zsynchronizowany z README."

    for domain_id, info in DOMAINS.items():
        domain_categories = info["categories"]  # type: ignore[assignment]
        present = [c for c in domain_categories if c in by_category]
        if not present:
            continue

        lines.append(f"## {info['label']}")
        lines.append("")

        for category in present:
            items = by_category[category]
            cat_slug = category_slug(category)
            lines.append(f"### {category}")
            lines.append("")
            if for_starlight:
                lines.append(f"[Przegląd wiki](/{domain_id}/{cat_slug}/) · {len(items)} projektów")
                lines.append("")
            else:
                lines.append(
                    f"Wiki: `site/src/content/docs/{domain_id}/{cat_slug}/` · {len(items)} projektów"
                )
                lines.append("")
            lines.append("| | Narzędzie | Use cases | Dokumentacja | OpenAPI |")
            lines.append("|--:|-----------|-----------|--------------|---------|")
            lines.extend(_render_table_rows(items, read_wiki=read_wiki, for_starlight=for_starlight))
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def update_readme(catalog_body: str) -> None:
    header = (
        "## Katalog projektów\n\n"
        "Pełna tabela (ikona, use cases, docs, OpenAPI) — auto-generowana.  \n"
        "Szczegóły: [strona katalogu w wiki](site/src/content/docs/catalog/index.md).\n\n"
    )
    block = f"{README_MARKER_START}\n{header}{catalog_body}{README_MARKER_END}"

    if README_PATH.exists():
        text = README_PATH.read_text(encoding="utf-8")
        if README_MARKER_START in text and README_MARKER_END in text:
            pre = text[: text.index(README_MARKER_START)]
            post = text[text.index(README_MARKER_END) + len(README_MARKER_END) :]
            README_PATH.write_text(pre + block + post, encoding="utf-8")
            return

    README_PATH.write_text(
        README_PATH.read_text(encoding="utf-8").rstrip() + "\n\n" + block + "\n",
        encoding="utf-8",
    )


def write_catalog_files(
    projects: list[dict[str, Any]],
    metadata: dict[str, Any],
    *,
    read_wiki: bool = True,
) -> None:
    body = render_catalog_markdown(projects, metadata, read_wiki=read_wiki, for_starlight=False)
    update_readme(body)
    CATALOG_MD_PATH.write_text(
        "# CNCF Landscape — katalog\n\n" + body,
        encoding="utf-8",
    )

    catalog_dir = DOCS_DIR / "catalog"
    catalog_dir.mkdir(parents=True, exist_ok=True)
    starlight_body = render_catalog_markdown(
        projects, metadata, read_wiki=read_wiki, for_starlight=True
    )
    (catalog_dir / "index.md").write_text(
        f"""---
title: Katalog
description: Tabela wszystkich projektów — zsynchronizowana z README.
template: doc
---

# Katalog projektów

{starlight_body}
""",
        encoding="utf-8",
    )


def generate_catalog(*, read_wiki: bool = True) -> dict[str, int]:
    with LANDSCAPE_PATH.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    projects = payload["projects"]
    metadata = payload["metadata"]
    write_catalog_files(projects, metadata, read_wiki=read_wiki)
    return {"projects": len(projects)}
