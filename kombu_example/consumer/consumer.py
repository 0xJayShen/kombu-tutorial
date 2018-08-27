# -*- coding: utf8 -*-
from kombu.mixins import ConsumerMixin
from kombu_example.consumer.exchange_queue import  task_queues
from  kombu_example.consumer.callback import do_something
class Worker(ConsumerMixin):

    def __init__(self, connection):
        self.connection = connection

    def get_consumers(self, Consumer, channel):
        return [Consumer(queues=task_queues,
                         accept=['pickle','json'],
                         callbacks=[self.process_task])]

    def process_task(self, body, message):
        args = body['args']
        kwargs = body['kwargs']

        try:
            do_something(*args, **kwargs)
        except Exception as exc:
           print('task raised exception: %r', exc)
        message.ack()

from kombu import Connection
from kombu_example.consumer.config import config_use as  use
connection = Connection(host=use.Host, port=use.Port, virtual_host=use.VirtualHost, password=use.PassWord,
                            userid=use.UserId)
