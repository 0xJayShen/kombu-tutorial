# -*- coding: utf8 -*-
from kombu.pools import producers
from kombu import Connection
from kombu_example.producter.exchange import task_exchange

priority_to_routing_key = {
    'high': 'hipri',
    'mid': 'midpri',
    'low': 'lopri',
}


def send_as_task(connection,  args=(), kwargs={}, priority='mid'):
    payload = { 'args': args, 'kwargs': kwargs}
    routing_key = priority_to_routing_key[priority]
    with producers[connection].acquire(block=True) as producer:
        producer.publish(payload,
                         serializer='pickle',
                         compression='bzip2',
                         exchange=task_exchange,
                         declare=[task_exchange],
                         routing_key=routing_key)


from kombu_example.producter.config import config_use as  use

connection = Connection(host=use.Host, port=use.Port, virtual_host=use.VirtualHost, password=use.PassWord,
                        userid=use.UserId)
