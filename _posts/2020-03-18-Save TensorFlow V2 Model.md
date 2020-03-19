---
title: "Save Tensorflow V2 Models"
date: 2020-03-18 00:26:00 +0800
categories: [Zip Password]
tags: [Zip Password]
---

I have got a simple wish. I just need to save TensorFlow models so that I can restart the training after my Super Computer quota time gets over. Is it too much to ask for? Well It's not. Let's dive in.

First let's find out what are the differences between HDF5, CKPT and PB. These are the three main model types. Well there is a very good question asked on Stackoverflow which I wanna keep track of:

https://stackoverflow.com/questions/59887312/when-to-use-the-ckpt-vs-hdf5-vs-pb-file-extensions-in-tensorflow-model-savin

Anyways let's save checkpoints in ckpt for now.