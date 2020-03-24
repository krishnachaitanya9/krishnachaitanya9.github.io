---
title: "OpenDCIM Backup"
date: 2020-02-23 00:26:00 +0800
categories: [Eagle PCB]
tags: [Eagle PCB]
---

Recently I had to take OpenDCIM backup. What I did was:

First take backup of dcim database. 

```bash
mysqldump -u dcim -p dcim > test.sql
```

Then Copy the folders drawings and pictures from original opendcim location.



Next in the new location do:

```bash
mysql -u dcim -p dcim < test.sql 
```

From the test.sql obtained. Then copy the original drawings and pictures to new location and Voila!