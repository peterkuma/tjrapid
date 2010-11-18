# Django settings.

from site_settings import *

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Bratislava'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
LANGUAGE_CODE = 'sk'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
#   'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'tjrapid.main.middleware.LanguageMiddleware', 
    'tjrapid.main.middleware.CategoryMiddleware', 
)

ROOT_URLCONF = 'tjrapid.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs', 
#   'django.contrib.flatpages',
    'django.contrib.markup',
    'tjrapid.main',
    'tjrapid.ob',
    'tjrapid.news',
    'tjrapid.eventapp',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.i18n',
    'django.core.context_processors.auth',
    'tjrapid.main.context_processors.category', 
)

SESSION_SAVE_EVERY_REQUEST = True

import os
RGFONT = os.path.join(FONTS_DIR, 'LiberationSans-Regular.ttf')
BDFONT = os.path.join(FONTS_DIR, 'LiberationSans-Bold.ttf')
ITFONT = os.path.join(FONTS_DIR, 'LiberationSans-Italic.ttf')

