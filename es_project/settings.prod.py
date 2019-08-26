try:
    from .base import *  # noqa
except ImportError:
    pass

import raven

CORS_ORIGIN_WHITELIST = (
    '127.0.0.1',
    'localhost'
)

DEBUG = False

# Raven Sentry
RAVEN_CONFIG = {
    'dsn': config('SENTRY_DNS'),
    'release': raven.fetch_git_sha(os.path.abspath(BASE_DIR)),
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        }
    },
    'handlers': {
        'sentry': {
            'level': 'DEBUG',
            'class':
                'raven.contrib.django.raven_compat.handlers.SentryHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'sentry'],
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console', 'sentry'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
