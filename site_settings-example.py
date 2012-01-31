# Site-specifig django settings.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Your name', 'your-email@example.org'),
)

SERVER_EMAIL = 'root'

MANAGERS = ADMINS

DATABASE_ENGINE = 'postgresql_psycopg2' # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'tjrapid'               # Or path to database file if using sqlite3.
DATABASE_USER = 'tjrapid'               # Not used with sqlite3.
DATABASE_PASSWORD = ''                  # Not used with sqlite3.
DATABASE_HOST = ''                      # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Absolute path to the root directory.
ROOT = '/home/user/www/tjrapid/'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = root + 'site_media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/site_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '8$w)5-w9ux6n1lzdruw7g5!%rx*pdgwi2_gb2p8^*rppxi5^dw'

TEMPLATE_DIRS = (
    root + 'templates/',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

FONTS_DIR = root + 'fonts/'

