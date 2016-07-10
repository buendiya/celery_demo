from __future__ import absolute_import
import os

from celery import Celery

from demo.CONFIGS import BROKER_URL

app = Celery('tasks', 
             broker=os.environ.get('celery_demo_broker', BROKER_URL))
app.conf.CELERY_ALWAYS_EAGER = True
