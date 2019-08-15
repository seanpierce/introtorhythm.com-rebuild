"""
Django settings for introtorhythm project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import os.path
import configparser

# configs = ['./env.ini', './test.env.ini']
CONFIG = configparser.RawConfigParser()

try:
    CONFIG.read('./env.ini')
except Exception as e:
    CONFIG.read('./test.env.ini')


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tg#v3opo9aqqm#rns#^t(+29)@@!#e1bk!_47q)biu$_e-_m*j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = eval(CONFIG.get('Environment', 'DEBUG'))

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = CONFIG.get('Environment', 'ALLOWED_HOSTS').split(',')
HOST_URL = CONFIG.get('Environment', 'HOST_URL')

if DEBUG is True:
	SECURE_SSL_REDIRECT = False
else:
	SECURE_SSL_REDIRECT = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'episode',
    'subscribers',
    'webpack_loader',
    'storages',
    'ckeditor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'introtorhythm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'introtorhythm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = ''
STATIC_URL = '/assets/'
STATICFILES_DIRS = ( os.path.join('assets'), )

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}

AWS_ACCESS_KEY_ID = CONFIG.get('AWS Secret Keys', 'AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = CONFIG.get('AWS Secret Keys', 'AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'podcasts.introtorhythm.com'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

DEFAULT_FILE_STORAGE = 'introtorhythm.storage_backends.MediaStorage'

# Email Settings

if not DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = CONFIG.get('EMAIL SECRET KEYS', 'EMAIL_HOST')
    EMAIL_HOST_USER = CONFIG.get('EMAIL SECRET KEYS', 'EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = CONFIG.get('EMAIL SECRET KEYS', 'EMAIL_HOST_PASSWORD')
    EMAIL_PORT = int(CONFIG.get('EMAIL SECRET KEYS', 'EMAIL_PORT'))
    EMAIL_USE_TLS = True
else:
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = 'tmp/emails/'
