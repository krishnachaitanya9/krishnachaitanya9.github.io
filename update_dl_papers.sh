#!/bin/bash
# Start Hardcoding Variables
ARXIV_PATH="$HOME/PycharmProjects/arXiv-Daily-Mailer/arxiv_mailer.py"
BLOG_PATH="$HOME/PycharmProjects/krishnachaitanya7.github.io"
ANACONDA_PATH="$HOME/anaconda3/envs/py3.7/bin/python"
DL_PAPERS_MD="$BLOG_PATH/_posts/2020-09-25-DL_Papers.md"
NOW=$(date +"%Y-%m-%d %H:%M:%S")
# End hardcoding variables
cd "$BLOG_PATH"
# Pulling all the latest updates
git pull
rm $DL_PAPERS_MD
echo "---
title: "Latest Deep Learning Papers"
date: $NOW +0800
featured-img: pytorch-logo
categories: [Deep_Learning]
tags: [Deep_Learning]
mathjax: Yes
---
" > "$DL_PAPERS_MD"
$ANACONDA_PATH $ARXIV_PATH --print True >> "$DL_PAPERS_MD"
git add .
git commit -m "Update DL Papers"
git push -u origin master
