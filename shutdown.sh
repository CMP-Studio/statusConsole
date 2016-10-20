#!/bin/bash

#Stop server
pkill gunicorn

#Stop celery
pkill celery

#Stop redis
pkill redis
