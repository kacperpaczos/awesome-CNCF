"""Heurystyczne generowanie use cases i alternatyw dla projektów CNCF."""

from __future__ import annotations

from typing import Any

# Szablony use cases wg subkategorii (PL)
_SUBCATEGORY_USE_CASES: dict[str, list[str]] = {
    "Automation & Configuration": [
        "Automatyzacja provisioningu infrastruktury jako kod",
        "Standaryzacja konfiguracji środowisk dev/stage/prod",
        "Compliance i audyt zmian w klastrach Kubernetes",
    ],
    "Container Runtime": [
        "Uruchamianie kontenerów OCI w Kubernetes i środowiskach edge",
        "Izolacja workloadów z niskim narzutem wydajnościowym",
        "Integracja z CRI w platformach PaaS i bare metal",
    ],
    "Container Registry": [
        "Przechowywanie i dystrybucja obrazów kontenerów w CI/CD",
        "Skanowanie podatności i podpisywanie artefaktów",
        "Replikacja multi-region dla wdrożeń globalnych",
    ],
    "Service Proxy": [
        "Zarządzanie ruchem east-west między mikrousługami",
        "mTLS, retry i circuit breaking bez zmian w kodzie aplikacji",
        "Observability L7 (metryki, trace) na poziomie mesh",
    ],
    "Scheduling & Orchestration": [
        "Orkiestracja kontenerów w skali produkcyjnej",
        "Autoscaling i self-healing workloadów",
        "Multi-tenant platformy wewnętrznego developer experience",
    ],
    "Monitoring": [
        "Zbieranie metryk z aplikacji i infrastruktury",
        "Alerty SLO/SLA i dashboardy operacyjne",
        "Korelacja sygnałów przed incydentem produkcyjnym",
    ],
    "Logging": [
        "Centralizacja logów z klastrów i aplikacji",
        "Forensics i root-cause analysis po awarii",
        "Compliance — retencja i audyt zdarzeń",
    ],
    "Tracing": [
        "Distributed tracing w architekturze mikrousług",
        "Diagnoza latency i bottlenecków między serwisami",
        "Integracja trace z metrykami i logami (observability 3-pillar)",
    ],
    "Security & Compliance": [
        "Skanowanie obrazów i runtime security w K8s",
        "Policy-as-code dla admission control",
        "CIS benchmarks i hardening klastrów",
    ],
    "Key Management": [
        "Rotacja sekretów i certyfikatów w Kubernetes",
        "Integracja z HSM / cloud KMS",
        "Sealed secrets i external secrets dla GitOps",
    ],
    "API Gateway": [
        "Ekspozycja API na zewnątrz z rate limiting i auth",
        "Wersjonowanie i routing ruchu do mikrousług",
        "Developer portal i dokumentacja API",
    ],
    "Service Mesh": [
        "Mutual TLS między serwisami bez zmian aplikacji",
        "Canary i blue-green na poziomie sieci",
        "Fine-grained traffic policies i observability",
    ],
}

_CATEGORY_USE_CASES: dict[str, list[str]] = {
    "Provisioning": [
        "Budowa i utrzymanie platformy Kubernetes / cloud native",
        "GitOps i IaC dla zespołów platform engineering",
    ],
    "Runtime": [
        "Warstwa wykonawcza kontenerów i storage/network dla podów",
        "Optymalizacja I/O i sieci pod workloady stateful",
    ],
    "Orchestration & Management": [
        "Zarządzanie cyklem życia aplikacji w klastrze",
        "Polityki, szablony i abstrakcje dla developerów",
    ],
    "Observability and Analysis": [
        "Pełny obraz zdrowia systemu produkcyjnego",
        "Proaktywne wykrywanie anomalii i capacity planning",
    ],
    "App Definition and Development": [
        "Definicja i pakowanie aplikacji cloud native",
        "Przyspieszenie developer loop (build, deploy, debug)",
    ],
    "Platform": [
        "Wewnętrzna platforma developerska (IDP) na Kubernetes",
        "Golden paths i self-service dla zespołów produktowych",
    ],
    "Serverless": [
        "Event-driven workloads bez zarządzania serwerami",
        "Skalowanie do zera i pay-per-use",
    ],
    "Wasm": [
        "Lekkie, przenośne moduły poza klasycznym kontenerem",
        "Edge, pluginy i sandboxowany kod wielojęzyczny",
    ],
    "AI Agent": [
        "Orkiestracja agentów LLM z narzędziami i pamięcią",
        "Automatyzacja workflowów z udziałem modeli AI",
    ],
    "AI Native Infra": [
        "Infrastruktura pod trening i inferencję modeli",
        "GPU scheduling i data pipelines ML",
    ],
}


