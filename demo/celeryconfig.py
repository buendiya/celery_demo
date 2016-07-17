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
        'process_formatter': {
            '()': 'celery.utils.log.ColorFormatter',
            'fmt': "[%(asctime)s: %(levelname)s/%(processName)s] %(message)s"
        },
        'celery_task_formatter': {
            '()': 'celery.app.log.TaskFormatter',
            'fmt': """[%(asctime)s: %(levelname)s/%(processName)s] %(task_name)s[%(task_id)s]: %(message)s"""
        },
    },
    'filters': {
    },
    'handlers': {
        'console': {
            'level': 'INFO',
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
            'formatter': 'celery_task_formatter',
        },
#         'sentry': {
#             'level': 'INFO',
#             'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
#             'formatter': 'celery_task_formatter',
#         },
    },
    'loggers': {
        'django.security': {
            'handlers': ['console', ],
            'level': 'WARNING',
            'propagate': True,
        },
        'common.logger': {
            'handlers': ['debug_log_handler', ],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
