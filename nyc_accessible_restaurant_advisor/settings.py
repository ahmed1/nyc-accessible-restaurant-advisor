"""
Django settings for nyc_accessible_restaurant_advisor project.
Generated by 'django-admin startproject' using Django 3.1.2.
For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import django_heroku
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

os.environ["PATH"] = (
    os.path.join(BASE_DIR, r"venv\Lib\site-packages\osgeo") + ";" + os.environ["PATH"]
)
os.environ["PROJ_LIB"] = (
    os.path.join(BASE_DIR, r"env3\Lib\site-packages\osgeo\data\proj")
    + ";"
    + os.environ["PATH"]
)
GDAL_LIBRARY_PATH = os.path.join(BASE_DIR, r"venv\lib\site-packages\osgeo\gdal301.dll")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "j6^f1g$)jqbn*d-3n$!n2rk7*9r&@i-fsbd1p_=6^4&$lh@)^g"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "accessible_restaurant.apps.AccessibleRestaurantConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "django.contrib.sites",
    "crispy_forms",
    "import_export",
    "django_filters",
    "leaflet",
    "storages",
    # allauth related apps
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # providers
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.facebook",
]

SITE_ID = 1

AUTH_USER_MODEL = "accessible_restaurant.User"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "nyc_accessible_restaurant_advisor.urls"

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

WSGI_APPLICATION = "nyc_accessible_restaurant_advisor.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_USER_MODEL = "accessible_restaurant.User"


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# AWS settings
AWS_ACCESS_KEY_ID = "AKIAR4MJX54OQDOW2X6E"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "accessible-restaurant"
AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
# AWS_DEFAULT_ACL = 'public-read'
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}

AWS_MEDIA_LOCATION = "media"
MEDIAFILES_DIRS = [
    os.path.join(BASE_DIR, "media"),
]
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_MEDIA_LOCATION)
DEFAULT_FILE_STORAGE = "accessible_restaurant.storage_backends.MediaStorage"


CRISPY_TEMPLATE_PACK = "bootstrap4"

# Email setting
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "nyc.accessible.rest@gmail.com"
EMAIL_HOST_PASSWORD = "6063team408"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
DEFAULT_TO_EMAIL = "nyc.accessible.rest@gmail.com"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"


django_heroku.settings(locals(), test_runner=False)


# Yelp parameters
YELP_REST_ENDPOINT = "https://api.yelp.com/v3/businesses/"
YELP_TOKEN = "PKbT9xaBBV7GvQU72SRGf-0JAz4-CvMu1zVOeKA2Bz5heJQAHoONKYNRX-AUYP0JwzL2da6aFBFKLPPZipnO5LFDsQlcq2QUJs_UhMhalZnv59QNaXK591UFIZKXX3Yx"

LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/accounts/login"
LOGOUT_REDIRECT_URL = "/"
GDAL_LIBRARY_PATH = os.environ.get('GDAL_LIBRARY_PATH')
GEOS_LIBRARY_PATH = os.environ.get('GEOS_LIBRARY_PATH')

# GEOIP_PATH = os.path.join(BASE_DIR, "geoip")
# GDAL_LIBRARY_PATH = os.environ.get("GDAL_LIBRARY_PATH")

# Leaflet parameters
LEAFLET_CONFIG = {"SCALE": None, "RESET_VIEW": False}

# Third party email configuration
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_QUERY_EMAIL = False
SOCIALACCOUNT_EMAIL_REQUIRED = False
SOCIALACCOUNT_STORE_TOKENS = False

# Third party account adpter
ACCOUNT_ADAPTER = "nyc_accessible_restaurant_advisor.users.adapter.UserAccountAdapter"
SOCIALACCOUNT_ADAPTER = (
    "nyc_accessible_restaurant_advisor.users.adapter.CustomSocialAccountAdapter"
)
