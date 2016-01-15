FROM nvidia/cuda:cudnn

MAINTAINER grahama

RUN apt-get update && apt-get install -y \
    software-properties-common wget curl python3 python3-dev python3-pip libncurses5-dev libblas-dev liblapack-dev gfortran

WORKDIR root

RUN pip3 install --upgrade setuptools numpy scipy
