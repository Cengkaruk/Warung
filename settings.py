# Django settings for Warung project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Aji Kisworo Mukti', 'adzy@di.blankon.in'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'warung.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Asia/Jakarta'
LANGUAGE_CODE = 'en'
SITE_ID = 1
USE_I18N = False

import os
MEDIA_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = '(fo--szdsapjf02jfj02f2mfk00202b)kwd5p=xwq@xl(++3^^hoiyou%m725qkp53iql7_a('

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'Warung.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)
