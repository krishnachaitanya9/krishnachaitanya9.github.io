---
title: "Getting I2C working in Raspberry Pi 3B Ubuntu Mate"
date: 2020-01-15 00:26:00 +0800
featured-img: raspberry-pi-logo
categories: [RPi, I2C]
tags: [RPi, I2C]
---

So for the labwork we are using Ubuntu Mate, so that we can use ROS. Ubuntu Mate has an advantage for getting ROS installed easily compared to Raspbian OS preferred by Raspberry Pi community. But having Ubuntu mate comes with it's own problems. I2C activation isn't easy. So Let's work on it.

So this worked for me:

Add the following line to `/boot/config.txt`

```bash
dtparam=i2c_arm=on
```

Add the following line to `/etc/modules`

```bash
i2c-dev
```

Reboot Raspberry Pi. 

Reference:

https://raspberrypi.stackexchange.com/questions/61905/enable-i2c-on-ubuntu-mate-raspberry-pi-3

After this you need to find out what are the addresses your I2C devices are. To do that you need to execute the command below:

```bash
hiro@hiro-desktop:~$ sudo i2cdetect 1
WARNING! This program can confuse your I2C bus, cause data loss and worse!
I will probe file /dev/i2c-1.
I will probe address range 0x03-0x77.
Continue? [Y/n] Y
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- 29 -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- 6b -- -- -- -- 

```

I have executed "sudo i2cdetect 1" because I had connected to I2C port 1 in Raspberry Pi. There are 2 I2C ports in Raspberry Pi. If you connect to the other port, you may have to put "sudo i2cdetect 0".



According to the output above, it means that you have 2 I2C devices connected to port 1. One is at address 0x29 and another is at address 0x6b. 