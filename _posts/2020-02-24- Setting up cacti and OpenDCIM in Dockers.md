---
title: "Cacti and Eagle installation"
date: 2020-02-23 00:26:00 +0800
categories: [Eagle PCB]
tags: [Eagle PCB]
---

So I had to install Cacti and OpenDCIM for a project. Here is how I did it.

To run cacti execute

```bash
docker run -d -p 80:80 -p 161:161 quantumobject/docker-cacti
```



# 

The default username is admin and password is admin. After that visit http://localhost/cacti to login and start the installation. As I am running a docker image it's important to save all the work after doing some changes like installation. To do that execute:

```bash
docker commit DOCKER_ID latest_cacti
```

After this your new command to run cacti docker would be:

```bash
docker run -d -p 80:80 -p 161:161 latest_cacti
```



Where DOCKER_ID you can get from the 

```bash
docker ps
```

command.

