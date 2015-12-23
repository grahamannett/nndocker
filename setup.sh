#! /bin/sh

# don't log or write anything by using:
# logfile="/dev/null"
# or touch logfile; logfile="~/logfile"
# and appending to all lines >>$logfile 2>&1
# Made by graham a for softlayer server using nvidia grid k2 gpu to do neural net stuff

# basic setup using 14.04 to create GPU enabled docker containers to train model using Keras, need to setup initial models
echo -e "\033[0;30;42m fresh install \033[0m\033[0;32m\033[0m"

apt-get install -y curl wget git htop vim

################################################################################
# docker stuff
echo -e "\033[0;30;43m installing docker from official script \033[0m\033[0;33m\033[0m"
curl -sSL https://get.docker.com/ | sh

# Docker Compose
wget https://github.com/docker/compose/releases/download/1.5.2/docker-compose-`uname -s`-`uname -m` -O docker-compose
chmod +x docker-compose
mv docker-compose /usr/local/bin/

mkdir tmp && cd $_

################################################################################
# install cuda 7.5
# -------------------
# NOTES:
# Need CORRECT DRIVER, not sure if I need cuda 7.5 thing based on
# https://github.com/NVIDIA/nvidia-docker but for some reason i believe it didnt work without that
# -------------------
# OFFICIAL DOCUMENTATION:
# http://developer.download.nvidia.com/compute/cuda/7.5/Prod/docs/sidebar/CUDA_Quick_Start_Guide.pdf
# http://developer.download.nvidia.com/compute/cuda/7.5/Prod/docs/sidebar/CUDA_Installation_Guide_Linux.pdf
############################
# POSSIBLY MAY NEED:
# sudo apt-get install ubuntu-drivers-common
# sudo ubuntu-drivers autoinstall
# cd /usr/local/cuda/samples/1_Utilities/deviceQuery
# make
# ./deviceQuery
############################
#
echo -e "\033[0;30;43m installing nvidia driver \033[0m\033[0;33m\033[0m"
apt-get install -y software-properties-common
add-apt-repository ppa:graphics-drivers/ppa -y
apt-get install -y nvidia-352 nvidia-settings


echo -e "\033[0;30;43m installing nvidia cuda 7.5 \033[0m\033[0;33m\033[0m"
wget http://developer.download.nvidia.com/compute/cuda/7.5/Prod/local_installers/cuda-repo-ubuntu1404-7-5-local_7.5-18_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1404-7-5-local_7.5-18_amd64.deb
apt-get update && apt-get install -y cuda nvidia-current


################################################################################
# Final Stuff
# -------------------
# symlink nvidia-docker to /usr/local/bin
git clone https://github.com/NVIDIA/nvidia-docker.git
mv nvidia-docker/nvidia-docker /usr/local/bin/
mv

# tmux 2.0
add-apt-repository -y ppa:pi-rho/dev
apt-get update && apt-get install -y tmux

# may need to set up another user aswell so not strictly using root
# adduser graham sudo

echo -e "\033[0;30;42m success \033[0m\033[0;32m\033[0m"