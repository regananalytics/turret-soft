FROM python:3-buster

RUN apt-get update && apt-get install -y \
    alsa-base \
    alsa-utils \
    pulseaudio

CMD aplay /usr/share/sounds/alsa/Front_Center.wav

