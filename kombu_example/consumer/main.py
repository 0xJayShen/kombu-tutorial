# -*- coding: utf8 -*-

from kombu_example.consumer.config import config_use
from kombu_example.consumer.consumer import ConsumerRoutes
from kombu_example.producter.sender import Producer

KR = ConsumerRoutes(config_use.get_connection(), 2)
producer = Producer(config_use.get_connection())

if __name__ == '__main__':

    @KR.route(exchange_name="AExchange", queue_name="AQueue", routing_key="a")
    def print_info(body, message):
        print('接收方监听--------', body)
        reply = {"info": "success","uuid":body.get("uuid")}
        #监听之后要在callback里再往exchange里发消息
        producer.send_as_task(exchange_name='AExchange', payload=reply,
                              routing_key='a.reply')
        message.ack()


    @KR.route(exchange_name="AExchange", queue_name="AQueue.reply", routing_key="a.reply")
    def print_info(body, message):
        print('监听reply--------', body)

        message.ack()
