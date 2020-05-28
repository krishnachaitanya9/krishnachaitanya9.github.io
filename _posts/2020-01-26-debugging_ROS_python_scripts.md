---
title: "Debugging ROS in python"
date: 2020-01-26 00:26:00 +0800
featured-img: ros-logo
categories: [ROS, Catkin]
tags: [ROS, Catkin]
---

So I had to develop some scripts for ROS. For ROS you usually need the environment variables pretty badly, and it's always usually relies on system interpreter. In my case it was ROS melodic and it was dependent on Python2.7. By the time of writing this blog, Python2.7 was deprecated, but still we were using it for ROS melodic. It's too bad that they only give support for Ubuntu LTS versions. You use your PyCharm to do debugging. PyCharm's debugger is one of the best. If you open PyCharm normally (From the desktop icon that it creates) you wouldn't be able to debug because catkin environment isn't activated. But if you first open terminal, activate catkin environment and then run pycharm.sh manually then you can easily debug your code with PyCharm.

One conundrum I had was that I had to debug controller manager [Link](https://github.com/ros-controls/ros_control/pull/458) to fix a bug of denial of service inside it. Now all I know it's loaded inside a Dynamic Linked SO library. How to find where in the memory is it loaded? Here comes the use of catkin build. I downloaded the [ros control](https://github.com/ros-controls/ros_control) from the link and bulit it along with debugging symbols by the use of the catkin build command with extra Flag added:
```bash
-DCMAKE_BUILD_TYPE=Debug
```
Now I went through the code and found some places where I can add std::cout statements which I know will definitely print. After building using the catkin build and seeing for myself the std::cout statements I conferred that infact atleast whatever the code I have in my catkin workspace is loading up. Next to pin point which application I printed out the PID using ::getpid() and voila! Now I know the PID and I looked into the htop command to find which application the PID belongs to. It was gzserver in my case which is short for Gazebo Server. Now in CLion you can connect to it (Technical term is attach to process) at runtime and debug it. Now when I attach to gzserver CLion detects that it's able to debug the Controller Manager. Voila! 