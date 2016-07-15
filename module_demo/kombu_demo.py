# encoding=utf-8

from kombu import Connection


def kombu_connection_test():
    connection = Connection('amqp://jingsz:hello_world@121.41.4.137:5672//')
    connection.connect()
    print connection.connected
    connection.release()

if __name__ == '__main__':
    kombu_connection_test()

