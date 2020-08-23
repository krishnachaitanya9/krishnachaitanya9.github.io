---
title: "Liquorix Kernel With Panda"
date: 2020-08-21 00:26:00 +0800
featured-img: panda-logo
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

Panda documentation prefers the kernel to run in option-5. By default the normal kernels run in option-2 or option-1. The liquorix kernel runs in option-4 [Ref (search for Hard Kernel Preemption)](https://liquorix.net/). Now let me rephrase the question asked by the OP nero_valerius. I have a kernel compiled with Option-4 (Liquorix Kernel). Can I run Panda without explicitly building it with Option-5? The answer is Yes. How to do it is explained in Link1.

The next question that can pop into mind: Can I use Liquorix Kernel, patch it with RT patch as suggested in Panda documentation and then build my own Liquorix with RT patch? Well I tried for 2 days and couldn't. There is always an error. One more logical thing to think is that the Liquorix Kernel developers might have developed the fully RT kernel if there was an option but I think there wasn't. So that's why they didn't develop full RT kernel. Else they would. I have tried it for my own sake and I have accepted it that I couldn't. Better people have tried :). 

In the future there is a possibility that RT kernel might be available as is and merged to main master kernel code, but we have to wait till that time. I will count for those days.

The next question is if I have Liquorix Kernel then can the Nvidia Driver be installed and does it work? Well I have and RTX GPU and below is my screenshot that it works.
![Kernel_Screenshot](/assets/img/liquorix_kernel/kernel_screenshot.png)

Now I have to test whether this will work with Panda or not. That's the next step. Thanks!
