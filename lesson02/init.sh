#!/bin/sh

# Prepare nginx configs before

sudo mkdir /var/www/html/public
sudo touch /var/www/html/public/example.txt
sudo chmod 777 /var/www/html/public/example.txt
echo 'Hello World' > /var/www/html/public/example.txt

gunicorn --workers 2 myapp:app &

curl http://localhost:8080/app/


# Don't foget to kill processes (via 'ps')
