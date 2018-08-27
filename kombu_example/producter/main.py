# -*- coding: utf8 -*-
from kombu import Connection
from kombu_example.producter.sender import send_as_task,connection

if __name__ == '__main__':

    send_as_task(connection,  args=('Kombu',), kwargs={},
             priority='high')
