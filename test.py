from __future__ import absolute_import

from demo.tasks import add, retry_demo_task


def test_add():
    add.delay(2,2)


def test_retry():
    retry_demo_task.delay()
    

if __name__ == '__main__':
    test_add()
