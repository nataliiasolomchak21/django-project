from pathlib import Path
import os
import dj_database_url

development = os.environ.get('DEVELOPMENT', True)

if os.path.isfile("env.py"):
    import env

# The comments at the top explain what this file is for - it configures the Django settings for a project called django_todo.
"""
Django settings for django_todo project.

Generated by 'django-admin startproject' using Django 3.2.22.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
# We import pathlib to help with file paths later.
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR sets the base directory for the project. This tells Django where to look for files.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY is generated when starting the project. This is like a password Django uses to encrypt private data.
SECRET_KEY = os.environ.get('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True means Django will show more details about errors. This helps during development.
DEBUG = development


# ALLOWED_HOSTS is a whitelist of sites the Django site can be accessed from. It's empty now so anyone can access it.
if development:
    ALLOWED_HOSTS = ['ckz8780-django-todo-project-eac7d080498b.herokuapp.com']
else:
    ALLOWED_HOSTS = ['127.0.0.1']


# Application definition
# INSTALLED_APPS lists the Django apps used in this project. Default ones like admin, auth, contenttypes etc are already added.
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "todo",
]
# MIDDLEWARE lists middleware that process requests/responses in Django.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
# ROOT_URLCONF sets the main urls.py file Django uses for routing.
ROOT_URLCONF = "django_todo.urls"
# TEMPLATES configures the template engine Django uses to render pages.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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
# WSGI_APPLICATION points to the file for deploying Django with WSGI servers.
WSGI_APPLICATION = "django_todo.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# DATABASES defines the database config for Django.
# if development:
#     DATABASES = {
#         'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
#     }
# else:
DATABASES = {
    # 'default' is the default database connection name.
    "default": {
        # ENGINE specifies to use 'django.db.backends.sqlite3' - this means use SQLite for the database.
        "ENGINE": "django.db.backends.sqlite3",
        # NAME gives the database file path - BASE_DIR/db.sqlite3 tells it to create a db.sqlite3 file in the base directory.
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
# AUTH_PASSWORD_VALIDATORS defines some validators to apply certain password rules.
AUTH_PASSWORD_VALIDATORS = [
    {
        # No commonly used passwords
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        # Minimum length
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        # Can't be entirely numeric
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        # Not too similar to username
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"
# USE_I18N, USE_L10N, USE_TZ enable internationalization features.
USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
# STATIC_URL defines the base URL path where static files are served from, like '/static/'.
STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
# DEFAULT_AUTO_FIELD sets the default primary key type for models.
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
