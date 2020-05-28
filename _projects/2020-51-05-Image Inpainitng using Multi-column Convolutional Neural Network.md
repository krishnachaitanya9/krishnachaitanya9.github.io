---
layout: post
title: "Image Inpainitng using Multi-column Convolutional Neural Network"
date: 2020-05-05 00:26:00 +0800
featured-img: CNN-logo
categories: [DeepLearning]
tags: [DeepLearning]
---
Image inpainting is a technique to generate or estimate suitable pixel-level information to fill a missing section of an image. It is useful in many applications like image restoration, image denoising or object removal etc. It may
sound an easy task but generating missing pieces of an image and make it look realistic is a challenging problem. Generating a realistic image will require a higher level understanding of various features of the image and low level
detailing to perfectly match it with the surroundings in terms of color and texture.

The proposed network Generative Multi-column Convolutional Neural Network (GMCNN) in the original paper shown in Figure 2, primarily consists of three sub-networks: a generator network to produce the results, local and global discriminators for adversarial training and a pre-trained VGG network for ID-MRF loss calculation. Only the generator network is used while testing the network. The generator network has three parallel encoder-decoder branches to extract the various level of feature information from input image X and applied mask M. Then a decoder module common to all three branches is used to transform these features into the original image space Yˆ . The multiple branches with different levels of configurations are useful to capture a different level of information from an image. The generator network is trained to generate optimal feature representations using the provided data. The output of each branch is up-sampled and concatenated into a feature map F. The feature map F is further transformed into image space using the shared decoding module having two convolutional layers. This decoding module is denoted by d(·) provides the output Yˆ of the generator network as Yˆ = d(F). Minimizing the loss between this output Yˆ and original image Y make these branches capture the required information from the input. The decoding module d(·) influences the generate features in each of the branches in the training phase.

The original reference architecture from the paper has been adopted with some changes. Two types of attention mechanisms have been tested. One is using Squeeze-and-Excitation mechanism in Fig 4 and the other is with A2 double attention networks in Fig 3. Both of the methods yield relatively same results.

When both of the architectures in 3 and 4 are compared, just using  squeeze-and-Excitation block as in Fig 4 slightly outperforms the A2 double attention networks. The reason for including the attention mechanism originates from
[15] where the authors have noted that attention mechanism helps in generating  etter inpainting results. Finally the table 1 shows improved Peak Signal to Noise Ratio (PSNR) numbers in architectures where the attention mechanism has been added.

Squeeze and Excitation Attention is a creative attention mechanism where first for each layer(original tensor) a
global pooling is taken. This outputs a tensor whose shape is equal to number of layers. This tensor is then excited
by an activation function. Activation function can be chosen from a range of activation functions like sigmoid, tanh
etc. Lets call this intermediate tensor. This output is then multiplied to original layer on which pooling was applied.
The result is a hybrid output with same tensor shape as original tensor. As global pooling is done here the output
tensor has a context of whole image. As the intermediate tensor is learned by the model, and the intermediate tensor
is basically a weight multiplied to original tensor, less important layers have low weight and more important layers
have more weight.

In this attention mechanism there are two blocks. One feature gathering and the other feature distribution. Feature
gathering block is usually placed at the start of the context encoder. Feature Distribution is usually placed at the end
of context decoder. In this way this mechanism ensures that important features are identified and disseminated.

Usually, in a context encoder, the middle layers (feature Space) are dense layers as mentioned in [10]. But this
causes a lot of features to be lost in the feature space. One solution to this is to add multiple dilated convolution
layers in place of dense layers to keep the feature space rich [16]. Hence there are many dilated convolution layers
in the middle of all three parallel context encoder-decoders in our architectures.
The reason we think the architecture in 3 performed a bit poorly was because it started developing the checkerboard
artifacts problem elucidated in [9]. The more the artifacts the lesser the PSNR would be. We ran both models in
Figs 4 and 3 for 7k steps and architecture in 3 developed artifacts earlier than architecture in 4 which is responsible
for decreasing the PSNR. The results of the PSNR are shown in the table 1.

Full Project Report: [Link](https://krishnachaitanya9.github.io/assets/pdf/Deep_Learning_Project.pdf)


