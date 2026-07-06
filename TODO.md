# TODO — CNCF Autonomous Knowledge Base

> To repozytorium jest **indeksem**: katalogiem projektów CNCF Landscape z linkami, metadanymi i wskazaniami do submodułów. Kod, dokumentacja i specyfikacje API żyją w **osobnych folderach w root** — nie wewnątrz siebie nawzajem.

## Cel

Zbudować autonomiczną bazę wiedzy o ~2409 projektach cloud native:
- indeks (to repo) — wiki, katalog, linki, metadane
- `projects/` — submoduły do oficjalnych repozytoriów (kod źródłowy)
- `openapis/` — osobny folder na specyfikacje OpenAPI per projekt
- `documentations/` — osobny folder na dokumentację projektów (submoduły / kopie / linki lokalne)

## Struktura folderów (root)

```
/
├── projects/          # submoduły Git → oficjalne repo (kod)
│   └── <project-id>/
├── openapis/          # specyfikacje OpenAPI (osobny folder, nie w projects/)
│   └── <project-id>/
│       └── openapi.yaml   # wygenerowany lub skopiowany ze źródła
├── documentations/    # dokumentacja projektów (osobny folder)
│   └── <project-id>/      # submodule do repo docs LUB mirror / index linków
├── data/              # landscape.json, docs_index.json, overrides
├── pipeline/          # logika Python
├── scripts/           # scrape, sync, discover, generate
└── site/              # wiki Astro Starlight
```

---

## 1. Infrastruktura repozytorium

