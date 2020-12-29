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

## Install Locally in Edit/Debug Mode
To install turret-soft locally, we're going to use the python setuptools package, which should be installed by default.
Setuptools basically packages python modules/packages so they can be run from the command line as if they were binary installs.
Editor-mode allows you to debug the installation by linking the source code in the repo to the "binary" on your path.

First, make sure you have activated the `turret` conda environment:
```
conda activate turret
```
Next, simply `cd` into the root of this repo (where this readme is) and in a terminal run:
```
pip install -e ./turret-soft
```
The `-e` flag denotes editor mode, and the path `./turret-soft` points pip to the directory containing `setup.py`.

When you install the package, you'll see two new folders appear in `/turret-soft/` which are used for the debug install. They should be grayed out since they are ignored from the git repo (won't be included when you push/pull the repo).

To test that it installed properly, run `turret` in a terminal to check for the expected output. Right now, the turret will just ask "Hellooo?"

### Debug with VSDBG
This is great, but its not really debuggable yet. I've created a package called `vsdbg` that makes debugging installed packages much easier.

First, clone the vsdbg repo to your machine from here: [vsdbg repo](https://github.com/regananalytics/vsdbg).

We can now install this in the same way we installed `turret-soft`. First `cd` into the vsdbg directory, and execute:
```
pip install -e .
```
This will install both vsdbg and vsdbg_ez.

Using vsdbg is actually stupid easy. All we have to do is import it in our code, and vsdbg will start up a debug session that will let us set breakpoints and all that useful debugging stuff.

I like to import vsdbg_ez in our base `__init__.py` file. Go ahead and open `/turret-soft/turret_soft/__init__.py` and add this single line to the top of the blank file:
```
import vsdbg_ez
```
The `ez` version of vsdbg is all we need right now because we don't need anything fancy. When we go to run `turret` from the command line, you'll see nothing happen. The script actually pauses now until we attach a debug session. Go ahead and cancel with `Ctrl-C` or whatever it is on Mac.

Let's attach a debug session.

In VSCode, click the little debug icon on the left side of the screen. Under the "Run and Debug" button you'll see something about creating a launch.json file. Click that.

From the drop down, select `Python`, and then select `Remote Attach`. Hit enter twice to accept `localhost` and `5678` as the debug session address. VSCode automatically creates a remote attach debug json configuration for us. Save and close the json file.

Now lets add a breakpoint. Open the `/turret-soft/turret_soft/__main__.py` file and click to the left of the print line to add a breakpoint.

In your command line, go ahead and execute `turret` again. See how it pauses. Click back into your VSCode window and hit `F5` to start a debug session. Voila! It should now start debugging and stop at the breakpoint we've created! You can use `F5` again to continue, or `F10` to continue line-by-line.

Note: It is imperative that both the VSCode Interpretor and the command line you are using are on the same conda environment, or this will not work!

Just remember to remove the `import vsdbg_ez` from the `__init__.py` file before pushing your code back into the repository. I forget every time, to be honest, so I will create a script to do this automatically down the road.


## Install Docker
Installing docker is different depending on your os. Follow the instructions here:
[Get Docker](https://docs.docker.com/get-docker/)

Also, be sure to complete the post-install instructions. They are essential.
