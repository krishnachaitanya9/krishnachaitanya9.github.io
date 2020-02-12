---
title: "Git daily commands"
date: 2020-02-10 00:26:00 +0800
categories: [Git]
tags: [Git]
---

So recently I have been working a lot around Git. many people have been pushing pulling raising PR's and issues etc. Good stuff. So I thought to write a git tutorial for myself to keep all commands in handy.

To checkout a branch you do:

```bash
git checkout branch_name
```

So to delete a local branch you do:

```bash
git branch -D branch_name
```

This will delete the branch from your local repository, without asking more questions. Straight up delete lol. Best way to take revenge. Go to other's PC, delete branch. LEAVE. I am kidding, don't do that, it's diabolical. Or is it?

Delete local branches which aren't there in remote. Remote meaning on github website when you go to branches, you don't see some which are there in your local PC. One reason could be that somebody might have forgot to push to remote, or somebody deleted that branch from remote. Either case if you want it gone from your PC too run the below command:

```bash
git remote prune origin
```

Now your lazy co-workers pushed on Sunday and you have to merge those into your branch named "not_master" which is not a master. Assume your co-worker is on "IAmLazy" branch. How do you integrate his branch changes into your and start working on it? One way could be you could send a letter to your boss saying "Sunday is important to me you POS" or you can suck up and merge the branch like this:

```bash
git rebase origin/IAmLazy
```

And more better your co-worker pushed it to master to show his workmanship. How do you get all changes from master?

```bash
git rebase origin/master
```

I was just executing git rebase, even if it executes successfully it doesn't do shit. So be mindful of that. Very important.

If there are merge conflicts, resolve them locally and then execute

```bash
git rebase --continue
```

That's all folks. Please enjoy your time!