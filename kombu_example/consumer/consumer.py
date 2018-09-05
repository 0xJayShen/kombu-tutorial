from threading import Thread

from kombu import Exchange, Queue
from kombu import pools
from kombu.mixins import ConsumerMixin

connections = pools.Connections(limit=100)


class ConsumerRoutes:
    def __init__(self, connection, thread_num):
        self.connection = connection
        self.thread_num = thread_num
    def route(self, **kwargs):
        def func_wrapper(func):

            self._route(callback=func, **kwargs)
            return func

        return func_wrapper

    def _route(self, exchange_name="", exchange_type="topic", routing_key=None, queue_name=None, callback=None):
        exchange = Exchange(exchange_name, type=exchange_type, durable=True, auto_delete=False)
        queue_name = queue_name or routing_key
        queue = Queue(queue_name, exchange, routing_key=routing_key, durable=True, auto_delete=False)

        # 线程启动任务
        # self._start_worker_thread(queue, callback)
        # t = Thread(target=self._start_worker_thread, args=[queue, callback])
        # print(t)
        # t.start()
        # t.join()
        t_objs = []
        for i in range(self.thread_num):
            t = Thread(target=self._start_worker_thread, args=[queue, callback], daemon=False)
            t.start()
        #     t_objs.append(t)
        # for i in t_objs:
        #     i.join()

    def _start_worker_thread(self, queue, callback):
        with connections[self.connection].acquire(block=True) as conn:
            worker = Worker(conn, queue, callback)
            worker.run()


class Worker(ConsumerMixin):
    def __init__(self, connection, queue, callback):
        self.connection = connection
        self.queues = [queue]
        self.callback = callback

    def get_consumers(self, Consumer, channel):
        return [Consumer(queues=self.queues, callbacks=[self.callback])]
