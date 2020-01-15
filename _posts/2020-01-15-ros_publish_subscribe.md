---
title: "ROS No brainer Intro"
date: 2020-01-15 00:26:00 +0800
categories: [ROS]
tags: [ROS]
---

Recently I had to work with ROS. God knows why, but had to. So here I am. This is a no-brainer introduction. One of the very good reference is a youtube [link](https://www.youtube.com/watch?v=DLVyc9hOvk8). First things first, you need to run ROS Core by the following command:

```bash
roscore
```

It will printout some useful info. Basically it means that in the Ubuntu PC or Raspberry Pi where you ran the command, that will work as Master. In this blog we will call this Master. It will have a list of publishers and subscribers  and basically whatever is going on. Don't forget this command y'all. Also when the command is executed, search for  ROS_MASTER_URI environment variable. That's what you have to set the environment variable in all nodes running listener and talker. Next command to enter is:

```bash
rostopic list
```

And the default output will be:

```bash
/rosout
/rosout_agg
```

Now there comes something called topic. What's topic? Topic is something to which talker sends the data to and listener listens for the data. Where can you find list of topics? From the Master. The only job of Master is to know about topics, and who are publishing them and who is subscribing to them. That's it. 

Now there is a listener code and talker code. Listener code is where you wanna put your listener, which will listen and then perform some actions based on input it gets. Talker is the code which talks, which basically means it will send the data to the specific topic. Easy?

Now in every PC/Embedded system where you wanna run your talker and listener code you need to set the below environment variables:

```bash
ROS_MASTER_URI
ROS_IP
```

So ROS_IP is the IP of the PC in which the listener or talker is running. So the Master can be anywhere in the network. Listener can be anywhere in the network. Talker can be anywhere on the network. As long as they are accessible to each other, it's okay.

Next lets make an imaginary scenario and code together.

### Master Code

Set below environment variables

ROS_MASTER_URI = http://172.16.0.210:11311

ROS_IP = 172.16.0.210

This will be running roscore in one of the terminal

### Talker Code

Set below environment variables

ROS_MASTER_URI = http://172.16.0.210:11311

ROS_IP = 172.16.0.109

Code:

```python
#!/usr/bin/env python
# license removed for brevity
import rospy
from robotic_skin.sensor.adxl335 import ADXL335
from sensor_msgs.msg import Imu

def talker():
    pub = rospy.Publisher('/imu', Imu, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(10) 

    accel_sensor = ADXL335(xpin=0, ypin=1, zpin=2)
    imu_msg = Imu()

    while not rospy.is_shutdown():
        data = accel_sensor._read_raw()
        imu_msg.linear_acceleration.x = data[0]
        imu_msg.linear_acceleration.y = data[1]
        imu_msg.linear_acceleration.z = data[2]

        pub.publish(imu_msg)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
```

Talker code will be sending IMU data. When you start the talker, in master node when you input the below command 

```bash
rostopic list
/imu (apart from other, you should see this topic)
```

### Listener Code

Set below environment variables

ROS_MASTER_URI = http://172.16.0.210:11311

ROS_IP = 172.16.0.110

Code:

```python
#!/usr/bin/env python
# license removed for brevity
import rospy
from robotic_skin.sensor.adxl335 import ADXL335
from sensor_msgs.msg import Imu

def talker():
    pub = rospy.Publisher('/imu', Imu, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(10) 

    accel_sensor = ADXL335(xpin=0, ypin=1, zpin=2)
    imu_msg = Imu()

    while not rospy.is_shutdown():
        data = accel_sensor._read_raw()
        imu_msg.linear_acceleration.x = data[0]
        imu_msg.linear_acceleration.y = data[1]
        imu_msg.linear_acceleration.z = data[2]

        pub.publish(imu_msg)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
```

The listener will start listening, and according to the input received from the talker, it will start printing the x,y,z accelerations continuously.  Here you should see one important piece in rospy.Publisher function called queue_size. That means if you if the queue is full, it will drop any next data it would receive. So if you anticipate to take more time, then just increase queue_size. Else packets will be dropped. 

Good Day!

