# -*- coding: utf8 -*-
from kombu.pools import producers


priority_to_routing_key = {
    'high': 'hipri',
    'mid': 'midpri',
    'low': 'lopri',
}


def a():
    print(1)

def send_as_task(connection, exchange, args=(), kwargs={}, routing_key=''):
    payload = {'args': args, 'kwargs': kwargs}
    with producers[connection].acquire(block=True) as producer:
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
