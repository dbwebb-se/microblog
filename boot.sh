#!/bin/sh

source .venv/bin/activate
sleep 5
while true; do
    flask db upgrade 2>&1

    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Upgrade command failed, retrying in 5 secs...
    echo YEst
    sleep 5
done
exec gunicorn -b :5000 --access-logfile - --error-logfile - microblog:app