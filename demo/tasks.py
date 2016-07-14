from __future__ import absolute_import

import json
import random

from logging.handlers import RotatingFileHandler

from demo.celery import app
from celery.utils.log import get_task_logger
from .CONFIGS import DEBUG_FILE

logger = get_task_logger(__name__)
file_handler = RotatingFileHandler(DEBUG_FILE)
logger.addHandler(file_handler)


@app.task(bind=True)
def add(self, x, y):
    # logger.info(json.dumps(self.request.__dict__, indent=4))
    logger.info('hello, world')
    return x + y


@app.task(bind=True)
def retry_demo_task(self):
    try:
        random_value = random.randrange(0, 2)
        logger.info('I am coming into retry with %s' % random_value)
        if random_value == 1:
            raise Exception('I am retry Exception')
        logger.info('I have finished retry.')
    except Exception as exc:
        raise self.retry(countdown=1, exc=exc)
