---
title: "Take RPi image backup and also load it in your filesystem to check it's contents"
date: 2020-01-08 00:26:00 +0800
featured-img: raspberry-pi-logo
categories: [RPi]
tags: [RPi]
---
Recently I started using my favorite Raspberry Pi again. So after installing some software and checking whether it's working or not, I wanted to take backup of the image. Before I used to do it in Win32DiskImager. But recently I have been a zealot about ubuntu. So I thought I should try using dd. I was always afraid of dd that I would mess-up something, but don't worry, if I am able to do it, you will definitely be able to do it. So let's start taking backup shall we?!

First see what what's your SD card device. For example Mine had 2 partitions, Fat32 for boot and ext4 for the file system and they were /dev/sda1 and /dev/sda2 respectively. In this case our SD card would be /dev/sda. NOT /dev/sda1 or /dev/sda2. /dev/sda. See the stress I am putting. Unless you wanna just take backup of filesystem, but some extra Mb's won't kill ya. So how would you find this /dev/sda? By using "Disks" application. Congrats you found your device. Go drink a beer!

Now you have to run the dd, to take the backup. Execute the below command (We are considering that /dev/sda as our device as discussed previously)

```bash
sudo dd if=/dev/sda of=/path/to/destination/new.img
```

Voila! you have your new image. Now if you want to see what are inside it how would you do it? Rather than me explaining see this Stack Exchange accepted answer. It's very well written. I hope to write a script to automate this one day.

[Mount RPi img file RPi Stack Exchange](https://raspberrypi.stackexchange.com/questions/13137/how-can-i-mount-a-raspberry-pi-linux-distro-image)
