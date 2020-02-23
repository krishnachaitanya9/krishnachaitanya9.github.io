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
git rebase origin/master
```

I was just executing git rebase, even if it executes successfully it doesn't do shit. So be mindful of that. Very important.

If there are merge conflicts, resolve them locally and then execute

```bash
git rebase --continue
```

Now you have a directory, you want it deleted in remote after you added in gitignore. What should you do? Basically without deleting the original directory and committing the changes you delete git's copy and then commit changes. That's how . See the commands below:

```bash
git rm -r --cached some-directory
git commit -m 'Remove the now ignored directory "some-directory"'
git push origin master
```

That's all folks. Please enjoy your time!