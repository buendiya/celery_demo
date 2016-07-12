from __future__ import absolute_import

from celery.schedules import crontab

name = 'demo'


CELERYBEAT_SCHEDULE = {
                       'add_task': {'task': '%s.tasks.add' % name,
                                                    'args': (1, 2),
                                                    'schedule': crontab(hour=11, minute=24),
                                                },
                       }

CELERY_TIMEZONE = 'Asia/Shanghai'


CELERY_ALWAYS_EAGER = True