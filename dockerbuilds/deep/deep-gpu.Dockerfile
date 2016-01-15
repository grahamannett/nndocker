FROM grahama/deep:base

MAINTAINER grahama

RUN pip3 install --upgrade theano keras

ENV TENSORFLOW_VERSION 0.6.0

RUN pip --no-cache-dir install \
    https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-${TENSORFLOW_VERSION}-cp27-none-linux_x86_64.whl

RUN cd ~ && echo "[global]\ndevice=gpu\nfloatX=float32\n\n[nvcc]\nfastmath=True\n\n[cuda]\nroot=/usr/local/cuda" > .theanorc

RUN mkdir ~/.keras/ && echo '{"epsilon": 1e-07, "floatx": "float32", "backend": "tensorflow"}' > ~/.keras/keras.json