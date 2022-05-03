#!/bin/sh

sudo cp ./conf.d/default /etc/nginx/sites-available/

sh ./app/runapp.sh &

sudo systemctl restart nginx

gunicorn --workers 2 gcorn:app
