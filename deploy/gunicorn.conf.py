#!/usr/bin/env python
#
#  Copyright (C) 2019 Tieto Czech s.r.o.
#  Lumir Jasiok
#  lumir.jasiok@tieto.com
#  http://www.tieto.com
#
#
#

# file gunicorn.conf.py
# coding=utf-8
# Reference: https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py
import os
import multiprocessing

loglevel = 'debug'
# errorlog = os.path.join(_VAR, 'log/api-error.log')
# accesslog = os.path.join(_VAR, 'log/api-access.log')
errorlog = "/tmp/gunicorn-error.log"
accesslog = "/tmp/gunicorn-access.log"

# bind = 'unix:%s' % os.path.join(_VAR, 'run/gunicorn.sock')
bind = 'unix:/app/app.sock'
#bind = '127.0.0.1:5001'
# workers = 3
workers = multiprocessing.cpu_count() * 2 + 1

timeout = 3 * 60  # 3 minutes
keepalive = 24 * 60 * 60  # 1 day

capture_output = True
