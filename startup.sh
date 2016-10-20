#!/bin/bash

#Start redis
redis-server > /var/log/redis.log &

#Start celery
celery -A statusConsole worker -B > /var/log/celery-statusConsole.log &

#Start gunicorn
./server.sh > /var/log/gunicorn-statusConsole.log &
