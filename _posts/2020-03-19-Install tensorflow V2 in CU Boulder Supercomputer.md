---
title: "Install TensorFlow V2 in Supercomputer"
date: 2020-03-19 00:26:00 +0800
categories: [tensorflow]
tags: [tensorflow]
---

So first I did was load whatever modules were available to me to kickstart. The specific part of the module spider command I was interested in is:

```bash
$ module spider

...
  cuda: cuda/7.5.18, cuda/8.0.61, cuda/9.0.176, cuda/9.1.85, cuda/10.1
    CUDA compiler and libraries

  cudnn: cudnn/4.0, cudnn/5.1, cudnn/7.1
    GPU Accelerated Deep Learning
...
```

Now you see I can load cuda 10.1 and cudnn 7.1. Are those compatible? Let's check.  If you go to https://developer.nvidia.com/rdp/cudnn-archive you will find that cudnn 7.1 is for cuda 9. Won't be compatible. 

Now we have only option to load cuda10.1 from module load. Good!

Let's see what are the dependencies of TensorFlowV2. According to this link: https://www.tensorflow.org/install/gpu#software_requirements you need

- Nvidia GPU Drivers (In case of supercomputer, you don't really need to care, they are managed)
- CUDA Toolkit (Can be obtained from module load)
- cuDNN (Need to Install)
- TensorRT (Need to Install)

So let's get started. Download cuDNN for cuda 10.1 from here: https://developer.nvidia.com/rdp/cudnn-download. I downloaded cuDNN v7.6.5 for cuda 10.1 from the option "cuDNN Library for Linux". Next unpack it using the command: 

```bash
tar -xvf cudnn-10.1-linux-x64-v7.6.5.32.tgz
mv cuda cudnn
```

keep in mind the filenames might change in your case. I renamed the extracted folder from cuda to cudnn so that I know.

As I extracted to some folder, now I need to set environment variables as explained in the documentation:

So when I module load cuda, it's stored for me in 

```bash
/curc/sw/cuda/10.1/
```

I found it using "which nvcc". Now I can set environment variables just as explained in this medium guide: https://medium.com/@danielwzou/installing-cudnn-on-a-remote-shared-machine-without-sudo-or-root-privileges-855228db7d25

Now I need to download TensorRT. To download it I went to this and downloaded TensorRT V6 because TensorRT V7 wasn't in compatible list

To install TensorRT locally you need to follow the tutorial: https://docs.nvidia.com/deeplearning/sdk/tensorrt-install-guide/index.html

