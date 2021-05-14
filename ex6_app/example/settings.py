from __future__ import annotations

import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

DEBUG = os.environ.get("DEBUG", "") == "1"

SECRET_KEY = "django-insecure-b92+0uh45p*zjtcmi%5y+&#)bmjr0%)j8nwdf&**bwl@jz03h^"

# Dangerous: disable host header validation
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "example.core",
]

ROOT_URLCONF = "example.urls"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
