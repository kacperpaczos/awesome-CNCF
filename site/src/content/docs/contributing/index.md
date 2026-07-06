---
title: Contributing
description: Jak aktualizować bazę wiedzy CNCF KB.
---

# Contributing

## Cykl aktualizacji

1. `python scripts/scrape.py` — pobierz dane z landscape.cncf.io
2. `python scripts/generate_docs.py` — wygeneruj `site/`
3. Edytuj strony projektów (use cases, alternatywy, OpenAPI)
4. `python scripts/generate_docs.py` — odświeża wiki **i** tabele README (`CATALOG.md`)
5. `cd site && npm run dev` — podgląd

Jednym poleceniem: `python scripts/scrape.py --docs`

## Struktura domen

| Domena | Kategorie |
|--------|-----------|
| `platform` | Provisioning, Runtime, Orchestration & Management, Platform |
| `applications` | App Definition and Development, Serverless, Wasm |
| `observability` | Observability and Analysis |
| `ai` | AI Agent, AI Native Infra, Training, Inference, Data |
| `ecosystem` | CNCF Members, Special |

Treść: `site/src/content/docs/<domena>/<kategoria>/<projekt>.md`

## Ręczna edycja

Generator **zachowuje** uzupełnione sekcje Use cases / Alternatywy / OpenAPI przy regeneracji (bez `--no-preserve`).

## OpenAPI (TODO)

Specyfikacje w `openapi/<project-id>/` jako submoduły Git, aktualizacja CI/CD.
