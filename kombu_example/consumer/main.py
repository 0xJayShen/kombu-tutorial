# -*- coding: utf8 -*-

import os
import threading
from kombu_example.consumer.config import config_use
from kombu_example.consumer.consumer import ConsumerRoutes


KR = ConsumerRoutes(config_use.get_connection(), 2)


@KR.route(exchange_name="BExchange", queue_name="BQueue", routing_key="b")
def print_info(body, message):
    print("B线程", threading.currentThread().ident)
    print('B进程', os.getpid(), os.getppid())
    message.ack()

@KR.route(exchange_name="AExchange", queue_name="AQueue", routing_key="a")
def print_info(body, message):
    print("A线程", threading.currentThread().ident)
    print('A进程', os.getpid(), os.getppid())
    message.ack()
