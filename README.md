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
