from __future__ import absolute_import
import logging

from raven import Client
from raven.contrib.celery import register_signal, register_logger_signal
from raven.handlers.logging import SentryHandler
from celery import Celery as _Celery
from celery.signals import after_setup_task_logger


def add_sentry_handler_to_celery_task_logger(client, sentry_handler_log_level):
    handler = SentryHandler(client)
    handler.setLevel(sentry_handler_log_level)

    def process_task_logger_event(sender, logger, loglevel, logfile, format,
                             colorize, **kw):
        for h in logger.handlers:
            if type(h) == SentryHandler:
                return False
        logger.addHandler(handler)

    after_setup_task_logger.connect(process_task_logger_event, weak=False)


class CeleryWithSentryInit(_Celery):
    """
    using:
    app = CeleryWithSentryInit(main='tasks', 
                 broker=os.environ.get('%s.broker', "amqp://@"),
                 sentry_dsn = os.environ.get('%s.dsn', 'http://'),)

    """
    def __init__(self, sentry_dsn=None, sentry_handler_log_level=logging.ERROR, **kwargs):
        super(CeleryWithSentryInit, self).__init__(**kwargs)
        self.sentry_dsn = sentry_dsn
        self.sentry_handler_log_level = sentry_handler_log_level

    def on_configure(self):
        if self.sentry_dsn:
            client = Client(self.sentry_dsn)

            # register a custom filter to filter out duplicate logs
            register_logger_signal(client)

            # hook into the Celery error handler
            register_signal(client)

            add_sentry_handler_to_celery_task_logger(client, self.sentry_handler_log_level)


