"""Local scaffold settings. No production configuration or sign-in exists yet."""

from salty.config import LOCAL, load_config

CONFIG = load_config()
SECRET_KEY = CONFIG["secret_key"]
DEBUG = False
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]
ROOT_URLCONF = "salty.urls"
INSTALLED_APPS = ["django.contrib.contenttypes"]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": LOCAL / "salty.sqlite3"}}
MEDIA_ROOT = LOCAL / "files"
USE_TZ = True
TIME_ZONE = "UTC"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
