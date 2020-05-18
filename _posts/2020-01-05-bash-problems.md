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

It doesn't say your syntax is wrong, but misleadingly says command not found. NOT COOL!!

Now you scratch your heads and think what all the mistakes you committed in your past and present life as well in this code? Well remember bash is very certain about spaces. Convert the above code to

```bash
if [ -z "$1" ] && [ -z "$2" ];
```
Specifically a space after [, will allow you bash script to run properly.

So how to find this anamolies? You gotta install linter. I use atom for all my bash scripts. I use the shellcheck linter in Ubuntu (Don't know don't care about Windows OS) which can be installed as below:

```bash
sudo snap install shellcheck
```

Then in atom you have to install this amazing plugin [linter-shellcheck](https://atom.io/packages/linter-shellcheck). This will show if you have any problems in the script and help you correct it. 

Recently I have found that zsh is a GREAT for people who use branches and git like me. I installed agnoster theme and it's beautiful. But zsh doesn't have shell linters by default, I hope they make one. The default bash shell linter doesn't work for zsh, and it throws an error. To make the shellcheck interpret our zsh script as a bash script, you need to add the following line after shebang line:

```bash
# shellcheck shell=bash
```

Like this, you can atleast lint your code and not pull your hair. Source: https://scriptingosx.com/2019/08/shellcheck-and-zsh/

Good Day!