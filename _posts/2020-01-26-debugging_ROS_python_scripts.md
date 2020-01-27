---
title: "Debugging ROS in python"
date: 2020-01-26 00:26:00 +0800
categories: [ROS, Catkin]
tags: [ROS, Catkin]
---

So I had to develop some scripts for ROS. For ROS you usually need the environment variables pretty badly, and it's always usually relies on system interpreter. In my case it was ROS melodic and it was dependent on Python2.7. By the time of writing this blog, Python2.7 was deprecated, but still we were using it for ROS melodic. It's too bad that they only give support for Ubuntu LTS versions. Anyways. I couldn't use my favourite PyCharm so one many other's insistance I had to try VSCode. You won't get everything out of the box, but you have to configure everything. So let's try configuring it.

### Font

Go to File->Preferences->Settings, scroll down to find "Editor: Font Family". and put 'Fira Code Retina', font size: 17, and enable font ligatures. The setting.json should look something like this:

```. json
{
    "editor.fontFamily": "'Fira Code Retina'",
    "editor.fontLigatures": true,
    "editor.fontSize": 17
}
```

Now File -> Preferences -> Color Theme and Install Noctis Sereno. I like it. Maybe you will too. You can install any theme you like anyways. 

Finally it will install all linters itself. You need to enable this in your settings.json like this:

The catch here, as Visual Studio operates from the terminal where you opened, you can activate the catkin workspace before and open the visual studio by pressing:

```bash
code .
```

So all the environment variables which are needed to communicate are already there active in VS Code. After linting your code, you are really good to go. Place the breakpoint anywhere and start debugging.

For debugging the python code, you really can't use rosrun and use VSCode to debug. If you use rosrun, you can't debug. So the way is 

- Activate the catkin environment 
- Run the python file as is. It should work for normal run as well as debug

To quote the Mandalorian Series - "That's the way"

 This feature ain't available in PyCharm because it changes a lot of environment variables when running the python code. This is the only one downside of PyCharm else it's a greatest piece of software I have ever known. 

My final VS Code settings file looks something like this:

```json
{
    "editor.tokenColorCustomizations": {
        "textMateRules": [
          {
            "name": "Comment",
            "scope": [
              "comment",
              "comment.block",
              "comment.block.documentation",
              "comment.line",
              "comment.line.double-slash",
              "punctuation.definition.comment",
            ],
            "settings": {
              "fontStyle": "italic"
            }
          },
        ]
     },
    "editor.fontFamily": "'Fira Code Retina'",
    "editor.fontLigatures": true,
    "editor.fontSize": 17,
    "workbench.colorTheme": "Andromeda Italic",
    "python.linting.pylintEnabled": true,
    "terminal.integrated.inheritEnv": false
}
```

I will keep editing this to keep it updated here.