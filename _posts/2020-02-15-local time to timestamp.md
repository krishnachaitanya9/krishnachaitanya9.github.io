---
title: "Local Time to Unix Timestamp"
date: 2020-05-19 00:26:00 +0800
featured-img: python-logo
categories: [Python]
tags: [Python]
---

How to convert your local time to a unix time stamp? One of the major mistakes that happen is not passing the timezone info when getting the timestamp. It's many times safe to assume that datetime will generate using the PC's local time zone but why take risk? So pass the tzinfo (Time Zone Info) when calculating the time stamp like this:

```python
import datetime
from dateutil import tz
mst_time_zone = tz.gettz('America/Denver')
start_time = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second,
                                       tzinfo=mst_time_zone)
```
You need year, month, day, hour, minute, second and timezone to accurately calculate the timestamp which can be converted to other times in other time zones and also to maintain perfect inter-operability. 
Thanks!