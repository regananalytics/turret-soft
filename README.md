# turret-soft
Operating Software and resources for an Automated Nerf Turret


# Resources
## Hardware
[Jetson Nano *OWNED*](https://developer.nvidia.com/embedded/jetson-nano-developer-kit)

I already own one of these. They have a built in GPU and they run ubuntu linux.
Using NVIDIA's Jetpack SDK we can even stream video, display a cool targeting UI, etc.

## Software
[This Repo](https://github.com/regananalytics/turret-soft)

We can write the operating system in python and deploy it via docker/kubernetes so we can update it remotely.

[Tensorflow](https://www.tensorflow.org/)

Tensorflow is my preferred ML framework, and we can just use a prebuilt model for object detection (OD).
Tracking can be done natively in python using a kalman tracker or something simpler.

## Extras
[Wiki of Portal Turret Sounds](https://theportalwiki.com/wiki/Turret_voice_lines)

We should totally have these sounds play whenever things happen.
I have copied most of these into categories in the `/audio` directory.


# Development Installation
This project uses git for source control and github to host the repo.

To download the repo, you will first need to install git:
[Mac](https://git-scm.com/download/mac), [Windows](https://git-scm.com/download/win), [Linux](https://git-scm.com/download/linux)

You can then clone the repo by running this command in a terminal 
```
git clone https://github.com/regananalytics/turret-soft.git
```

There are a number of ways to install Python, but I only use [anaconda](https://docs.anaconda.com/anaconda/install/)

Anaconda allows you to create python environments using Conda. In a terminal, you can create a new one by running:

```
conda create -n turret tensorflow [or tensorflow-gpu, but not on Mac]
```
Which creates a new python environment with TF installed named turret. You can then activate it with
```
conda activate turret
```


### Set up VS Code

I prefer VSCode as an IDE, and it integrates really well into git and github:
[Mac, Linux, Windows](https://code.visualstudio.com/download)

Git is built into VSCode's source control. Once you open the repo folder in VSCode, it should automatically recognize it as a git repository.

To activate the right conda environment for this project, you can select the python interpretor for the project. With the project open, you should see `Python 3.X.X 64-bit` in the lower left of the window (usually in blue). Click this text to get a dropdown of interpretors. Select your new `Python 3.X.X 64-bit ('turret': conda)` interpretor. If by chance it does not appear, exit out of vscode and open it again. It sometimes takes one or two restarts until it detects new conda envs.

To make sure tensorflow is installed correctly, I have included a `/test/test_tf.py` file which should run to completion.

As you start working with Python, you will get little pop-ups that ask if you want to install a linter, extensions, etc. These are all good and you should install them. If it asks whether to install through pip or conda, you can pick either. I usually use conda but it totally doesn't matter.

