---
title: "Git daily commands"
date: 2020-02-10 00:26:00 +0800
categories: [Git]
tags: [Git]
---

To setup your email in git to be used globally:

```bash
git config --global user.email "chaitanyaradon89@gmail.com"
```

So recently I have been working a lot around Git. many people have been pushing pulling raising PR's and issues etc. Good stuff. So I thought to write a git tutorial for myself to keep all commands in handy.

To checkout a branch you do:

```bash
git checkout branch_name
```

So to delete a local branch you do:

```bash
git branch -D branch_name
```

This will delete the branch from your local repository, without asking more questions. 

Delete local branches which aren't there in remote. Remote meaning on github website when you go to branches, you don't see some which are there in your local PC. One reason could be that somebody might have forgot to push to remote, or somebody deleted that branch from remote. Either case if you want it gone from your PC too run the below command:

```bash
git remote prune origin
```

Now your co-workers pushed on Sunday and you have to merge those into your branch named "not_master" which is not a master. Assume your co-worker is on "coworker" branch. How do you integrate his branch changes into your and start working on it? One way could be to merge the branch like this:

```bash
git rebase origin/coworker
```

And more better some changes have been merged to master through a PR. How do you get all changes from master?

```bash
git merge origin/master
```

This will merge all master's commits into one commit and also let's you resolve any conflicts so that it's ready to merge into master. It's always better to do merge. Online you can see many blog posts about differences. Adding to them one other difference is that When I was doing rebase, lots of commits were coming up in the pull requests for merging a branch to master. But when I did merge there was only one clean commit which would be merging all changes from master. Hence use merge to get all changes from master.

Now you have a directory, you want it deleted in remote after you added in gitignore. What should you do? Basically without deleting the original directory and committing the changes you delete git's copy and then commit changes. That's how . See the commands below:

```bash
git rm -r --cached some-directory
git commit -m 'Remove the now ignored directory "some-directory"'
git push origin master
```

How to add a submodule?

```bash
git submodule add https://github.com/erdalpekel/panda_simulation.git src/panda_simulation
```

If you just clone, git will make you a folder, but in submodule if you tell it the name of non existent folder it will clone everything to it. Like panda_simulation shouldn't be there in src, so everything will be cloned to src/panda_simulation. It won't make new folder and save it to src/panda_simulation/panda_simulation. Good point to know!

Now if you want to add a submodule with a specific branch, what would you do?

You need to see this stackoverflow link for better answer: https://stackoverflow.com/questions/1777854/how-can-i-specify-a-branch-tag-when-adding-a-git-submodule

That's all folks. Please enjoy your time!