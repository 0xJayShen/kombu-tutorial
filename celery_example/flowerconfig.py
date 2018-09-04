# -*- coding: utf8 -*-
"""
flower启动命令使用的配置文件
"""

address = '0.0.0.0' # 保证外网可以访问
port = 5555

# basic_auth = ['mkd:mkd','artcm:111'] # 用户名：密码

persistent = True # 持久化celery tasks（如果为False的话，重启flower后，监控的tasks全部消失了！）
db = './flowerdb' # 持久化tasks存储的地方
