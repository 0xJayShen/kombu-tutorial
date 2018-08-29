# -*- coding: utf8 -*-

from kombu_example.consumer.config import config_use
from kombu_example.consumer.consumer import ConsumerRoutes

KR = ConsumerRoutes(config_use.get_connection())

if __name__ == '__main__':
    @KR.route(exchange_name="AExchange", queue_name="AQueue", routing_key="a")
    def print_info(body, message):
        print('body : "{0}"'.format(body))
        message.ack()


    @KR.route(exchange_name="BExchange", queue_name="BQueue", routing_key="b")
    def print_info(body, message):
        print('body : "{0}"'.format(body))

        message.ack()
