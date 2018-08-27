# -*- coding: utf8 -*-
from kombu_example.consumer.consumer import connection,Worker
if __name__ == '__main__':
    with connection as conn:
        try:
            worker = Worker(conn)
            worker.run()
        except KeyboardInterrupt:
            print('bye bye')