#!/bin/bash

#Start redis
redis-server > /var/log/redis.log &

#Start celery
celery -A statusConsole worker -B &

#Start gnuicorn
./server.sh
