---
title: "VSCode and Hydra Config"
date: 2021-01-26 00:26:00 +0800
featured-img: pytorch-logo
categories: [PyTorch]
tags: [PyTorch]
---
I use Hydra to manage all my config requirements. It's a beautiful package. Love it!!

When I debug my program, I set HYDRA_FULL_ERROR=1. But still I am not able to go inside the debugger frames,
when I can see which line from the site-packages, the error is originating from. When I looked around a bit, I found the issue.

You also have to set 
```bash
"justMyCode": false
```
in your debug config file of VSCode. Else you can't see all the frames from where the exception is originating. 

So you need to set HYDRA_FULL_ERROR and justMyCode and then only you can see all debugger frames. I hope this helps someone.

Take care!!
