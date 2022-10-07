"""
Django settings for introtorhythm project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import os.path
import configparser
import datetime

# configs = ['./env.ini', './test.env.ini']
CONFIG = configparser.RawConfigParser()
CONFIG.read('./env.ini')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hq(x#eh(h^b@cqy584bt_wq_x_yh=d%&ls%bb1r&8dq9apy1oe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = eval(CONFIG.get('Environment', 'DEBUG'))

# URL Config
CORS_ALLOW_CREDENTIALS = True
ORIGIN_WHITELIST = CONFIG.get('Environment', 'CORS_ORIGIN_WHITELIST').split(',')
ALLOWED_HOSTS = ORIGIN_WHITELIST
CORS_ALLOWED_ORIGINS = ORIGIN_WHITELIST
CSRF_TRUSTED_ORIGINS = ORIGIN_WHITELIST
CORS_ORIGIN_WHITELIST = ORIGIN_WHITELIST
HOST_URL = CONFIG.get('Environment', 'HOST_URL')
CSRF_COOKIE_SAMESITE = 'None'

# Application definition
INSTALLED_APPS = [
    'admin_extension',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'episodes',
    'content',
    'subscribers',
    'schedule',
    'ckeditor',
    'api',
    'repositories'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'introtorhythm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

now = datetime.datetime.now()
log_name = str(now.year) + '-' + str(now.month) + '-' + str(now.day)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/' + log_name + '.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}

WSGI_APPLICATION = 'introtorhythm.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# pulls in assets for the Django Admin settings
STATIC_ROOT = 'static'
if DEBUG:
    STATIC_URL = '/assets/'
else:
    STATIC_URL = '/static/'

# the location where the static assets live
# note: when the app references the public URL, it will point to the assets folder
# note2: all files under this directory will be pulled into the static folder
STATICFILES_DIRS = [os.path.join('assets')]

# local storage
MEDIA_ROOT = 'uploads/'

# AWS S3 file storage
DEFAULT_FILE_STORAGE = 'introtorhythm.storage_backends.MediaStorage'

AWS_ACCESS_KEY_ID = CONFIG.get('AWS Secret Keys', 'AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = CONFIG.get('AWS Secret Keys', 'AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'podcasts.introtorhythm.com'
AWS_DEFAULT_ACL = 'public-read'
AWS_MEDIA_URL = 'https://s3.amazonaws.com/%s/media/' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = CONFIG.get('EMAIL SECRET KEYS', 'EMAIL_HOST')
EMAIL_HOST_USER = CONFIG.get('EMAIL SECRET KEYS', 'EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = CONFIG.get('EMAIL SECRET KEYS', 'EMAIL_HOST_PASSWORD')
EMAIL_PORT = int(CONFIG.get('EMAIL SECRET KEYS', 'EMAIL_PORT'))
EMAIL_USE_TLS = True
EMAIL_BOOKING_RECIPIENT = CONFIG.get('EMAIL SECRET KEYS', 'EMAIL_BOOKING_RECIPIENT')