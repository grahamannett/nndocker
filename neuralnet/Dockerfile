FROM nvidia/cuda

MAINTAINER grahama

RUN apt-get update && apt-get install -y wget python3-dev python3-numpy python3-scipy python3-pip

RUN pip3 install -r requirements.txt

RUN cd ~ && echo "[global]\ndevice=gpu0\nfloatX=float32\n\n[cuda]\nroot=/usr/local/cuda" > .theanorc