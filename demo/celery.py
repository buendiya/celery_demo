from __future__ import absolute_import

from celery import Celery

from .CONFIGS import BROKER_URL

app = Celery('demo',
             broker=BROKER_URL,
             include=['demo.tasks'])

app.config_from_object('demo.celeryconfig')

