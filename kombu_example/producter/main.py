# -*- coding: utf8 -*-
from kombu import Connection
from kombu_example.producter.sender import send_as_task
if __name__ == '__main__':
    send_as_task(exchange_name='55', args=('d',), kwargs={3: 1},
                 routing_key='a')
    send_as_task(exchange_name='66',  args=('d',), kwargs={3:1},
                 routing_key='b')

