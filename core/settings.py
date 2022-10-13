"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.1.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Load env
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR.joinpath("templates")
STATIC_DIR = BASE_DIR.joinpath("static")
MEDIA_DIR = BASE_DIR.joinpath("media")

# Environment Variables
ON_PRODUCTION = os.getenv("ON_PRODUCTION") == "True"
DJANGO_DB_ENGINE = os.getenv("DB_ENGINE")
DJANGO_DB_NAME = os.getenv("DB_NAME")
DJANGO_DB_USER = os.getenv("DB_USER")
DJANGO_DB_PASSWORD = os.getenv("DB_PASSWORD")
DJANGO_DB_HOST = os.getenv("DB_HOST")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not ON_PRODUCTION

# Hosts allowed for project
ALLOWED_HOSTS = ["127.0.0.1", ".vercel.app"]

# Django built-in apps
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# Third Party apps
THIRD_PARTY_APPS = []

# local django apps
LOCAL_APPS = []

# Application definition

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

if ON_PRODUCTION:
    USE_X_FORWARDED_HOST = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    DATABASES = {
        "default": {
            "ENGINE": f"django.db.backends.{DJANGO_DB_ENGINE}",
            "NAME": DJANGO_DB_NAME,
            "USER": DJANGO_DB_USER,
            "PASSWORD": DJANGO_DB_PASSWORD,
            "HOST": DJANGO_DB_HOST,
        }
    }

else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    }
]

# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Dhaka"

USE_I18N = True

USE_TZ = True

# Media files

MEDIA_URL = "media/"
MEDIA_ROOT = MEDIA_DIR

# Static files (CSS, JavaScript, Images)

STATIC_URL = "static/"

if ON_PRODUCTION:
    STATIC_ROOT = STATIC_DIR
else:
    STATICFILES_DIRS = [STATIC_DIR]

# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
