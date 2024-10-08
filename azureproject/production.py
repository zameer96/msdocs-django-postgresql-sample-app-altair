import os
import json

from .settings import *  # noqa
from .settings import BASE_DIR

# Configure the domain name using the environment variable
# that Azure automatically creates for us.
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
DEBUG = True

# WhiteNoise configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Add whitenoise middleware after the security middleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configure Postgres database based on connection string of the libpq Keyword/Value form
# https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
default_database = os.getenv('DATABASE_URL')
if default_database.startswith('{'):
    print("PPEEEE")
    default_database = json.loads(default_database)
else:
    print("PPIIII  ", default_database)
    default_database = dj_database_url.parse(default_database)
print("PROD DB -----DD >>> ", default_database)


DATABASES = {
    'default': default_database
}

cache_default = os.getenv('CACHE_URL')
if cache_default.startswith('{'):
    cache_default = json.loads(cache_default)

CACHES = {
        "default": cache_default,
}