# FROM selects the docker image to start with. In this case, we're starting with the python image which is based on the ubuntu image.
FROM ubuntu:18.04

# Install Audio Stuff
RUN apt update && apt install -y \
    alsa-base \
    alsa-utils \
    pulseaudio \
    python3.8 \
    python3.8-distutils \
    python3.8-dev \
    python3-pip

RUN python3.8 -m pip install -U pip setuptools

# Now we want to COPY over our turret-soft files. 
#This will copy everything from the current folder into the container's /app folder.
COPY . /app

# Now change our working directory to the /app folder
WORKDIR /app

# Install turret-soft.
# No need for editor mode right now. We can play with that later.
RUN pip3 install -e .

# The CMD is the final command for the container.
# The container will execute the CMD and then stop itself once the CMD is complete.
CMD turret


# To Build this image on your machine, cd into this directory and run:
#
#   docker build . -t turret:latest
#
# '.' tells docker the Dockerfile is in this directory
# '-t turret:latest' tells docker to tag this image 'turret:latest'
# turret is the name of the image, latest is the tag

# Once that is complete, run the image with:
#
#   docker run --rm turret:latest
#
# '--rm' tells docker to remove the image after it completes.
# If we hadn't tagged our image we would have to use a weird hash name instead of 'turret:latest'