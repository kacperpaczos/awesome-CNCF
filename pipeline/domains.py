"""Mapowanie kategorii CNCF Landscape na domeny wiki."""

from __future__ import annotations

from pipeline.parser import category_filename

DOMAINS: dict[str, dict[str, object]] = {
    "platform": {
        "label": "Platforma i infrastruktura",
        "description": "Provisioning, runtime, orkiestracja i warstwa platformowa.",
        "categories": [
            "Provisioning",
            "Runtime",
            "Orchestration & Management",
            "Platform",
        ],
    },
    "applications": {
        "label": "Aplikacje i delivery",
        "description": "Definicja aplikacji, CI/CD, serverless i Wasm.",
        "categories": [
            "App Definition and Development",
            "Serverless",
            "Wasm",
        ],
    },
    "observability": {
        "label": "Observability",
        "description": "Monitoring, logi, tracing i analiza.",
        "categories": ["Observability and Analysis"],
    },
    "ai": {
        "label": "AI i dane",
        "description": "Agenci AI, infrastruktura ML, trening i inferencja.",
        "categories": [
            "AI Agent",
            "AI Native Infra",
            "Training",
            "Inference",
            "Data",
        ],
    },
    "ecosystem": {
        "label": "Ekosystem CNCF",
        "description": "Członkowie CNCF i kategorie specjalne.",
        "categories": ["CNCF Members", "Special"],
    },
}

_CATEGORY_TO_DOMAIN: dict[str, str] = {
    category: domain
    for domain, info in DOMAINS.items()
    for category in info["categories"]  # type: ignore[union-attr]
}


def domain_for_category(category: str) -> str:
    return _CATEGORY_TO_DOMAIN.get(category, "ecosystem")


def category_slug(category: str) -> str:
    return category_filename(category).replace(".json", "")


def doc_slug(project_id: str) -> str:
    """Bezpieczny slug pliku (np. C++ → cplusplus)."""
    return (
        project_id.replace("++", "plusplus")
        .replace("+", "plus")
        .replace("/", "-")
    )


def project_path(domain: str, category: str, project_id: str) -> str:
    return f"{domain}/{category_slug(category)}/{doc_slug(project_id)}"


def project_url(domain: str, category: str, project_id: str) -> str:
    return f"/{project_path(domain, category, project_id)}/"
