---
title: "Setting Wake on LAN in Pop! OS"
date: 2020-02-17 00:26:00 +0800
featured-img: Pop_OS-logo
categories: [Pop!_OS]
tags: [Pop!_OS]
---



Issue was something like this:

Had a PC in my lab. Powerful one. But on Sundays I wanted to work, but not by going to lab. I want to access it through Team Viewer. But I also wanted to turn off my computer when my work is over rather than keeping it up all night and also have the ability to turn it on when I wanted. What did I do? Use Wake-On-LAN. Wake on LAN is a technology is an ethernet standard, which many ethernet supports. You just have to send a magic packet to turn the PC on. 

So to turn it on, you gotta have another PC turned on in the same local subnet. My university PC's were accessible through a VPN. But as long as I am not in the same subnet I cannot send a magic packet even if I know which subnet my PC is in. Only devices in the same subnet can wake up other devices in the same subnet. Now who will come to my rescue? Which device can I always keep on?: Raspberry Pi.

So I made this script present on my GitHub:

https://github.com/krishnachaitanya9/Wake-Me-When-September-Ends

In the readme you can find the crontab which runs every 15 minutes to decide whether to send the magic packet or not.

My idea for turning on the PC is that when it sees an unread email in one of my folders in email, it will send a magic packet. I specially kept one email in there which I toggle between read and unread. The script in the repo checks for unread emails, if yes turns on my PC.

Well everything is good till turning on the PC, but in Ubuntu 18.04 LTS where there is gdm3, it doesn't give access to TeamViewer to let TeamViewer login into my PC. Solution to that is to directly login without password. To set that up you need to edit /etc/gdm3/custom.conf to enable it. You need to uncomment below lines to activate login when the PC turns itself on:

```bash
# Enabling automatic login
AutomaticLoginEnable = true
AutomaticLogin = user1


```

If you want the user to login automatically uncomment the above lines. user1 should be replaced with your username appropriately.

```text
# Enabling timed login
TimedLoginEnable = true
TimedLogin = user1
TimedLoginDelay = 10
```

But if you are in a lab setting like me, and you want to login only after 10 seconds, then uncomment the above lines only. This will make the PC login after 10 seconds. Important note: At this point lines starting with  AutomaticLogin should be commented out, the ones I mentioned for automatic login without delay.

Now if you have kept the Team Viewer on startup list, you can see your PC popping up in your Team Viewer accessible PC's list.

Now activating mult-monitor TeamViewer in ubuntu is very easy:

After connecting to your PC do:

View -> Check Monitors as individual tabs

Now click on whatever monitor you want and you can access all of them remotely. It's particularly useful as I work on multiple monitors.

Enjoy working remotely and also sipping some nice coffee!!