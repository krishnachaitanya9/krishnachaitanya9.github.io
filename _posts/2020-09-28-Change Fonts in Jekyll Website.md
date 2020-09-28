---
title: "Change Fonts in Jekyll Website"
date: 2020-09-28 00:26:00 +0800
featured-img: jekyll-logo
categories: [Jekyll]
tags: [Jekyll]
---
You gotta change files:

- _includes/head.html
Change the Google API's URL for the family of font that you want. Usually head.html is the HTML included in all HTML files in jekyll. If you have different naming make sure to add the changes in that.
```
<link rel="stylesheet"
          href="https://fonts.googleapis.com/css?family=Courier Prime">
```

- assets/css/main.css
In the body tag, update the font family's first font with whatever font you wish to change. Remember it should be of the same family as the URL that you entered in the head.html. Your interested font should be in the first place:
```
font-family:"Courier Prime",-apple-system,BlinkMacSystemFont,"Courier Prime",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Hiragino Sans GB","Microsoft YaHei","WenQuanYi Micro Hei",sans-serif;
```


A good site to choose fonts would be: https://www.w3schools.com/howto/howto_google_fonts.asp where you can get Google API URL's and font name easily. First, personally select your font in Google fonts (https://fonts.google.com/) website.

Look at the changes I made for my Jekyll site here to make whole website use "Courier Prime" font: [Link](https://github.com/krishnachaitanya7/krishnachaitanya7.github.io/commit/3eb06ae6ebea111269e65b8e3aa77056509d7fed)

Hope this helps!!
