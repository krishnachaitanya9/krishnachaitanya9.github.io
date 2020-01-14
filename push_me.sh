#!/bin/bash
git add .
if [ -z "$1" ]
then
  git commit -m "Blog Content"
else
  git commit -m "$1"
fi
git push -u origin master
