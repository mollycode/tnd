#! /bin/bash

set -e
LOGFILE=/var/log/gunicorn/tnd.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
# user/group to run as
USER=www-data
#GROUP=1
cd /home/edge/virtualenv/tnd/tnd
source ../bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec ../bin/gunicorn_django -w $NUM_WORKERS --user=$USER --log-level=debug \
    --log-file=$LOGFILE 2>>$LOGFILE