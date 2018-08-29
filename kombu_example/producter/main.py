# -*- coding: utf8 -*-
from kombu_example.producter.sender import Producer
from kombu_example.producter.config import config_use

if __name__ == '__main__':
    producer = Producer(config_use.get_connection())
    producer.send_as_task(exchange_name='55', args=('d',), kwargs={3: 1},
                 routing_key='a')
    producer.send_as_task(exchange_name='66',  args=('d',), kwargs={3:1},
                 routing_key='b')


