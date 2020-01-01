---
title: "Cuda Installation Without Installing the Driver"
date: 2019-12-30 00:26:00 +0800
categories: [Nvidia, Cuda]
tags: [Cuda]
---

My Pop! OS comes with stable NVIDIA Stable Driver configuration from Apt and it would be foolish to mess that up with custom driver Installation. One thing I have learned from experience, if there is apt installation possible, do it. Don't try to install it yourself.

So I have this stable proprietary driver from Ubuntu Graphics PPA. So when I install the cuda run file downloaded from the NVIDIA's website, I simply un-check the driver installation. If I keep it checked then I would have stop ligthdm, kdm blah blah, not good. Simply un-check the driver and you will live to see another day.

Next problem is the gcc-version. For some reason only God knows, it doesn't support latest GCC version, and it cries like a little baby if you don't have old GCC version as your default. At the time of writing this article, I was installing cuda-10.2 I needed gcc-7. Fortunately multiple gcc version can co-exist together and don't fight like Kadarshians. So install the right version and you are good to go. If you develop C++ applications often you specify the GCC version while building and I guess it should be fine. I use CLion and I didn't face a problem yet.

After cuda is installed, it will complain that installation is incomplete as you didn't install the driver. Thank NVIDIA for the warning and just ignore the message.

Next thing is to add cuda path to all users. So I edited my /etc/environment file and now it looks something like this:
```bash
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/local/cuda-10.2/bin"
```
See the last cuda path in there? Attaboy!

Also cuda adds cuda-10.2.conf in /etc/ld.so.conf by itself. All you have to do is after cuda installation you have to run the below command:
```bash
sudo ldconfig
```

After this restart your PC. Time to run some simulations and see if our installation is working or not. If you allowed the NVIDIA samples be installed you will get NVIDIA samples in your home folder. Run the below commands:
```bash
cd ~/NVIDIA_CUDA-10.2_Samples/5_Simulations/smokeParticles
make
./smokeParticles
```
You should see a Nice simulation of smoke particles. Congratulate yourself and go to sleep!
