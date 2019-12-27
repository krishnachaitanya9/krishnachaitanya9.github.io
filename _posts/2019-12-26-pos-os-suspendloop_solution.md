---
title: "Pop! OS Suspend Loop Solution"
date: 2019-12-26 00:26:00 +0800
categories: [Pop! OS, Systemd Boot]
tags: [Systemd_Boot, Pop!_OS]
---
Just installed Pop!_OS in my new Razer Blade 15. Reason is because Pop! OS  supports NVidia
out of the box. I also didn't face HDMI issue. The HDMI issue is that when I plugin the HDMI cable
nothing was visible in the external monitor. But Pop! OS supported it right out of the box. I think
Pop! OS is the best Razer. Later I also installed Polychromatic app by Razer and I love the lighting.


But there was one problem. When I suspend my Blade and then turn it back on, it again used to suspend after
20 seconds. You can call it the "Suspend Loop". It's similar to what happened to my android mobile when I experimented on it a little too much. In terms on Android they call it "Boot Loop".

Unfortunately on Ubuntu website the solution I got was for Grub. Pop! OS migrated from Grub to systemd boot. They argue in their website that it cuts time in booting. Fair enough. After a lot of searching
I found the solution. You have to edit the following file

```bash
/boot/efi/loader/entries/Pop_OS-current.conf
```

And add the below lines after splash in the above file. The original file looks like this:
```bash
title Pop!_OS
linux /EFI/Pop_OS-2f6ebbd3-7b44-43a8-b484-876a8cbd8d98/vmlinuz.efi
initrd /EFI/Pop_OS-2f6ebbd3-7b44-43a8-b484-876a8cbd8d98/initrd.img
options root=UUID=2f6ebbd3-7b44-43a8-b484-876a8cbd8d98 ro quiet loglevel=0 systemd.show_status=false splash
```
The edited file looks like this:

```bash
title Pop!_OS
linux /EFI/Pop_OS-2f6ebbd3-7b44-43a8-b484-876a8cbd8d98/vmlinuz.efi
initrd /EFI/Pop_OS-2f6ebbd3-7b44-43a8-b484-876a8cbd8d98/initrd.img
options root=UUID=2f6ebbd3-7b44-43a8-b484-876a8cbd8d98 ro quiet loglevel=0 systemd.show_status=false splash button.lid_init_state=open
```
Only difference is you need to add
```bash
button.lid_init_state=open
```
after splash.

And Voila! Suspend Loop problem solved!
