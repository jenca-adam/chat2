#!/bin/bash
for i in chapter* ;do
	cd $i;
	pdfjam page?.pdf worksheet.pdf -o chapter.pdf;
	qpdf --rotate=-90 chapter.pdf --replace-input;

	cd /home/adam/skola/anglictina/pdf/books/oliver-twist ;
	pwd;
	done
pdfjam chapter*/chapter.pdf -o book.pdf

