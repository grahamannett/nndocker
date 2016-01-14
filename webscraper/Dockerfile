FROM ubuntu:latest

MAINTAINER grahama

RUN apt-get update && apt-get install -y wget software-properties-common python3 python3-pip

RUN pip3 install -r requirements.txt

ADD webscraper src/

ADD credentials src/

WORKDIR src/