"""Normalizacja i grupowanie danych landscape."""

from __future__ import annotations

import re
from collections import defaultdict
from datetime import datetime, timezone
from typing import Any


def _slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^\w\s-]", "", value)
    value = re.sub(r"[\s_-]+", "-", value)
    return value.strip("-")


def _primary_repo_url(item: dict[str, Any]) -> str | None:
    repositories = item.get("repositories") or []
    for repo in repositories:
        if repo.get("primary") and repo.get("url"):
            return repo["url"]
    if repositories:
        return repositories[0].get("url")
    return None


def normalize_item(
    item: dict[str, Any],
    github_data: dict[str, Any],
    crunchbase_data: dict[str, Any],
) -> dict[str, Any]:
    repo_url = _primary_repo_url(item)
    github_info = github_data.get(repo_url) if repo_url else None
    crunchbase_info = crunchbase_data.get(item.get("crunchbase_url"))

    description = item.get("description")
    if not description and github_info:
        description = github_info.get("description")

    logo_path = item.get("logo")
    logo_url = f"https://landscape.cncf.io/{logo_path}" if logo_path else None

    return {
        "id": item.get("id"),
        "name": item.get("name"),
        "description": description,
        "category": item.get("category"),
        "subcategory": item.get("subcategory"),
        "maturity": item.get("maturity"),
        "homepage_url": item.get("homepage_url") or item.get("website"),
        "logo": logo_path,
        "logo_url": logo_url,
        "repositories": item.get("repositories") or [],
        "primary_repo_url": repo_url,
        "oss": item.get("oss"),
        "twitter_url": item.get("twitter_url"),
        "crunchbase_url": item.get("crunchbase_url"),
        "accepted_at": item.get("accepted_at"),
        "graduated_at": item.get("graduated_at"),
        "incubating_at": item.get("incubating_at"),
        "archived_at": item.get("archived_at"),
        "latest_annual_review_at": item.get("latest_annual_review_at"),
        "latest_annual_review_url": item.get("latest_annual_review_url"),
        "devstats_url": item.get("devstats_url"),
        "artwork_url": item.get("artwork_url"),
        "blog_url": item.get("blog_url"),
        "slack_url": item.get("slack_url"),
        "chat_channel": item.get("chat_channel"),
        "clomonitor_name": item.get("clomonitor_name"),
        "lfx_slug": item.get("lfx_slug"),
        "extra": item.get("extra"),
        "github": github_info,
        "crunchbase": crunchbase_info,
        # Pola na przyszłą knowledge base — uzupełnisz ręcznie / w kolejnych etapach
        "alternatives": [],
        "use_cases": [],
        "openapi": None,
    }


def build_projects(
    payload: dict[str, Any],
) -> list[dict[str, Any]]:
    github_data = payload.get("github_data") or {}
    crunchbase_data = payload.get("crunchbase_data") or {}
    items = payload.get("items") or []
    return [
        normalize_item(item, github_data, crunchbase_data)
        for item in items
    ]


def group_by_category(projects: list[dict[str, Any]]) -> dict[str, dict[str, list[dict[str, Any]]]]:
    grouped: dict[str, dict[str, list[dict[str, Any]]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for project in projects:
        category = project.get("category") or "Unknown"
        subcategory = project.get("subcategory") or "General"
        grouped[category][subcategory].append(project)
    return {
        category: dict(subcategories)
        for category, subcategories in sorted(grouped.items())
    }


def group_by_maturity(projects: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for project in projects:
        maturity = project.get("maturity") or "none"
        grouped[maturity].append(project)
    return {key: grouped[key] for key in sorted(grouped)}


def build_metadata(projects: list[dict[str, Any]], source_url: str) -> dict[str, Any]:
    maturity_counts: dict[str, int] = defaultdict(int)
    category_counts: dict[str, int] = defaultdict(int)
    for project in projects:
        maturity_counts[project.get("maturity") or "none"] += 1
        category_counts[project.get("category") or "Unknown"] += 1

    return {
        "scraped_at": datetime.now(timezone.utc).isoformat(),
        "source_url": source_url,
        "total_projects": len(projects),
        "with_description": sum(1 for p in projects if p.get("description")),
        "with_maturity": sum(1 for p in projects if p.get("maturity")),
        "with_logo": sum(1 for p in projects if p.get("logo")),
        "maturity_counts": dict(sorted(maturity_counts.items())),
        "category_counts": dict(sorted(category_counts.items(), key=lambda x: (-x[1], x[0]))),
    }


def category_filename(category: str) -> str:
    return f"{_slugify(category)}.json"


def maturity_filename(maturity: str) -> str:
    return f"{_slugify(maturity)}.json"
