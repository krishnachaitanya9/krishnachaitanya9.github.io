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

Next I have to make a conda environment. Let's do that first. CU has made an excellent tutorial on Github and I will be following that

https://github.com/ResearchComputing/Anaconda_Tutorial_Fall_2019

Next it will be useful to create conda environment at a particular location so that you don't run out of space. So the command I executed is:

```bash
source /curc/sw/anaconda3/latest # Activating conda base, so that shell recognizes conda commands
conda create -p /projects/koch3328/software/py3.7_gpu python=3.7 # Creating conda environment
conda activate /projects/koch3328/software/py3.7_gpu # Activating newly created environment
```

The install tensorflow GPU

```bash
module load gcc/8.2.0
conda install -c anaconda tensorflow-gpu
```

Now finally as we installed everything into custom folder, I made this small script to source all environment variables from:

```bash
#!/bin/bash
export PATH=/curc/sw/cuda/10.1/bin:$PATH
export PATH=$PATH:/projects/koch3328/software/TensorRT/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/curc/sw/cuda/10.1/lib64:/projects/koch3328/software/cudnn/lib64
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/projects/koch3328/software/TensorRT/lib
export CUDA_HOME=/curc/sw/cuda/10.1
export CUDA_INSTALL_DIR=$CUDA_HOME
export CUDNN_INSTALL_DIR=/projects/koch3328/software/cudnn
export CPATH=$CPATH:/curc/sw/cuda/10.1/include:/projects/koch3328/software/TensorRT/include:/projects/koch3328/software/cudnn/include
export CFLAGS="-I$CUDA_HOME/include $CFLAGS"
export LDFLAGS="$LDFLAGS -lm"
#export CUDA_HOME=$CUDA_HOME:/projects/koch3328/software/cudnn:/projects/koch3328/software/TensorRT

```

Now when you run the slurm script use this template:

```bash
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=23:59:00
#SBATCH --qos=normal
#SBATCH --partition=sgpu
#SBATCH --ntasks=1
#SBATCH --job-name=sgpu_ml_project
#SBATCH --output=ml_final_project.%j.out
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=koch3328@colorado.edu
module purge
module load python/3.6.5
module load gcc/8.2.0
module load cuda/10.1
source /curc/sw/anaconda3/2019.03/bin/activate
source /home/koch3328/set_environment_variables.sh
conda activate /projects/koch3328/software/py3.7_gpu
python --version
echo "training --"
cd /scratch/summit/koch3328/deep_learning
python test_tf_gpu.py
echo "Finished"

```

Where test_tf_gpu.py contains the following code:

```python
import tensorflow as tf

if __name__ == "__main__":
    if tf.test.gpu_device_name():
        print('Default GPU Device:{}'.format(tf.test.gpu_device_name()))
    else:
        print("Please install GPU version of TF")
```

Which printed out that infact I was using GPU. That's the way I setup running my GAN models in GPU.













































 