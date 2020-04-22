# -*- coding:utf-8 -*-
# gunicorn启动配置文件
import os
import gevent.monkey
gevent.monkey.patch_all()

import multiprocessing

# debug = True
loglevel = 'debug'
bind = "0.0.0.0:18080"
pidfile = "log/gunicorn.pid"
accesslog = "log/access.log"
errorlog = "log/debug.log"
daemon = True

# 启动的进程数
workers =  multiprocessing.cpu_count()/20 if multiprocessing.cpu_count() > 20 else 1;
worker_class = 'gevent'
