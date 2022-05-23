FROM ubuntu:20.04

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update
RUN apt install -y python3 python3-pip
RUN apt install -y postgresql
WORKDIR /usr/src/app
COPY requirements.txt ./novels_project/
RUN pip install -r ./novels_project/requirements.txt
COPY novels_project .
