from __future__ import absolute_import

from kombu import Exchange, Queue

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
)

CELERY_ROUTES = {'demo.tasks.add': {'queue': 'default'},
                 'demo.tasks.retry_task': {'queue': 'default'},}


# CELERY_ALWAYS_EAGER = True
