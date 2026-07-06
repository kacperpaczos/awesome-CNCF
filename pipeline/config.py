from pathlib import Path

BASE_URL = "https://landscape.cncf.io"
FULL_DATA_URL = f"{BASE_URL}/data/full.json"
GUIDE_DATA_URL = f"{BASE_URL}/data/guide.json"
LANDSCAPE_PAGE_URL = (
    f"{BASE_URL}/?view-mode=card&classify=maturity&sort-by=name&sort-direction=asc"
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
CACHE_DIR = DATA_DIR / "cache"
SITE_DIR = PROJECT_ROOT / "site"
LOGOS_DIR = SITE_DIR / "public" / "logos"

REQUEST_TIMEOUT = 60
USER_AGENT = (
    "CNCF-Landscape-KB-Scraper/0.1 "
    "(+https://github.com; educational knowledge-base project)"
)
