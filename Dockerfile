FROM python:3.9.9-slim

ENV SECRET_KEY=django-insecure-xokz#o4hk#ix19yi77rr#&kqj*mnk78z@n61$f)*2omh(6lo&_

ENV DB_HOST=apidb

ENV DB_NAME=base

ENV DB_USER=user

ENV DB_PASSWORD=password

WORKDIR /app

COPY requirements.txt ./

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

RUN chmod 777 wait-for-it.sh

RUN chmod 777 start.sh

EXPOSE 8000