from __future__ import absolute_import

from demo.tasks import add

if __name__ == '__main__':
    print add.delay(1,2)
