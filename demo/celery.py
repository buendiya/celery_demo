from __future__ import absolute_import

import os

from celery import Celery

from .CONFIGS import BROKER_URL

app = Celery('demo', 
             broker=os.environ.get('celery_demo_broker', BROKER_URL),
             include=['demo.tasks'])

app.config_from_object('demo.celeryconfig')