def _stars(project: dict[str, Any]) -> int:
    github = project.get("github") or {}
    return int(github.get("stars") or 0)


def _maturity_rank(project: dict[str, Any]) -> int:
    order = {"graduated": 0, "incubating": 1, "sandbox": 2, "archived": 3}
    return order.get(project.get("maturity") or "", 9)


def generate_use_cases(project: dict[str, Any]) -> list[str]:
    cases: list[str] = []
    desc = (project.get("description") or "").strip()
    sub = project.get("subcategory") or ""
    cat = project.get("category") or ""
    topics = (project.get("github") or {}).get("topics") or []
    name = project.get("name") or "Projekt"
    maturity = project.get("maturity")

    if desc:
        cases.append(f"{name}: {desc.rstrip('.')}")

    for template in _SUBCATEGORY_USE_CASES.get(sub, []):
        if template not in cases:
            cases.append(template)

    for template in _CATEGORY_USE_CASES.get(cat, []):
        if template not in cases:
            cases.append(template)

    for topic in topics[:3]:
        cases.append(f"Ekosystem / tag: `{topic}` — typowe wdrożenia wokół {name}")

    if maturity == "graduated":
        cases.append(f"Produkcja enterprise — projekt CNCF Graduated ({name})")
    elif maturity == "incubating":
        cases.append(f"Wdrożenia produkcyjne z rosnącym wsparciem CNCF Incubating")
    elif maturity == "sandbox":
        cases.append(f"Eksperymenty i POC — projekt CNCF Sandbox")

    if project.get("primary_repo_url") and "kubernetes" in (desc + " ".join(topics)).lower():
        cases.append("Integracja z ekosystemem Kubernetes (CRD, operator, CNI/CSI)")

    # dedupe preserving order
    seen: set[str] = set()
    unique: list[str] = []
    for case in cases:
        key = case.lower()
        if key not in seen:
            seen.add(key)
            unique.append(case)

    return unique[:5]


def generate_alternatives(
    project: dict[str, Any],
    peers: list[dict[str, Any]],
) -> list[dict[str, str]]:
    """Zwraca listę {name, slug, note} — slug to id projektu (ścieżka Starlight)."""
    others = [p for p in peers if p["id"] != project["id"]]
    if not others:
        return []

    others.sort(
        key=lambda p: (
            _maturity_rank(p),
            -_stars(p),
            (p.get("name") or "").lower(),
        )
    )

    category_slug = project.get("category", "")
    sub = project.get("subcategory") or "ten segment"
    result: list[dict[str, str]] = []

    for alt in others[:4]:
        note_parts = [f"Ta sama subkategoria: {sub}"]
        if alt.get("maturity"):
            note_parts.append(f"CNCF {alt['maturity']}")
        if _stars(alt):
            note_parts.append(f"⭐ {_stars(alt):,}")
        result.append({
            "name": alt["name"],
            "slug": alt["id"],
            "note": " · ".join(note_parts),
        })

    return result


def openapi_placeholder(project: dict[str, Any]) -> dict[str, str | None]:
    """Ścieżki pod przyszłe submoduły OpenAPI (CI/CD — TODO)."""
    project_id = project["id"]
    repo = project.get("primary_repo_url") or ""
    return {
        "status": "todo",
        "submodule_path": f"openapi/{project_id}",
        "public_url": f"/openapi/{project_id}/",
        "repo_search": f"{repo}/tree/HEAD" if repo else None,
        "note": "Pełna specyfikacja OpenAPI — submodule + CI/CD (TODO)",
    }
