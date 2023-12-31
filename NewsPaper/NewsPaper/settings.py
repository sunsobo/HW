"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(8@wc0du9sd^*1rf)stjy_2frc47^%&x3r$@@%$^+moqq_azq9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'newapp',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',
    'home',
    # 'fpages',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'NewsPaper.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGIN_REDIRECT_URL = "/news"

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "koder.s@yandex.ru"
EMAIL_HOST_PASSWORD = "LKJADHfo8203fj9_fds09j"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "Django News"

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://localhost:6379',
    }
}

# Celery settings

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Moscow'


SERVER_EMAIL = 'koder.s@yandex.ru'
DEFAULT_FROM_EMAIL = 'koder.s@yandex.ru'


EMAIL_FILE_PATH = 'email-messages'



# LOGGING
ADMINS = [("Admin", "sunsobolev@gmail.com"), ]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'console_1': {
            'format': '%(asctime)s-12s %(levelname)-4s %(message)s'
        },
        'console_2': {
            'format': '%(asctime)s-12s %(levelname)-8s %(pathname)-4s %(message)s'
        },
        'console_3': {
            'format': '%(asctime)s-12s %(levelname)-8s %(pathname)-4s %(exc_info)-2s %(message)s'
        },


        'file_general': {
            'format': '%(asctime)s %(levelname)-12s %(module)-8s %(message)s'
        },
        'file_errors': {
            'format': '%(asctime)s %(levelname)-12s %(message)-10s %(pathname)-8s %(stack_info)s'
        },
        'file_security': {
            'format': '%(asctime)s %(levelname)-12s %(module)-8s %(message)s'
        },
        'file_email': {
            'format': '%(asctime)s %(levelname)-12s %(message)-8s %(pathname)-s'
        },

    },

    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },

    'handlers': {
        # console
        'console_1': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_1',
        },
        'console_2': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_2',
        },
        'console_3': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_3',
        },
        'console_4': {
            'level': 'CRITICAL',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_3',
        },

        # general
        'file_general': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'file_general',
            'filename': '../_general.log_'
        },


        # errors
        'file_errors_1': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'file_errors',
            'filename': '../_errors.log_'
        },
        'file_errors_2': {
            'level': 'CRITICAL',
            'class': 'logging.FileHandler',
            'formatter': 'file_errors',
            'filename': '../_errors.log_'
        },


        # security
        'file_security': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file_security',
            'filename': '../_security.log_'
        },


        'mail_admins': {
            'level': 'ERROR',
            # отправка только, когда DEBUG=False
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'file_email',
            'include_html': True,
        },
    },

    'loggers': {
        # general
        'django': {
            'level': 'DEBUG',
            'handlers': [
                'console_1',
                'console_2',
                'console_3',
                'console_4',
                'file_general'
            ],
        },


        # errors
        'django.request': {
            'level': 'DEBUG',
            'handlers': ['file_errors_1', 'file_errors_2', 'mail_admins'],
        },
        'django.server': {
            'level': 'DEBUG',
            'handlers': ['file_errors_1', 'file_errors_2', 'mail_admins'],
        },
        'django.template': {
            'level': 'DEBUG',
            'handlers': ['file_errors_1', 'file_errors_2'],
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['file_errors_1', 'file_errors_2'],
        },


        # security
        'django.security': {
            'level': 'DEBUG',
            'handlers': ['file_security'],
        },
    },
}
