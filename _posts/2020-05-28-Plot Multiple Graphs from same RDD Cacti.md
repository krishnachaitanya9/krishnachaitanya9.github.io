---
title: "Plot Multiple Graphs from same RDD in Cacti"
date: 2020-05-28 00:26:00 +0800
featured-img: cacti-logo
categories: [Cacti]
tags: [Cacti]
---
So for one of my projects where I had to continuously log in data from a data source and compare the trend for years to come in server data analytics Cacti is the best suited for it. Now whenever you make a new graph cacti will start requesting the data source for each new graph even though it's from the same data source. Is the data source is queried multople times it can lead to DOS issues which isn't anticipated. I gotta keep the requests less and at the same time plot multiple graphs. How to do? Below is the way:

- Go to Management-> Data Sources. Fix one data source ID. In my case I choose 122 as it was least, meaning it has most data than any rrd
- In the above-selected data source ID, find what's the rrd file and note down the name. In my case it was xx.rrd. I will be calling it reference data source ID.
- Next, go to other new data sources and then change the rrd file with fixed data source's rrd file which in our case would be xx.rrd
- Disable the new data source so that it won't make multiple requests to the server as the reference data source ID is already doing the job of requesting the data. If the new data sources aren't disabled then they individually make multiple new requests
