---
title: "Make Password Protected Zip in Ubuntu"
date: 2020-03-18 00:26:00 +0800
categories: [Zip Password]
tags: [Zip Password]
---

I gotta password protect some files and then upload to GDrive somewhere. So what I gotta do? Password protect them. How do you do it using GUI in Ubuntu? There are many answers floating around but the right click option of setting password using compress doesn't work after Ubuntu 17.10. One of the answers I found totally right is: 

https://askubuntu.com/a/985694/389510

In the author's own words:

```text
Starting from Ubuntu 17.10, right-clicking and selecting "Compress" no longer has "Other Options" listed.

To resolve this, open "Archive Manager" and then drag & drop the files/folders from your File Manager into it and it will appear.
```

Now the compressed zip files their file structure is open. If you don't want that to be visible, first make a normal zip without password. Then make another zip file and put the normal zip inside that zip and protect it with password. End users would have to unzip twice, but you have secure password protection and nobody is able to see inside contents so they would be discouraged in opening them. win win.

And that's how you create password protected zips in ubuntu.

