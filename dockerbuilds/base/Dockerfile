FROM nvidia/cuda:cudnn

MAINTAINER grahama

RUN apt-get update && apt-get install -y software-properties-common wget curl

RUN add-apt-repository ppa:fkrull/deadsnakes

RUN apt-get update && apt-get install -y python3.5 python3.5-dev libncurses5-dev libblas-dev liblapack-dev gfortran

WORKDIR root

RUN curl https://bootstrap.pypa.io/get-pip.py | python3.5

RUN pip3 install setuptools numpy scipy theano keras --upgrade
