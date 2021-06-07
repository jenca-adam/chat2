#!/bin/bash
for i in chapter* ;do
	echo $i;
	cd $i;
	pdfjam page?.pdf worksheet.pdf -o chapter.pdf;
	qpdf --rotate=-90 chapter.pdf --replace-input;

	cd ..;
	pwd;
	done
pdfjam chapter*/chapter.pdf -o book.pdf --papersize '{1080px,850px}'

