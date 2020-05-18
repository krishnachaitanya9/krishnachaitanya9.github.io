---
title: "Trajectory Msg in Python"
date: 2020-01-26 00:26:00 +0800
categories: [ROS, Catkin]
tags: [ROS, Catkin]
---

So there are no good tutorials in Trajectory Messages on the internet. So this might serve as one. So to control a robot, it's position, joint's velocity and acceleration you need to use trajectory message. to control the robot. In the HIRO lab I work, there is robot called Pandas Emika. So my code will have some tidbits of panda robot if you are interested in that. So let's dive in. There are other alternatives like move_it where you can use their python implementation but I find using Trajectory Msg's from ROS easy. So here I go.

Trajectory Msg's are used to send trajectory info to either robot or a simulator which will then move the robot accordingly. So how do you use it? Run the below command:

```bash
rosmsg info trajectory_msgs/JointTrajectory

std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
string[] joint_names
trajectory_msgs/JointTrajectoryPoint[] points
  float64[] positions
  float64[] velocities
  float64[] accelerations
  float64[] effort
  duration time_from_start
```

So we find that there is a header, and also another field called points. So how do we set these values from python? Below is the code:

```python
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
trajectory_msg = JointTrajectory()
trajectory_msg.header.stamp = rospy.Time.now()
trajectory_msg.header.frame_id = '/base_link'

trajectory_msg.joint_names = ['panda_joint1', 'panda_joint2', 'panda_joint3', 'panda_joint4', 'panda_joint5', 'panda_joint6',
                              'panda_joint7']

point = JointTrajectoryPoint()
point.positions = [0, 0, 0, 0, 0, 0, 0]

```

Similarly you can set point.velocities, point.accelerations and point.effort. Enjoy!