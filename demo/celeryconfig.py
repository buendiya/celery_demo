from __future__ import absolute_import

from kombu import Exchange, Queue

from .CONFIGS import DEBUG_LOG


CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
)

CELERY_ROUTES = {'demo.tasks.add': {'queue': 'default'},
                 'demo.tasks.retry_task': {'queue': 'default'},}


# CELERY_ALWAYS_EAGER = True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)-8s[%(filename)s:%(lineno)d(%(funcName)s)] %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'debug_log_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': DEBUG_LOG,
            'mode': 'a',
            'maxBytes': 100 * 1024 * 1024,
            'backupCount': 5,
            'encoding': 'utf-8',
            'formatter': 'verbose',
        },
        'sentry': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
    },
    'loggers': {
        'django.security': {
            'handlers': ['console', 'sentry'],  # ['mail_admins', 'sentry'] using sentry to track security  error setup when wsgi starts
            'level': 'WARNING',
            'propagate': True,
        },
        'common.logger': {
            'handlers': ['debug_log_handler', 'sentry'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
