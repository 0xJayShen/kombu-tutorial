# -*- coding: utf8 -*-
class BaseConfig(object):
    pass

class Develope(object):
    Host = 'localhost'
    Port = 5672
    VirtualHost = 'test'
    PassWord = 'guest'
    UserId = 'guest'


config_dict = {"develop":Develope}
config_use = config_dict.get('develop')