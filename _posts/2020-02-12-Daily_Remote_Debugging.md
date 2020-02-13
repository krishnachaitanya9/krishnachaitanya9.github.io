---
title: "Remote Debugging"
date: 2019-02-12 00:26:00 +0800
categories: [Debugger]
tags: [Debugger]
---

So I wanted a solution in which the debugger can just fly in to my PC so that I can see all it's variables and see what caused the script to crash drastically. Luckily I have a friend in PyCharm. So this is how it goes.

There are two computers

- Own PC
- Server

Both of the PC's should have pydevd_pycharm installed for this tutorial.

The server will run our precious script and crash into an exception. Own PC will be ready to accept connections from the server, so that in our leisure we can see what the problem was. Lets make a small test script which will run into exception for sure to show it as a proof-of-concept

```python
"""
Remote debugging setup
Reference: https://stackoverflow.com/questions/6989965/how-do-i-start-up-remote-debugging-with-pycharm
"""
import math
import pydevd_pycharm
pydevd_pycharm.settrace('10.201.16.206', port=4444, stdoutToServer=True, stderrToServer=True)

if __name__ == "__main__":
    x = 0
    print("Wantedly testing remote exception to see if it works or not")
    y = 2/x
    print("Yayy!!!")
```

So here 10.201.16.206 is the IP of Own PC. I repeat the script should be same in both Own PC and server. Now in the pycharm you need to add the following settings:

- *Run*-> *Edit Configurations*: opens the 'Run/Debug Configurations' dialog
- *Defaults* -> "Python Remote Debug": is the template to use

So in this template there are a couple of things you need to carefully fill:

Host: keep it localhost

Port: Put any vacant port. If your pycharm is running in sudo you can put any port you wish, but I won't recommend doing that. You should put the same port in pydevd_pycharm.settrace port option.

Mapping: It's for showing at exactly what line you are in the remote and to show it in local. For that pycharm needs to know the path mappings so that it can identify the file correctly and show the exception. For the local put the project path from where pycharm is running. Please specify the full path. In the remote you can do so similarly. Basically your Project path from where you run python files should be same in both Own PC and remote server. For example:

Own PC Project path: /home/blabla/PycharmProjects/test/

Server path: /home/blabla2/PycharmProjects/test/

This works

This doesn't work:

Own PC Project path: /home/blabla/PycharmProjects/test/another_folder

Server path: /home/blabla2/PycharmProjects/test/

As there is another_folder inside test. In more layman terms, you open both folders side-by-side both folder's folder structure and files should exectly look same. Then you can put these two paths in path mapping.

Now you are ready with everything. Now Save the Python Remote Debugging template with some name and run it in your Own PC.  According to our settings lets assume it's running in port 4444. So port 4444 in Own PC is open to connections.

Go to server pc, and then run the script, the moment it runs, it should stop, which is an indication that everything is reachable and everything is working fine. Now you give a command to continue running and leave it for night. If there are any exceptions, it will come back and stop and show the debugger in your pycharm so that you can see all variables/environment variables etc.

To print environment variables make sure you import os before itself, even if it's not used in the script so that we can issue commands and get environment variables in our Pycharm console. The python command to execute would be something like this:

```python
print(os.popen('echo $PYTHONPATH').read())
```

Will print $PYTHONPATH of remote server in your local Own PC.

Happy Debugging!







