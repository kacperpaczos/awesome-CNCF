#!/usr/bin/env python3
"""Generuje dokumentację Starlight z data/landscape.json."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from pipeline.config import SITE_DIR
from pipeline.catalog import generate_catalog
from pipeline.starlight import generate_starlight

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generuj dokumentację Starlight")
    parser.add_argument("--no-preserve", action="store_true")
    parser.add_argument("--no-logos", action="store_true")
    args = parser.parse_args()

    stats = generate_starlight(
        preserve_manual=not args.no_preserve,
        download_images=not args.no_logos,
    )
    catalog = generate_catalog(read_wiki=True)
    logger.info(
        "Gotowe: %d domen, %d kategorii, %d projektów, %d logo, katalog: %d wierszy",
        stats["domains"],
        stats["categories"],
        stats["projects"],
        stats["logos"],
        catalog["projects"],
    )
    logger.info("Treść: %s", (SITE_DIR / "src/content/docs").resolve())
    logger.info("Podgląd: cd site && npm run dev")
    return 0


if __name__ == "__main__":
    sys.exit(main())
