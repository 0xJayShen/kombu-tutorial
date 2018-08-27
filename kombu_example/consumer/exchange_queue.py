# -*- coding: utf8 -*-
from kombu import Exchange, Queue
task_exchange = Exchange("example_exchange",type="topic",durable=True,auto_delete=False)
task_queues = [Queue('hipri', task_exchange, routing_key='hipri'),
               Queue('midpri', task_exchange, routing_key='midpri'),
               Queue('lopri', task_exchange, routing_key='lopri')]