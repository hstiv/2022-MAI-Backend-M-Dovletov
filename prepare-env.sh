#! /bin/sh

# For ubuntu/debian based distributives
echo '===>BEGIN!<==='

sudo apt-get update && sudo apt get upgrade

sudo apt install \
	python3 \
	python3-pip \
	python3-django \
	ca-certificates \
    curl \
    gnupg \
    lsb-release \

echo '===>DONE!<==='



