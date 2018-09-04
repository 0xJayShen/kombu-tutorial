# -*- coding: utf8 -*-
import datetime
from celery.schedules import crontab
from kombu import Exchange, Queue
BROKER_URL = 'amqp://guest:guest@localhost:5672/shen'
BROKER_POOL_LIMIT = 10 # 默认celery与borker的连接池连接数

# List of modules to import when celery starts.
CELERY_IMPORTS = ('celery_example.tasks', )

# 存储revokes状态(Persistent revokes)
# CELERYD_STATE_DB = './celeryservice/celerymain/celery_revokes_state_db'
####################################
# 默认task结果存储配置 #
# 建议：存储结果会浪费很多资源，业务上非必须的话，不存储结果
####################################
# CELERY_IGNORE_RESULT = True # celery结果忽略
## Using the database to store task state and results.
# CELERY_RESULT_BACKEND = 'mongodb://192.168.1.121:27017/'
# CELERY_MONGODB_BACKEND_SETTINGS = {
#   'database': 'celery_backend',
#   'taskmeta_collection': 'task_result',
#   'max_pool_size':10,
# }
####################################
# 默认频次限制配置 #
# 建议：频次内部实现灰常复杂，最好不要使用
####################################
CELERY_DISABLE_RATE_LIMITS = True # 不使用频次限制
# '1/s'每秒,'1/m'每分钟, '1/h'每小时 (每个task每秒最多执行频次,多出的任务为received状态，等待一段时间后执行，特别注意：这样就有可能导致有的任务会延迟执行)
# CELERY_DEFAULT_RATE_LIMIT = '10000/m'
####################################
# 一般配置 #
####################################
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = True
# CELERY_MESSAGE_COMPRESSION = 'gzip' # 如果发送的tasks参数信息量较大，则使用压缩传输
####################################
# 默认log配置 #
####################################
CELERY_LOG_FILE="./celery.log"
####################################
# routing #
# 需要了解一下rabbitMQ的“队列””交换机“”绑定“的概念：http://simple-is-better.com/news/353
####################################
##### 队列属性定义 ####
# 相当于定义RabbitMQ中的"队列、交换机、绑定"机制（跟celery无关）（可以使用同一个交换机绑定多个队列）
# 没有在CELERY_ROUTES中的task，默认发送到"celery"队列中
CELERY_QUEUES = (
    Queue('queue_add_reduce', exchange=Exchange('calculate_exchange', type='topic', durable=True, auto_delete=False), routing_key='key1'),
    Queue('queue_sum', exchange=Exchange('calculate_exchange', type='topic', durable=True, auto_delete=False), routing_key='key2'),
    Queue('celery', Exchange('celery'), routing_key='celery'), # 里面使用的都是默认参数值
)
CELERY_DEFAULT_QUEUE = 'celery'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_DEFAULT_ROUTING_KEY = 'celery'

###### 路由：taks对应发送的队列及使用的routing_key #####
# delivery_mode参数(决定tasks发送到RabbitMQ后，是否存储到磁盘中)（celery默认使用２：持久化方式）：
# １表示rabbitmq不存储celery发送的tasks到磁盘,RabbitMQ重启后，任务丢失（建议使用这种方式）
# ２表示rabbitmq可以存储celery发送的tasks到磁盘，RabbitMQ重启后，任务不会丢失（磁盘IO资源消耗极大，影响性能）
CELERY_ROUTES = {
    'celery_example.tasks.add': {'queue': 'queue_add_reduce', 'routing_key': 'key1', 'delivery_mode': 1},
    'celery_example.tasks.reduce': {'queue': 'queue_add_reduce', 'routing_key': 'key1', 'delivery_mode': 1},
    'celery_example.tasks.sum_all': {'queue': 'queue_sum', 'routing_key': 'key2', 'delivery_mode': 1},
}