#!/bin/bash

#Start redis
redis-server > /var/log/redis.log &

#Start celery
celery -A statusConsole worker -B > /var/log/celery-statusConsole.log &

#Start gnuicorn
./server.sh > /var/log/gnuicorn-statusConsole.log &
