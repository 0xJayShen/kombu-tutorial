# -*- coding: utf8 -*-
from kombu import Connection
from kombu_example.producter.sender import send_as_task
from kombu_example.producter.config import config_use
from kombu_example.producter.create_exchange import create_exchange

if __name__ == '__main__':
    task_exchange = create_exchange(name="44")
    connection = config_use.get_connection()
    send_as_task(connection,task_exchange,  args=('Kombu',), kwargs={},
                 routing_key='high')

