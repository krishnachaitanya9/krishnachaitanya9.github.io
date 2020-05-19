---
title: "Convolutional Neural Networks"
date: 2020-05-14 00:26:00 +0800
featured-img: CNN-logo
categories: [Deep_Learning]
tags: [Deep_Learning]
---
In deep learning, anything related to images has convolution layer in them. So after you put an image into a convolution layer what would be the output width or height? The formula is

$$
\frac{W - K + 2P}{S} + 1
$$
Where

- W is the input volume (AKA either width or height of image)
- K is the Kernel size
- P is the padding
- S is the stride

Reference: [CS231n Stanford Course](https://cs231n.github.io/convolutional-networks/)

Now kernel size here can be (nxn) which means n = K = 3. How would the number of filters affect the output of convolutional layer? Now how to understand it intuitively? For example you input a single channel 28x28 image to a convolution layer with 3 convolutional filters what would be the output? To visualize this properly here is the [youtube link](https://youtu.be/k6ZF1TSniYk?t=296) I am directly copying the image from there. First let me put the variables in the formula. We will be considering the kernel size 5, padding would be 0, Stride would be 1 output widthxheight would be
$$
\frac{28 - 5 + 2(0)}{1} + 1 = 24
$$
So a 24x24 image output, the number of filters would directly affect the number of output channels. For example the input number of channels is 1, the number of filters lets assume it is 3, output no of channels would be equal to number of filters.

## Visualization
Let's take the input image 28x28x1 as below (Note the image shows the input as 1x1x28x28 which means it's batch_sizexno_of_channelsxwidthxheight, I am denoting it as widthxheightxno_of_channels)

![input_image](/assets/img/conv_nets/input_to_convolution.png)

Then the output of the convolution layer with 3 filters would be

![output_image](/assets/img/conv_nets/output_convolution.png)

Now the outputs that you see in the image, each individual layer is called as the feature map.

![feature_map](/assets/img/conv_nets/feature_map.png)

Reference: [machine learning mastery link](https://machinelearningmastery.com/convolutional-layers-for-deep-learning-neural-networks/)

Now what happens if there are multiple channels in the input rather than one channel as in above example? Even then the output number of channels will be equal to the number of filters. I will not go into more details but there is a beautiful article [here](https://blog.xrds.acm.org/2016/06/convolutional-neural-networks-cnns-illustrated-explanation/), the figure 2 explains it all. Lets write it in bold letters

**Number of filters in convolution = Output no of channels**
