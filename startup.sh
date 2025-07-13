#!/bin/sh

git pull

if [ "$?" -ne "0" ]
then
    echo "Error updating project!!!!!"
    exit 1
fi

SESSION_SECRET='123HELLO' gunicorn --bind=0.0.0.0 --timeout 600 "ubroker_web:create_app()"
