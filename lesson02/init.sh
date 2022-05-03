#!/bin/sh

# Prepare nginx configs before

# sudo mkdir /var/www/html/public
# sudo touch /var/www/html/public/example.txt
# sudo chmod 777 /var/www/html/public/example.txt
# echo 'Hello World' > /var/www/html/public/example.txt

sudo cp ./conf.d/default /etc/nginx/sites-available/

sudo systemctl restart nginx

gunicorn --workers 2 gcorn:app
