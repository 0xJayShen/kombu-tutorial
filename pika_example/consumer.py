import pika
import sys
import time
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, virtual_host='test', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='111',
                         exchange_type='topic')
#创建一个名字叫muqueue的队列,用来投递消息
#durable = True队列持久化
#exclusive=False 是否排外的，有两个作用，一：当连接关闭时connection.close()该队列是否会自动删除；
# 二：该队列是否是私有的private，如果不是排外的，可以使用两个消费者都访问同
# 一个队列，没有任何问题，如果是排外的，会对当前队列加锁，其他通道channel是不能访问的，如果强制访问会报异常
result = channel.queue_declare(exclusive=False,queue='myqueue',durable = True
                               )
queue_name = result.method.queue
#队列绑定exchange
channel.queue_bind(exchange='111',queue=queue_name,routing_key="aa.*")

import json
def callback(ch, method, properties, body):
    print(json.loads(body.decode('utf-8')))
    time.sleep(2)
    ch.basic_ack(delivery_tag=method.delivery_tag)

#，再同一时刻，不要发送超过1条消息给一个工作者（worker)公平调度
channel.basic_qos(prefetch_count = 3 )
channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=False)

if __name__ == '__main__':

    channel.start_consuming()