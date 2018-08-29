# -*- coding: utf8 -*-
from kombu_example.consumer.async import async
from kombu_example.consumer.consumer import ConsumerRoutes
from kombu_example.consumer.config import config_use

KR = ConsumerRoutes(config_use.get_connection())


@KR.route(exchange_name="55", queue_name="Elizabeth", routing_key="high")
def print_info(body, message):
    print('Elizabeth says: "{0}"'.format(body))
    message.ack()