# -*- coding: utf8 -*-
from celery_example import tasks
tasks.reduce.delay(1)
print(tasks.reduce.delay(1,))