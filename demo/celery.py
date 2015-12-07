from __future__ import absolute_import
import os

from celery import Celery

app = Celery('tasks', 
             broker=os.environ.get('celery_demo_broker', "amqp://@amqp"))
app.conf.CELERY_ALWAYS_EAGER = True
