# event_manager/settings.py
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure--*hlfv-9bx%@rki*yifg!vlq-(k-z(3e_rd$wilus5c*@&e_!0"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "example.com",
    "localhost",
    "127.0.0.1",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",  # < im dev-betrieb standard static auschalten
    "django.contrib.staticfiles",
    "django_extensions",
    "events",
    "crispy_forms",
    "crispy_bootstrap5",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # <<<<< HIER
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Dateien werden im Browser gecached und komprimiert (gzip)
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Formulare (Crispy forms unterstützt div. Templatepacks, u.a. bootstrap 2 - 5)
CRISPY_TEMPLATE_PACK = "bootstrap5"

if DEBUG:
    MIDDLEWARE.extend(["debug_toolbar.middleware.DebugToolbarMiddleware"])

    # Apps, die nur lokal genutzt werden
    INSTALLED_APPS.extend(["debug_toolbar"])

    DEBUG_TOOLBAR_CONFIG = {
        "INTERCEPT_REDIRECTS": False,
    }

    INTERNAL_IPS = ("127.0.0.1",)


ROOT_URLCONF = "event_manager.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "event_manager" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "event_manager.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "de-DE"

TIME_ZONE = "Europe/Berlin"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

# der URL-Pfad, unter dem statischen Dateien in der URL stehen
STATIC_URL = "static/"  # {% static %}
# hier sucht Django nach statischen Dateien (css, images, js):
STATICFILES_DIRS = [BASE_DIR / "static"]

# manage.py collectstatic sammelt alle Dateien in diesem Verzeichnis.
# dieses Verzeichnis wird in .gitignore notiert
STATIC_ROOT = BASE_DIR / "staticfiles"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
