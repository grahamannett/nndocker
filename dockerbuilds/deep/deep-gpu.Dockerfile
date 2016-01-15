FROM grahama/deep:base

MAINTAINER grahama

RUN pip3 install --upgrade theano keras

ENV TENSORFLOW_VERSION 0.6.0

RUN pip3 install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.6.0-cp34-none-linux_x86_64.whl

# for Theano use this and change  "backend": "tensorflow" to theano:
RUN cd ~ && echo "[global]\ndevice=gpu\nfloatX=float32\n\n[nvcc]\nfastmath=True\n\n[cuda]\nroot=/usr/local/cuda" > .theanorc


# RUN mkdir ~/.keras/ && echo '{"epsilon": 1e-07, "floatx": "float32", "backend": "theano"}' > ~/.keras/keras.json