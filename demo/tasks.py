from __future__ import absolute_import

from demo.celery import app
from celery.utils.log import get_task_logger

# @app.task
# class add(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     
#     def __call__(self):
#         print 'hello'
#         print __name__
#         return self.x + self.y

@app.task
def add(x, y):
    print 'hello'
    print __name__
    return x + y
