#!/bin/bash

NAME="statusConsole"                             # Name of the application (*)
DJANGODIR=/var/www/statusConsole                 # Django project directory (*)
SOCKFILE=/var/www/sockets/gunicorn.sock        # we will communicate using this unix socket (*)
USER=ubuntu                                  # the user to run as (*)
GROUP=www-data                                 # the group to run as (*)
NUM_WORKERS=3                                  # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=statusConsole.settings    # which settings file should Django use (*)
DJANGO_WSGI_MODULE=statusConsole.wsgi            # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE \
  --reload  &

echo "Server up!"
