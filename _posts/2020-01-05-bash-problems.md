---
title: "Bash -z silly mistake"
date: 2020-01-05 00:26:00 +0800
categories: [Bash]
tags: [Bash]
---

I was making a small script to automate removal of last page in a pdf file. I wanted to do that with Bash. I didn't know it would be that painful but yeah, here I am. The original code I was using was:

```bash
if [-z "$1" ] && [ -z "$2" ];
```

If you use the above code, do you know what you will get? The below error:

```bash
-z command not found
```

Now you scratch your heads and think what all the mistakes you committed in your past and present life as well in this code? Well remember bash is very certain about spaces. Convert the above code to

```bash
if [ -z "$1" ] && [ -z "$2" ];
```
Specifically a space after [, will allow you bash script to run properly. Good Day!
