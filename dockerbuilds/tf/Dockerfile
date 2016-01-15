FROM nvidia/cuda:7.0-cudnn2-devel

MAINTAINER grahama

RUN apt-get update && apt-get install -y \
    software-properties-common wget curl python3 python3-dev python3-pip libncurses5-dev libblas-dev liblapack-dev gfortran

WORKDIR root

RUN pip3 install --upgrade setuptools numpy scipy

RUN pip3 install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.6.0-cp34-none-linux_x86_64.whl

RUN pip3 install --upgrade keras

RUN mkdir ~/.keras/ && echo '{"epsilon": 1e-07, "floatx": "float32", "backend": "theano"}' > ~/.keras/keras.json
