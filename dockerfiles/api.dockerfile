FROM python:3.8

WORKDIR /usr/src/app

COPY ../ApiApplication/ ./
COPY ../.env ./

RUN pip install wheel setuptools --no-cache-dir
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 5000