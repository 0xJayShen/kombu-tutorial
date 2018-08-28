# -*- coding: utf8 -*-


if __name__ == '__main__':

    from kombu_example.consumer.consumer import KombuRoutes

    KR = KombuRoutes()
    @KR.route(exchange_name="44", queue_name="Elizabeth", routing_key="high")
    def print_info(body, message):
        print('Elizabeth says: "{0}"'.format(body))
        message.ack()
    # import time
    # time.sleep(30)