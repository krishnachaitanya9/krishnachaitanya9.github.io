---
title: "Using Textblocks to save time writing regards in my emails"
date: 2020-02-29 00:26:00 +0800
categories: [Automation]
tags: [Automation]
---

First install the following else the package wouldn't work:

```bash
sudo apt install xclip
sudo apt install xsel
```

Then from the Repo: https://github.com/GeorgeCiesinski/text-script install it and add text blocks about your regards saying

```bash
Regards
Kodur Krishna Chaitanya
```

save it as #rg.txt  inside textblocks folder. Now type in #rg in your email and above regards string saved into #rg.txt appears in your text.

If it doesn't appear then you need to look into logs to find specific issue which would be inside "Logs" folder inside your project directory.

Cheers!

