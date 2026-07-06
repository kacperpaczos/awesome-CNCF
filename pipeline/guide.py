"""Treści wprowadzające z CNCF Landscape guide.json."""

from __future__ import annotations

import json
import re
from html import unescape
from pathlib import Path
from typing import Any

from pipeline.config import CACHE_DIR, DATA_DIR

GUIDE_PATH = CACHE_DIR / "guide.json"


def strip_html(html: str) -> str:
    text = re.sub(r"<br\s*/?>", "\n", html, flags=re.IGNORECASE)
    text = re.sub(r"</p>", "\n\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<li>", "- ", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    text = unescape(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def load_guide_intros() -> dict[str, str]:
    if not GUIDE_PATH.exists():
        return {}
    with GUIDE_PATH.open(encoding="utf-8") as handle:
        guide: dict[str, Any] = json.load(handle)
    return {
        entry["category"]: strip_html(entry.get("content", ""))
        for entry in guide.get("categories", [])
        if entry.get("category")
    }
