---
title: "Using Textblocks to save time writing regards in my emails"
date: 2020-02-29 00:26:00 +0800
featured-img: python-logo
categories: [Automation]
tags: [Automation]
---

First install the following else the package wouldn't work:

```bash
sudo apt install xclip
sudo apt install xsel
```

Then from the Repository: https://github.com/GeorgeCiesinski/text-script install it and add text blocks about your regards saying

```bash

Regards
Kodur Krishna Chaitanya
```

save it as #rg.txt  inside text-blocks folder. Now type in #rg in your email and above regards string saved into #rg.txt appears in your text. If it doesn't appear then you need to look into logs to find specific issue which would be inside "Logs" folder inside your project directory.



Also one mistake I made was to not cd into textblocks directory before running the python file.  I corrected it by using this command:

```bash
cd /home/shivababa/PycharmProjects/text-script/textscript && /home/shivababa/anaconda3/envs/py3.8/bin/python /home/shivababa/PycharmProjects/text-script/textscript/text-script.py
```

That did the trick!

Cheers!

