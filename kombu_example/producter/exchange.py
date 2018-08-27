# -*- coding: utf8 -*-
from kombu import Exchange, Queue
task_exchange = Exchange("example_exchange",type="topic",durable=True,auto_delete=False)