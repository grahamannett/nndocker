# Neural Niche Docker Config

![Layout of Current Dockerized Plan](other/layout.png)

## Docker Container Setup
### GPU/nvidia official stuff
Using the official Nvidia Dockerfile:
https://github.com/nvidia/nvidia-docker
Official Documentation:
http://developer.download.nvidia.com/compute/cuda/7.5/Prod/docs/sidebar/CUDA_Quick_Start_Guide.pdf
Cuda Downloads:
https://developer.nvidia.com/cuda-downloads


setup nvidia-docker plugin

git clone https://github.com/NVIDIA/nvidia-docker


NOT SURE IF BELOW STILL IS TRUE:

## Using nvidia-docker

Updated 1/14 since they (nvidia) changed things around.
```
git clone https://github.com/NVIDIA/nvidia-docker
cd nvidia-docker && make install
nvidia-docker volume setup
# you may need to symlink nvidia-docker into /usr/local/bin/nvidia-docker (cant remember)
```

with tmux start nvidia-docker-plugin in one pane and then using NV_GPU='0,1' nvidia-docker run you can bind and use gpu with theano/keras (assuming you specify to use gpu in theanorc or something similar)

<!-- (cant remember exactly) cd tools && make install -->


- https://hub.docker.com/r/nvidia/cuda/

## building/running docker images

#### breakdown of Dockerfiles

Using just python 3.4 at the moment
base image is based off of nvidia/cuda:cudnn but has theano, keras already (will move to grahama/deep:keras later)

#### building

to build:
docker build -t grahama/deep:base dockerbuilds/base

#### running containers w/ gpu

the way to run it is then (for instance with interactive and mounted volume):
NV_GPU='0,1' nvidia-docker run -it -v $PWD/datafolder:/root/data grahama/deep:base



## Scraping YouTube
https://developers.google.com/youtube/v3/code_samples/python#search_by_keyword
https://developers.google.com/youtube/v3/docs/search/list


## PostgresSQL DB

main table:
videoid     string
title       string
subs/cc     bool

subs table:
videoid     string
ifsubs      string



# Coordinating App with Docker Compose

Because the app requires multiple parts

## Docker-Compose Links:
https://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/
https://docs.docker.com/compose/compose-file/#links
https://docs.docker.com/compose/extends/


# Helpful Docker stuff

## Stop and Remove all docker containers
sudo docker stop $(sudo docker ps -a -q)
sudo docker rm $(sudo docker ps -a -q)

