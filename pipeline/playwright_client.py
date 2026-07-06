"""Walidacja strony i pobieranie zasobów przez Playwright."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

from playwright.sync_api import sync_playwright

from pipeline.config import FULL_DATA_URL, LANDSCAPE_PAGE_URL

logger = logging.getLogger(__name__)

_CHROMIUM_CANDIDATES = (
    {"channel": "chromium"},
    {"channel": "chrome"},
    {"executable_path": "/usr/bin/chromium-browser"},
    {"executable_path": "/snap/bin/chromium"},
)


def _launch_browser(playwright):
    last_error: Exception | None = None
    for options in _CHROMIUM_CANDIDATES:
        try:
            return playwright.chromium.launch(headless=True, **options)
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            logger.debug("Chromium launch failed (%s): %s", options, exc)
    raise RuntimeError(
        "Nie udało się uruchomić Chromium. Zainstaluj: playwright install chromium "
        "lub systemowy pakiet chromium-browser."
    ) from last_error


def fetch_landscape_via_playwright() -> dict[str, Any]:
    """Pobiera full.json w kontekście przeglądarki (fallback gdy requests zawiedzie)."""
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        try:
            context = browser.new_context()
            response = context.request.get(FULL_DATA_URL)
            if not response.ok:
                raise RuntimeError(
                    f"Playwright request failed: {response.status} {response.status_text}"
                )
            return response.json()
        finally:
            browser.close()


def validate_landscape_page(expected_count: int) -> dict[str, Any]:
    """Ładuje stronę landscape i porównuje liczbę kart z danymi API."""
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        try:
            page = browser.new_page()
            captured: dict[str, Any] = {}

            def on_response(response) -> None:
                if response.url.endswith("/data/full.json") and response.ok:
                    try:
                        captured["payload"] = response.json()
                    except Exception as exc:  # noqa: BLE001
                        logger.warning("Nie udało się sparsować full.json: %s", exc)

            page.on("response", on_response)
            page.goto(LANDSCAPE_PAGE_URL, wait_until="networkidle", timeout=120_000)

            cards = page.locator("[data-testid='card'], .card, article").count()
            api_count = len((captured.get("payload") or {}).get("items", []))

            return {
                "page_loaded": True,
                "cards_in_dom": cards,
                "items_from_network": api_count,
                "expected_count": expected_count,
                "counts_match": api_count == expected_count if api_count else None,
            }
        finally:
            browser.close()


def download_logos_with_playwright(
    projects: list[dict[str, Any]],
    logos_dir: Path,
    *,
    only_cncf: bool = False,
    limit: int | None = None,
) -> dict[str, int]:
    """Pobiera pliki logo; Playwright lepiej radzi sobie z SPA i redirectami."""
    logos_dir.mkdir(parents=True, exist_ok=True)
    stats = {"downloaded": 0, "skipped": 0, "failed": 0}

    targets = [
        project
        for project in projects
        if project.get("logo_url") and (not only_cncf or project.get("maturity"))
    ]
    if limit is not None:
        targets = targets[:limit]

    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        try:
            context = browser.new_context()
            for project in targets:
                logo_path = project["logo"]
                destination = logos_dir / Path(logo_path).name
                if destination.exists():
                    stats["skipped"] += 1
                    continue
                try:
                    response = context.request.get(project["logo_url"])
                    if not response.ok:
                        stats["failed"] += 1
                        continue
                    destination.write_bytes(response.body())
                    stats["downloaded"] += 1
                except Exception:  # noqa: BLE001
                    stats["failed"] += 1
        finally:
            browser.close()

    return stats