- [x] Zainicjować repozytorium Git (`git init`) → [github.com/kacperpaczos/awesome-CNCF](https://github.com/kacperpaczos/awesome-CNCF)
- [x] Utworzyć trzy osobne foldery w root:
  - `projects/` — submoduły do repozytoriów z kodem
  - `openapis/` — specyfikacje OpenAPI (nie wewnątrz `projects/`)
  - `documentations/` — dokumentacja projektów (nie wewnątrz `projects/`)
- [ ] Zdefiniować wspólną konwencję nazewnictwa: `<project-id>/` we wszystkich trzech folderach (np. `orchestration-management--scheduling-orchestration--kubernetes`)
- [ ] Dodać `projects/`, `openapis/`, `documentations/` do `.gitignore` tam, gdzie potrzeba (puste placeholdery / `.gitkeep`), submoduły przez `.gitmodules`
- [ ] Napisać skrypt `scripts/sync_submodules.py`:
  - iteracja po `data/landscape.json`
  - dla projektów z `primary_repo_url` / `repositories[]` → `git submodule add`
  - pomijanie duplikatów URL (wiele projektów → jedno repo)
  - raport: dodane / pominięte / błędy / brak repo
- [ ] Dodać `.gitmodules` i dokumentację aktualizacji submodułów (`git submodule update --init --recursive`)
- [ ] CI: okresowa synchronizacja submodułów i walidacja stanu

---

## 2. Folder `openapis/` — generator standardów OpenAPI

- [ ] Utworzyć folder `openapis/` w root (osobny od `projects/` i `documentations/`)
- [ ] Utworzyć `scripts/generate_openapi.py` (lub moduł `pipeline/openapi.py`)
- [ ] Dla każdego projektu generować / umieszczać spec w `openapis/<project-id>/`:
  - `openapi.yaml` — kanoniczny plik specyfikacji
  - `meta.json` — status, źródło, data, link do repo źródłowego
- [ ] Minimalny szablon OpenAPI (nagłówek, info, serwery, tagi, placeholder paths) wypełniany z metadanych:
  - `name`, `description`, `homepage_url`, `primary_repo_url`, `maturity`, `category`
- [ ] Wykrywanie istniejących speców — skan `projects/<project-id>/` (submodule):
  - pliki `openapi.yaml`, `openapi.json`, `swagger.yaml`, `swagger.json`
  - katalogi `api/`, `spec/`, `docs/api/`
  - adnotacje w README / linki w repo
- [ ] Jeśli znaleziono oficjalny spec w repo → **skopiować do `openapis/<project-id>/`**, nie trzymać w submodule
- [ ] Status per projekt: `found` | `generated` | `todo` | `n/a` (brak API / brak repo)
- [ ] Zaktualizować generator wiki (`pipeline/starlight.py`) — linki do `openapis/<project-id>/`
- [ ] Zaktualizować katalog (`pipeline/catalog.py`) — kolumna OpenAPI → `/openapis/<project-id>/`

---

## 3. Folder `documentations/` — oficjalna dokumentacja projektów

- [ ] Utworzyć folder `documentations/` w root (osobny od `projects/` i `openapis/`)
- [ ] Dla każdego projektu katalog `documentations/<project-id>/`:
  - `index.json` — oficjalny URL docs, źródło odkrycia, data weryfikacji
  - opcjonalnie submodule Git — jeśli dokumentacja ma osobne repo (np. `*-docs`, `website`)
  - opcjonalnie mirror / snapshot — statyczna kopia do offline (jeśli licencja i rozmiar na to pozwalają)
- [ ] Rozszerzyć model danych w `pipeline/parser.py` o pola:
  - `docs_url` — oficjalna dokumentacja techniczna (URL zewnętrzny)
  - `docs_local_path` — ścieżka w `documentations/<project-id>/`
  - `docs_source` — skąd pochodzi: `landscape` | `repo` | `web` | `submodule` | `manual`
  - `docs_candidates[]` — alternatywne URL-e do weryfikacji
- [ ] Napisać `scripts/discover_docs.py`:
  - **Źródło 1 — repo (`projects/`):** przeszukanie README, `docs/`, `mkdocs.yml`, `book.toml`, `docusaurus.config.js`, `website/`, linki `docs.*`, `documentation`
  - **Źródło 2 — internet:** wyszukiwanie „{nazwa projektu} official documentation site” (API wyszukiwarki / scraping z ograniczeniami rate-limit)
  - **Źródło 3 — homepage:** heurystyka (np. `docs.{domena}`, `/docs`, link z `homepage_url`)
  - walidacja URL (HTTP 200, content-type, słowa kluczowe „documentation”, „docs”)
  - jeśli docs są w osobnym repo → `git submodule add` do `documentations/<project-id>/`
- [ ] Zapisywać indeks odkrytych linków do `data/docs_index.json` (cache)
- [ ] Rozróżnić w wiki i katalogu:
  - **Strona główna** (`homepage_url`)
  - **Dokumentacja online** (`docs_url`)
  - **Dokumentacja lokalna** (`documentations/<project-id>/`)
  - **Repozytorium kodu** (`projects/<project-id>/`)
- [ ] Ręczna weryfikacja / override w `data/docs_overrides.json`
- [ ] CI: okresowe odświeżanie `docs_index.json` + `documentations/` + raport martwych linków

---

## 4. Indeks (to repo) — integracja

- [ ] Traktować `data/landscape.json` jako kanoniczne źródło listy projektów
- [ ] Każda strona wiki projektu powinna linkować do trzech osobnych folderów:
  - `projects/<project-id>/` — kod źródłowy (submodule)
  - `documentations/<project-id>/` — dokumentacja (URL + ewentualny submodule / mirror)
  - `openapis/<project-id>/` — specyfikacja OpenAPI
- [ ] `CATALOG.md` / README — kolumny: Narzędzie | Docs | Repo | OpenAPI
- [ ] `contributing/index.md` — zaktualizować ścieżki: `projects/`, `documentations/`, `openapis/` (zamiast starego `openapi/`)

---

## 5. Autonomiczność (autonomous)

- [ ] GitHub / hosting — publikacja wiki (GitHub Pages lub inny)
- [ ] Cron / GitHub Actions:
  - `scrape.py` — odświeżenie danych z landscape.cncf.io
  - `discover_docs.py` — aktualizacja linków dokumentacji
  - `sync_submodules.py` — synchronizacja submodułów
  - `generate_openapi.py` + `generate_docs.py` — regeneracja wiki i katalogu
- [ ] Powiadomienia o zmianach (nowe projekty, martwe linki, nowe commity w submodułach)

---

## 6. Priorytety wdrożenia

1. `git init` + utworzenie trzech folderów: `projects/`, `openapis/`, `documentations/`
2. `sync_submodules.py` → `projects/` (projekty z repo GitHub)
3. `discover_docs.py` → `documentations/` (skan repo, potem web)
4. `generate_openapi.py` → `openapis/` (szablon + kopiowanie ze znalezionych speców w `projects/`)
5. Integracja z wiki i katalogiem
6. CI i hosting

---

## Uwagi

- ~59% projektów (1420) nie ma publicznego repo — `projects/` i `openapis/` jako `n/a`, ale `documentations/` nadal wypełniać przez wyszukiwanie w internecie
- ~41% (989) ma `primary_repo_url` — pełny pipeline: submodule w `projects/` + skan repo → `documentations/` + `openapis/`
- Trzy foldery są **równoległe w root** — OpenAPI nie ląduje w `projects/`, dokumentacja nie ląduje w `openapis/`
- Istniejący placeholder `openapi/<project-id>/` w kodzie (`pipeline/enrichment.py`) — **zastąpić** folderem `openapis/<project-id>/`
- Nazwa projektu: **autonomous** (nie AWS) — autonomiczna, samoaktualizująca się baza wiedzy