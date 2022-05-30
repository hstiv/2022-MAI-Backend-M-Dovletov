FROM ubuntu:20.04

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update
RUN apt install -y python3 python3-pip libpq-dev postgresql 
WORKDIR /usr/src/app
RUN mkdir novels_project
COPY requirements.txt .
RUN pip install -r requirements.txt whitenoise
COPY novels_project novels_project
RUN echo 'from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser("admin", "admin@myproject.com", "112233qq")' | python3 novels_project/manage.py shell ; exit 0