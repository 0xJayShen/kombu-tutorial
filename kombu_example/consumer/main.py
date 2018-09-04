# -*- coding: utf8 -*-

from kombu_example.consumer.config import config_use
from kombu_example.consumer.consumer import ConsumerRoutes
import multiprocessing
import os
import threading
if __name__ == '__main__':
    #
    def a():
        KR = ConsumerRoutes(config_use.get_connection(), 2)

        @KR.route(exchange_name="BExchange", queue_name="BQueue", routing_key="b")
        def print_info(body, message):
            print("B线程", threading.currentThread().ident)
            print('B进程', os.getpid(), os.getppid())
            print(threading.active_count())
            message.ack()

        @KR.route(exchange_name="AExchange", queue_name="AQueue", routing_key="a")
        def print_info(body, message):
            print("A线程", threading.currentThread().ident)
            print('A进程', os.getpid(), os.getppid())
            message.ack()

    for i in range(2):
        p = multiprocessing.Process(target=a)
        p.start()
