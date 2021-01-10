FROM ubuntu:20.04

ARG PYTHON_VERSION_TAG=3.9.1
ARG LINK_PYTHON_TO_PYTHON3=1

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        alsa-base \
        alsa-utils \
        bash-completion \
        build-essential \
        curl \
        gcc \
        g++ \
        git \
        make \
        nano \
        pulseaudio \
        python3 \
        python3-pip \
        wget \
        sudo \
        tree

RUN touch .bashrc && echo "alias python=python3" >> .bashrc

CMD aplay /usr/share/sounds/alsa/Front_Center.wav

