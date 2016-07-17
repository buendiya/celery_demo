from __future__ import absolute_import

from logging.config import dictConfig

from demo.tasks import add, retry_task
from demo.celery import app
from demo.celeryconfig import LOGGING


def test_add():
    add.delay(2,2)


def test_retry():
    retry_task.delay()
    
def get_conf():
    print app.conf

def test_log_config():
    dictConfig(LOGGING)

if __name__ == '__main__':
    test_add()
