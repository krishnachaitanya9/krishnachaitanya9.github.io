---
title: "How to make ROS print Debug statements"
date: 2020-04-01 00:26:00 +0800
featured-img: ros-logo
categories: [ROS DEBUG]
tags: [ROS DEBUG]
---

Recently I had to print DEBUG statements in ROS. By default they aren't prepared. To print debug statements you have to execute the command:

```bash
export ROSCONSOLE_CONFIG_FILE=/home/shivababa/custom_rosconsole.conf
```

You have to pass full path to custom_rosconsole.conf. So now how to write this custom_rosconsole.conf? Below is an example:

```java
# Set the default ros output to warning and higher
log4j.logger.ros=WARN
# Override my package to output everything (Change the level to fit your needs)
log4j.logger.ros.controller_manager=DEBUG
```

```java
log4j.logger.ros.controller_manager=DEBUG
```

How did I get controller_manager? controller_manager is the name of ROS package. you can put any ROS package in place of controller_manager. When you put rosrun you should get controller manager as one of the suggestions of auto-complete. That's one tip. Done. Now where your ROS Core terminal is running you can see a deluge of DEBUG print statements. Good Luck!



































 