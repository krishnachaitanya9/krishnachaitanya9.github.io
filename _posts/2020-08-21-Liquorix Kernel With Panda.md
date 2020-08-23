---
title: "Liquorix Kernel With Panda"
date: 2020-08-21 00:26:00 +0800
featured-img: franka_panda
categories: [Panda]
tags: [Panda]
---
The problem statement: I want to use Nvidia Graphics card to run an RT (Real Time) kernel along with Nvidia Graphics driver installed which can help me in cuda computing.

According to this [Link1](https://www.franka-community.de/t/nvida-driver-on-rt-kernel-and-alternatives/1319/9) the guy nero_valerius claims that he used Liqourix kernel to run RT kernel for Franka Emika Panda (Panda). Well that's interesting. If you read Panda documentation for real time kernel [Link](https://frankaemika.github.io/docs/installation_linux.html#setting-up-the-real-time-kernel) it says to activate PREEMPT_RT. Now what's PREEMPT_RT?

Basically there are 2 types of RT kernel. One is PREEMPT_RTB and another is PREEMPT_RT_FULL. Panda documentation says to use PREEMPT_RT_FULL. How do I know? Well when you build kernel and see for the configurations you want to build, atleast for kernel versions greater than 5.2 to choose the preemption model we will get those in General Setup -> Preemption Model -> Fully Preemptible Kernel. (Please read my comment at [Link](https://unix.stackexchange.com/questions/582075/trouble-selecting-fully-preemptible-kernel-real-time-when-configuring-compil?newreg=b80e2082d0624298a5c37588f66e4817)) Below are the options we can see:

Preemption Model
    1. No Forced Preemption (Server) (PREEMPT_NONE)
    2. Voluntary Kernel Preemption (Desktop) (PREEMPT_VOLUNTARY)
    3. Preemptible Kernel (Low-Latency Desktop) (PREEMPT__LL) (NEW)
    4. Preemptible Kernel (Basic RT) (PREEMPT_RTB) (NEW)
    > 5. Fully Preemptible Kernel (RT) (PREEMPT_RT_FULL) (NEW)

Panda documentation prefers the kernel to run in option-5. By default the normal kernels run in option-2 or option-1. The liquorix kernel runs in option-3 [Ref (search for Hard Kernel Preemption)](https://liquorix.net/). Now let me rephrase the question asked by the OP nero_valerius. I have a kernel compiled with Option-4 (Liquorix Kernel). Can I run Panda without explicitly building it with Option-5? The answer is Yes. How to do it is explained in Link1.

The next question that can pop into mind: Can I use Liquorix Kernel, patch it with RT patch as suggested in Panda documentation and then build my own Liquorix with RT patch? Well I tried for 2 days and couldn't. There is always an error. One more logical thing to think is that the Liquorix Kernel developers might have developed the fully RT kernel if there was an option but I think there wasn't. So that's why they didn't develop full RT kernel. Else they would. I have tried it for my own sake and I have accepted it that I couldn't. Better people have tried :) 

In the future there is a possibility that RT kernel might be available as is and merged to main master kernel code, but we have to wait till that time. I will count for those days.

The next question is if I have Liquorix Kernel then can the Nvidia Driver be installed and does it work? Well I have and RTX GPU and below is my screenshot that it works.
![Kernel_Screenshot](/assets/img/liquorix_kernel/kernel_screenshot.png)

Next we have a compiled kernel. How do we know which option in above 5 options is it set? We can get answer from 2 commands. First:
```bash
py-2.7.17 pop-os in ~
○ → uname -v
#1 ZEN SMP PREEMPT liquorix 5.7-21ubuntu1~bionic (2020-08-19)
```
Now the RT kernel shows up as SMP PREMPT RT. The above command is just showing that it is SMP PREMPT. To dig more we move into the next command:
```bash
atom /boot/config-$(uname -r)
```
In the text editor you will find below lines:
```
# CONFIG_PREEMPT_NONE is not set
# CONFIG_PREEMPT_VOLUNTARY is not set
CONFIG_PREEMPT=y
CONFIG_PREEMPT_COUNT=y
CONFIG_PREEMPTION=y
```
According to this [link](https://rt.wiki.kernel.org/index.php/Frequently_Asked_Questions#How_does_the_CONFIG_PREEMPT_RT_patch_work.3F) you should have below lines if it's an RT kernel:
```
CONFIG_PREEMPT=y
CONFIG_PREEMPT_RT_BASE=y
CONFIG_PREEMPT_RT_FULL=y
```
We don't have CONFIG_PREEMPT_RT_BASE or CONFIG_PREEMPT_RT_FULL set to y. So MAYBE we can assume that it's compiled in Option-3. How do I know? Test it something like this:

Take any kernel, any version for that matter, download the exact version RT patch, then patch the kernel with RT patch, then go into the kernel source code and type the following
```bash
make nconfig
```
Navigate to the PREEMPT settings (It would be in General Setup -> Preemption Model -> Fully Preemptible Kernel as suggested previously in this post) then if you select Preemptible Kernel (Basic RT) then settings would be something like
```
CONFIG_PREEMPT_RT_BASE=y
# Not set CONFIG_PREEMPT_RT_FULL
```
If you select Fully Preemptible Kernel (RT) then the settings would look something like this:
```
CONFIG_PREEMPT=y
CONFIG_PREEMPT_RT_BASE=y
CONFIG_PREEMPT_RT_FULL=y
```
That's why by default the liquorix kernel is compiled with Option-3 {Preemptible Kernel (Low-Latency Desktop) (PREEMPT__LL)}.

Now I have to test whether this will work with Panda or not. That's the next step. Thanks!
