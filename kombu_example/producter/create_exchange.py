# -*- coding: utf8 -*-
from kombu import Exchange
def create_exchange(name='',type='topic',durable=True,auto_delete=False):
    exchange =  Exchange(name=name,type=type,durable=durable,auto_delete=auto_delete)
    return exchange