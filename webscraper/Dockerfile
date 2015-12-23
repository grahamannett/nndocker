FROM ubuntu:vivid

MAINTAINER grahama

RUN apt-get update && apt-get install -y wget software-properties-common python3 python3-pip python3-psycopg2

RUN pip3 install youtube-dl google-api-python-client

ADD webscraper src/

ADD credentials src/

WORKDIR src/