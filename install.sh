#! /bin/sh

# For ubuntu/debian based distributives
echo '===>BEGIN!<==='

sudo apt-get update && sudo apt-get upgrade

sudo apt install \
	python3 \
	python3-pip \
	ca-certificates \
    curl \
    gnupg \
    lsb-release \
    nginx \
    gunicorn

python3 -m venv env
pip3 install django

# sh /dckr/docker-init.sh

echo '===>DONE!<==='



