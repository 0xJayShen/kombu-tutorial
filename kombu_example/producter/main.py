# -*- coding: utf8 -*-
from kombu_example.producter.sender import Producer
from kombu_example.producter.config import config_use
import uuid
if __name__ == '__main__':
    producer = Producer(config_use.get_connection())

    producer.send_as_task(exchange_name='AExchange', payload={"info":"do some thing","uuid":str(uuid.uuid1())},
                 routing_key='a')

