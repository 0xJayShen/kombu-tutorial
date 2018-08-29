# -*- coding: utf8 -*-
from kombu import Exchange
from kombu.pools import producers
from kombu_example.producter.config import config_use



def send_as_task( exchange_name, args=(), kwargs={}, routing_key=''):
    exchange = Exchange(name=exchange_name, type='topic', durable=True, auto_delete=False)
    payload = {'args': args, 'kwargs': kwargs}
    with producers[config_use.get_connection()].acquire(block=True) as producer:
        producer.publish(body=payload,
                         serializer='json',
                         compression='bzip2',
                         exchange=exchange,
                         declare=[exchange],
                         routing_key=routing_key,
                         retry=True,
                         retry_policy={
                             'interval_start': 0,  # First retry immediately,
                             'interval_step': 2,  # then increase by 2s for every retry.
                             'interval_max': 30,  # but don't exceed 30s between retries.)
                             'max_retries': 30,  # give up after 30 tries.
                         },
                         )
