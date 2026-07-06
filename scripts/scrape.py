#!/usr/bin/env python3
"""Pobiera dane z CNCF Landscape → data/landscape.json."""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from pipeline.client import fetch_guide_payload, fetch_landscape_payload, save_raw_payload
from pipeline.config import CACHE_DIR, DATA_DIR, FULL_DATA_URL, LOGOS_DIR
from pipeline.parser import build_metadata, build_projects
from pipeline.playwright_client import (
    download_logos_with_playwright,
    fetch_landscape_via_playwright,
    validate_landscape_page,
)
from pipeline.catalog import generate_catalog
from pipeline.starlight import generate_starlight

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("scrape")


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)


def save_outputs(payload: dict, projects: list[dict]) -> dict:
    metadata = build_metadata(projects, FULL_DATA_URL)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    save_raw_payload(payload, CACHE_DIR / "full.json")

    try:
        guide = fetch_guide_payload()
        write_json(CACHE_DIR / "guide.json", guide)
    except Exception as exc:  # noqa: BLE001
        logger.warning("guide.json: %s", exc)

    write_json(DATA_DIR / "landscape.json", {"metadata": metadata, "projects": projects})
    write_json(DATA_DIR / "metadata.json", metadata)
    return metadata


def fetch_payload(use_playwright: bool) -> dict:
    if use_playwright:
        return fetch_landscape_via_playwright()
    try:
        return fetch_landscape_payload()
    except Exception as exc:  # noqa: BLE001
        logger.warning("requests failed (%s), trying Playwright...", exc)
        return fetch_landscape_via_playwright()


def main() -> int:
    parser = argparse.ArgumentParser(description="Scrape CNCF Landscape")
    parser.add_argument("--use-playwright-fetch", action="store_true")
    parser.add_argument("--validate-playwright", action="store_true")
    parser.add_argument("--download-logos", action="store_true")
    parser.add_argument("--only-cncf", action="store_true")
    parser.add_argument("--logo-limit", type=int, default=None)
    parser.add_argument("--docs", action="store_true", help="Wygeneruj site/ po scrapingu")
    args = parser.parse_args()

    logger.info("Pobieranie: %s", FULL_DATA_URL)
    payload = fetch_payload(args.use_playwright_fetch)
    projects = build_projects(payload)
    metadata = save_outputs(payload, projects)
    logger.info("Zapisano %d projektów", metadata["total_projects"])

    if args.validate_playwright:
        validation = validate_landscape_page(metadata["total_projects"])
        write_json(CACHE_DIR / "validation.json", validation)
        logger.info("Walidacja: %s", validation)

    if args.download_logos:
        stats = download_logos_with_playwright(
            projects, LOGOS_DIR, only_cncf=args.only_cncf, limit=args.logo_limit
        )
        logger.info("Logo: %s", stats)

    if args.docs:
        logger.info("Generowanie dokumentacji Starlight + katalog...")
        generate_starlight()
        generate_catalog(read_wiki=True)

    return 0


if __name__ == "__main__":
    sys.exit(main())
