#!/usr/bin/env bash
service nginx start
cd /app && gunicorn -c /etc/gunicorn.conf.py wsgi
