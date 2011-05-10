# Django settings for Warung project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Aji Kisworo Mukti', 'adzy@di.blankon.in'),
    ('Azhari Harahap', 'azhari@harahap.us'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'media/db/warung.sqlite'
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

TIME_ZONE = 'Asia/Jakarta'
LANGUAGE_CODE = 'en'
SITE_ID = 1
USE_I18N = False

import os.path
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = '(fo--szdsapjf02jfj02f2mfk00202b)kwd5p=xwq@xl(++3^^hoiyou%m725qkp53iql7_a('

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'web.global.kategori_list',
    )

ROOT_URLCONF = 'Warung.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'web',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
)
