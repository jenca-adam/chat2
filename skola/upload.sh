#!/usr/bin/bash
m=$(pwd)
cd anj/pdf/books/oliver-twist
git add .  -v
git commit -m "$(date)" 
git push
cd $m
git add --all -v
for i in *;do
	git add $i;done 
git commit -m "$(date)" 
git push
