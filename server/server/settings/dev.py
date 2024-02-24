from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-86#b&^eempn+dwyzbj^@=vvi#p@yj7&vs4^u1ibet$!9^ch+#_"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "db_name",
#         "USER": "postgres",
#         "PASSWORD": "db_pwd",
#         "HOST": "127.0.0.1",
#         "PORT": "5432",
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    }
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5500",  # Live Server
    "http://localhost:3000",  # Create React App 1
    "http://localhost:3001",  # Create React App 1
    "http://localhost:5173",  # Vite
    "http://localhost:5174",  # Vite 2
]

INTERNAL_IPS = [
    "http://127.0.0.1"
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} - {asctime} | P : {process:d}, T : {thread:d} | {module} : {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} - {asctime} | {module} : {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "django": {"handlers": ["console"], "propogate": True, "level": "INFO"}
    },
}
