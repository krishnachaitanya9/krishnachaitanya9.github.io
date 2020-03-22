---
title: "Making ROSPkg find your package without installing it through catkin build"
date: 2020-03-22 00:26:00 +0800
categories: [ROS]
tags: [ROS]
---

So recently I had to use rospkg in python. I wanted it to find a ROS package. So I had to source catkin_workspace/devel/setup.bash. But how would those files be generated? When you install it. Well my catkin workspace had so many dependencies and it took a lot of time to install everything in powerful PC's. And also I was sure I won't be needing any of them. So there is no point to install them as it would take a lot of time. 

I just needed rospkg in python to find my ROS packages. How would you do that?

If you delve into code of rospkg it basically looks into the environment variable "ROS_PACKAGE_PATH". If the full path of your "catkin_workspace/src" is appended to this variable rospkg will find it. SO I added something like this in my bashrc 

```bash
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:/home/hiro/catkin_ws
```

"/home/hiro/catkin_ws" will depend on you, rospkg will find your workspace.

Enjoy!





































 