---
title: "Download GDrive files using wget"
date: 2020-03-25 00:26:00 +0800
categories: [GDrive wget]
tags: [GDrive wget]
---

To download GDrive files using wget use:

```bash
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=FILEID' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=FILEID" -O FILENAME && rm -rf /tmp/cookies.txt
```

Lets take an example. I had to download dataset. The URL was: https://drive.google.com/uc?id=1badu11NqxGf6qM3PTTooQDJvQbejgbTv&export=download

So the fields you need to put in the above wget command are:

Where FILEID = 1badu11NqxGf6qM3PTTooQDJvQbejgbTv

and FILENAME = CelebAMask-HQ.zip

And voila! Your file downloads.



































 