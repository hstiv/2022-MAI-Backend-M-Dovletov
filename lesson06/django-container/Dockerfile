FROM ubuntu:20.04
RUN apt update
RUN apt install -y python3 pip
RUN apt install -y postgresql
WORKDIR /usr/src/app
COPY requirements.txt /novels_project/
RUN pip install -r requirements.txt
COPY novels_project .