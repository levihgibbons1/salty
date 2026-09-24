"""Fail-closed local configuration, without exposing values in diagnostics."""

import json
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured

ROOT = Path(__file__).resolve().parents[1]
LOCAL = ROOT / ".local"


def load_config(path=None):
    path = path or LOCAL / "settings.json"
    try:
        config = json.loads(path.read_text())
    except (OSError, ValueError):
        raise ImproperlyConfigured(
            "Local configuration is missing or invalid. Run: python scripts/dev.py setup"
        ) from None
    if not isinstance(config, dict) or config.get("environment") not in {"development", "test"}:
        raise ImproperlyConfigured(
            "This scaffold supports development/test only; production is disabled."
        )
    key = config.get("secret_key")
    if not isinstance(key, str) or len(key) < 50 or key == "GENERATE_LOCALLY_WITH_SETUP":
        raise ImproperlyConfigured(
            "secret_key must be a generated value of at least 50 characters."
        )
    return config
