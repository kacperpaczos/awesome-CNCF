"""Pobieranie danych CNCF Landscape przez HTTP (requests)."""

from __future__ import annotations

import json
from typing import Any

import requests

from pipeline.config import (
    FULL_DATA_URL,
    GUIDE_DATA_URL,
    REQUEST_TIMEOUT,
    USER_AGENT,
)


def _session() -> requests.Session:
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
        }
    )
    return session


def fetch_json(url: str, session: requests.Session | None = None) -> Any:
    sess = session or _session()
    response = sess.get(url, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.json()


def fetch_landscape_payload(session: requests.Session | None = None) -> dict[str, Any]:
    return fetch_json(FULL_DATA_URL, session)


def fetch_guide_payload(session: requests.Session | None = None) -> dict[str, Any]:
    return fetch_json(GUIDE_DATA_URL, session)


def save_raw_payload(payload: dict[str, Any], path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
