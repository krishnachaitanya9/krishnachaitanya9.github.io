---
title: "Install Package using Python Wheels"
date: 2020-01-08 00:26:00 +0800
featured-img: raspberry-pi-logo
categories: [RPi, Wheels]
tags: [RPi, Wheels]
---

So when installing any python package on Raspberry Pi, if something is taking too long time, it might be building everything from sources.

You know in normal computer itself, building everything from scratch eats up a lot of computation power. RPi being an embedded computer, installing from sources will take-up sometimes a whole night. You wouldn't want that during deadlines.

So what's the solution here? Wheels!! Python wheels are packages specifically built for that platform. Little backstory if you try to a binary compiled to run in ARM devices, it won't run on intel devices. So a wheel generated for intel devices won't run on ARM devices such as RPi. Fortunately there are some good people on internet who compile these tedious packages for you and make them readily available for everyone to download. Please visit this wonderful website: [piwheels](https://www.piwheels.org/)

If you add the URL to pip, it will automatically find wheels and if present it will install them. You can also install this in virtual environment. Wherever you wish.

Despite many attempts, due to some unknown reasons sometimes pip can't find the appropriate wheels. What do you do at that time? You can download the wheel from the aforementioned website and install it as follows

```bash
pip install package_wheel.whl
```

This will save you enormous amounts of time. Also don't forget to go through piwheels website for their tutorials on how o do use it. It's pretty straightforward. Also read this article in how piwheels is contributing to saving people's time and helping them concentrate on more pressing concerns. [How piwheels will save Raspberry Pi users time in 2020](https://opensource.com/article/20/1/piwheels). Good Day!
