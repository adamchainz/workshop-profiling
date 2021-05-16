from __future__ import annotations

import getpass
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}}

DEBUG = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Dangerous: disable host header validation
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    # Scout needs priority
    "scout_apm.django",
    # First party
    "example.core",
    # Third party
    "debug_toolbar",
    # Contrib
    "django.contrib.staticfiles",
]

INTERNAL_IPS = [
    "127.0.0.1",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "example.urls"

SECRET_KEY = "django-insecure-b92+0uh45p*zjtcmi%5y+&#)bmjr0%)j8nwdf&**bwl@jz03h^"

STATIC_URL = "/static/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
            ],
        },
    }
]

# scout-apm
SCOUT_MONITOR = True
SCOUT_KEY: str = os.environ.get("SCOUT_KEY", "")
SCOUT_NAME = f"{getpass.getuser()} Demo App"
