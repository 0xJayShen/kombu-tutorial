# -*- coding: utf8 -*-

from kombu_example.consumer.consumer import ConsumerRoutes
from kombu_example.consumer.config import config_use

KR = ConsumerRoutes(config_use.get_connection())


@KR.route(exchange_name="55", queue_name="Elizabeth", routing_key="high")
def print_info(body, message):
    print('Elizabeth says: "{0}"'.format(body))
    message.ack()
if __name__ == '__main__':
    @KR.route(exchange_name="55", queue_name="Elizabeth", routing_key="a")
    def print_info(body, message):
        print('Elizabeth says: "{0}"'.format(body))
        message.ack()


    @KR.route(exchange_name="66", queue_name="Elizabeth", routing_key="b")
    def print_info(body, message):
        print('Elizabeth says: "{0}"'.format(body))
        message.ack()