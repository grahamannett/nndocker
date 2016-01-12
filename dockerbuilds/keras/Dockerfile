FROM grahama/deep:base

MAINTAINER grahama

RUN cd ~ && echo "[global]\ndevice=gpu\nfloatX=float32\n\n[nvcc]\nfastmath=True\n\n[cuda]\nroot=/usr/local/cuda" > .theanorc
