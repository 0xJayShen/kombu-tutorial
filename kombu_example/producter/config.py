# -*- coding: utf8 -*-
from kombu import Connection


class BaseConfig(object):

    @classmethod
    def get_connection(cls):
        connection = Connection(host=cls.Host, port=cls.Port, virtual_host=cls.VirtualHost, password=cls.PassWord,
                                userid=cls.UserId)
        return connection

class Develope(BaseConfig):
    Host = 'localhost'
    Port = 5672
    VirtualHost = 'test'
    PassWord = 'guest'
    UserId = 'guest'






config_dict = {"develop": Develope}
config_use = config_dict.get('develop')
