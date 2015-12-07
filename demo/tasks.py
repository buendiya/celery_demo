from __future__ import absolute_import

from demo.celery import app
from celery.utils.log import get_task_logger

@app.task
def add(x, y):
    print 'hello'
    print __name__
    return x + y
