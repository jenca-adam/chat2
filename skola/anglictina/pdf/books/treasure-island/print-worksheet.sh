#!/bin/bash
if [ -z "$1" ];then
  echo "print-worksheet: not enough args" ;exit 1;fi
if [ -z "$2" ];then 
 	array=$(dir);
  value=$1;
     lpr chapter$1/worksheet.pdf;
     exit $?;

  else
  echo "print-worksheet: too much args";
  exit 1;fi
