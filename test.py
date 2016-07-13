from __future__ import absolute_import

from demo.tasks import add

if __name__ == '__main__':
    add.delay(2,2)
