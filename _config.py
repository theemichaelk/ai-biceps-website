"""Site configuration — edit before deploy or set environment variables."""

import os
from pathlib import Path

_ROOT = Path(__file__).parent
_ENV_FILE = _ROOT / ".env"


def _load_dotenv():
    """Load KEY=VALUE pairs from .env into os.environ (no overwrite)."""
    if not _ENV_FILE.exists():
        return
    for line in _ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


_load_dotenv()

# Formspree endpoint (https://formspree.io) — leave empty to use mailto fallback
FORMSPREE_ENDPOINT = os.environ.get("TSBR_FORMSPREE_ENDPOINT", "")

# Google Analytics 4 measurement ID (e.g. G-XXXXXXXXXX) — leave empty to disable
GA_MEASUREMENT_ID = os.environ.get("TSBR_GA_MEASUREMENT_ID", "")

# Google Maps embed for Arlington HQ
GOOGLE_MAPS_EMBED = os.environ.get(
    "TSBR_GOOGLE_MAPS_EMBED",
    "https://maps.google.com/maps?q=518+Brynmawr+Ct,+Arlington,+TX+76014&output=embed",
)

# Public profiles — set in .env for production; Google Maps is the default fallback
_GOOGLE_PROFILE = (
    "https://www.google.com/maps/search/?api=1&query=The+Stone+Builders+Rejected+Arlington+TX"
)
SOCIAL_URLS = {
    "google": os.environ.get("TSBR_GOOGLE_PROFILE", _GOOGLE_PROFILE),
    "facebook": os.environ.get("TSBR_FACEBOOK", _GOOGLE_PROFILE),
    "twitter": os.environ.get("TSBR_TWITTER", _GOOGLE_PROFILE),
    "instagram": os.environ.get("TSBR_INSTAGRAM", _GOOGLE_PROFILE),
    "linkedin": os.environ.get("TSBR_LINKEDIN", _GOOGLE_PROFILE),
}