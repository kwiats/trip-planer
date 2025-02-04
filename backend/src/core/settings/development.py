import sys
from datetime import timedelta
from logging import config

from core.settings.base import *

# BASIC
SECURE_SSL_REDIRECT = False

# APPS
INSTALLED_APPS += [
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.github",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "drf_spectacular",
]

# MIDDLEWARE
MIDDLEWARE += [
    "allauth.account.middleware.AccountMiddleware",
]

# CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:9000",
    "http://127.0.0.1:9000",
    "http://127.0.0.1:8000",
]
CORS_URLS_REGEX = r"^/api/.*$"

# STORAGES
DEFAULT_STORAGE = "storages.backends.s3boto3.S3StaticStorage"
MEDIA_STORAGE = "core.storages.MediaS3Boto3Storage"
MEDIA_FILE_SIZE = 5 * 1024 * 1024  # 5MB
MEDIA_FILE_TYPE = "webp"
MEDIA_FILE_QUALITY = 100
MEDIA_DEFAULT_FOLDER = "media"
STORAGE_ACCESS_KEY = os.environ.get("STORAGE_ACCESS_KEY", "superuser")
STORAGE_SECRET_KEY = os.environ.get("STORAGE_SECRET_KEY", "superuser")
STORAGE_ENDPOINT_URL = os.environ.get("STORAGE_ENDPOINT_URL", "http://localhost:9000")
STORAGE_BUCKET_NAME = os.environ.get("STORAGE_BUCKET_NAME", "files")
STORAGE_REGION_NAME = os.environ.get("STORAGE_REGION_NAME", None)
DEFAULT_STORAGE_OPTIONS = {
    "access_key": STORAGE_ACCESS_KEY,
    "secret_key": STORAGE_SECRET_KEY,
    "bucket_name": STORAGE_BUCKET_NAME,
    "endpoint_url": STORAGE_ENDPOINT_URL,
}
DEFAULT_PUBLIC_STORAGE_OPTIONS = {
    "default_acl": "public-read",
    "file_overwrite": True,
    "querystring_auth": False,
}
STORAGES = {
    "staticfiles": {
        "BACKEND": DEFAULT_STORAGE,
        "OPTIONS": {
            **DEFAULT_STORAGE_OPTIONS,
            **DEFAULT_PUBLIC_STORAGE_OPTIONS,
            "location": "static",
        },
    },
    "media": {
        "BACKEND": MEDIA_STORAGE,
    },
}
STATIC_URL = f"{STORAGE_ENDPOINT_URL}/{STORAGE_BUCKET_NAME}/static/"
# MEDIA_URL = f"{STORAGE_ENDPOINT_URL}/{STORAGE_BUCKET_NAME}/media/"

# REST FRAMEWORK
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
        # "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "NON_FIELD_ERRORS_KEY": "errors",
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning",
    "DEFAULT_VERSION": os.environ.get("API_VERSION", "v1"),
    "ALLOWED_VERSIONS": ["v1", "v2"],
}

# SPECTACULAR
SPECTACULAR_SETTINGS = {
    "TITLE": "My API",
    "DESCRIPTION": "API documentation",
    "VERSION": "1.0.0",
}

# ALLAUTH
SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_AUTHENTICATION_METHOD = "email"

# REST AUTH
REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_HTTPONLY": False,
    "REGISTER_SERIALIZER": "apps.auth.serializers.RegisterSerializer",
    "LOGIN_SERIALIZER": "apps.auth.serializers.LoginSerializer",
    "JWT_AUTH_COOKIE": "access-token",
    "JWT_AUTH_REFRESH_COOKIE": "refresh-token",
}

# JWT
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=180),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "BLACKLIST_AFTER_ROTATION": False,
    "ROTATE_REFRESH_TOKENS": False,
    "UPDATE_LAST_LOGIN": True,
    "ALGORITHM": os.environ.get("TOKEN_ALGORITHM", "HS256"),
}

# DEBUG TOOLBAR
ENABLE_DEBUG_TOOLBAR = DEBUG and "test" not in sys.argv
if ENABLE_DEBUG_TOOLBAR:
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]
    INSTALLED_APPS += ("debug_toolbar",)
    INTERNAL_IPS = ["127.0.0.1", "localhost", "192.168.0.1", "10.0.2.2", "::1"]
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

    DEBUG_TOOLBAR_CONFIG = {
        "INTERCEPT_REDIRECTS": False,
        "DISABLE_PANELS": [
            "debug_toolbar.panels.redirects.RedirectsPanel",
        ],
        "SHOW_TEMPLATE_CONTEXT": True,
        "SHOW_TOOLBAR_CALLBACK": lambda request: True,
    }

# LOGGING
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "rich": {"datefmt": "[%X]"},
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "rich.logging.RichHandler",
            "filters": ["require_debug_true"],
            "formatter": "rich",
            "level": "DEBUG",
            "rich_tracebacks": True,
            "tracebacks_show_locals": True,
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "celery": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}
config.dictConfig(LOGGING)
