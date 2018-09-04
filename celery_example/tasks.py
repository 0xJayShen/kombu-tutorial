# -*- coding: utf8 -*-
import os
import sys
import datetime
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from celery import Celery
from celery import chain, group, chord, Task
from celery_example import config
app = Celery()
app.config_from_object(config)


__all__ = ['add', 'reduce','sum_all', 'other']


####################################
# task定义 #
####################################
@app.task
def add(x, y):
    return x + y


@app.task
def reduce(args):
    print(111)
    print(args)
    return args


@app.task
def sum_all(values):
    return sum([int(value) for value in values])


@app.task
def other(x, y):
    return x * y