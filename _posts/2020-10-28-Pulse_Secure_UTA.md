---
title: "Pulse Secure VPN connection in Raspberry PI or other ARM devices"
date: 2020-09-28 00:26:00 +0800
featured-img: DL-logo
categories: [VPN]
tags: [VPN]
---
Recently I was at a University where I had to use Pulse Secure VPN connection. The Pulse secure VPN doesn't provide any binaries for ARM :(. So I had to figure some way out to connect with my Raspberry PI. 

First I installed opeconnect from [here](https://launchpad.net/~lopin/+archive/ubuntu/openconnect-globalprotect)

Next, I used the below command:

```bash
sudo openconnect --protocol=pulse https://YOUR_ORGANIZATION_VPN_URL
```
And then done. In the command line itself you will be asked for your password and 2-factor authentication password and you are connected!!

