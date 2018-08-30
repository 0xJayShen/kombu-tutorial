import pika

# ----------远程连接
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, virtual_host='test', credentials=credentials))
channel1 = connection.channel()
a = connection.channel()
# ------------声明一个exchange,exchange的名字和类型
channel1.exchange_declare(exchange='111',
                          exchange_type='topic',
                          )

# ------------发送消息到exchange
routing_key = "myinfo2"
import json

message = json.dumps({1: 1})

if __name__ == '__main__':
    # a.queue_declare(exclusive=False, queue='myqueue', durable=True
    #               )
    a.basic_publish(
        body=message,
        exchange='111',
        routing_key="",
        properties=pika.BasicProperties(
            delivery_mode=2,  # 队列消息持久化
        )
    )

    connection.close()
