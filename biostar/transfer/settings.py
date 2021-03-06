from conf.examples.pg.pg_settings import *

import os
TRANSFER_APP = ['biostar.transfer']

INSTALLED_APPS = DEFAULT_APPS + FORUM_APPS + ACCOUNTS_APPS + EMAILER_APP + TRANSFER_APP

DEBUG = True

WSGI_APPLICATION = 'conf.examples.postgres.postgres_wsgi.application'

# The source database containing data from the old version of Biostar.
OLD_DATABASE = os.environ.setdefault("OLD_DATABASE", "old_biostar_db")

# The new database where the data will be copied into.
NEW_DATABASE = os.environ.setdefault("NEW_DATABASE", "database.db")

print(f'NEW_DATABASE={OLD_DATABASE}, OLD_DATABASE={OLD_DATABASE}')

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': NEW_DATABASE,
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },

    'biostar2': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': OLD_DATABASE,
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'TEST': {
            'MIRROR': 'default',
        }
    },
}

try:
    from .postgres_secrets import *
except ImportError as exc:
    print("No postgres_secrets module could be imported")
