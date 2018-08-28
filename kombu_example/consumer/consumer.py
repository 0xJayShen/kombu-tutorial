import logging
from threading import Thread
from time import sleep

from kombu import  Exchange, Queue
from kombu.mixins import ConsumerMixin
from kombu import pools
connections = pools.Connections(limit=100)
LOG = logging.getLogger(__name__)


class KombuRoutes:

    def route(self,*args,  **kwargs):
        def func_wrapper(func):
            self._route(callback=func, **kwargs)
            return func

        return func_wrapper

    def _route(self, exchange_name="", exchange_type="topic", routing_key=None, queue_name=None, callback=None):
        exchange = Exchange(exchange_name, type=exchange_type,durable=True,auto_delete=False)
        queue_name = queue_name or routing_key
        queue = Queue(queue_name, exchange, routing_key=routing_key,durable=True,auto_delete=False)

        # 线程启动任务
        t = Thread(target=self._start_worker_thread, args=[queue, callback])
        print(t)
        t.start()

    def _start_worker_thread(self,  queue, callback):
        from kombu_example.consumer.config import config_use
        connection = config_use.get_connection()
        with connections[connection].acquire(block=True) as conn:
            worker = Worker(conn, queue, callback)
            print(queue)
            worker.run()


class Worker(ConsumerMixin):
    def __init__(self, connection, queue, callback):
        self.connection = connection
        self.queues = [queue]
        self.callback = callback

    def get_consumers(self, Consumer, channel):
        return [Consumer(queues=self.queues, callbacks=[self.callback])]