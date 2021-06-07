#!/usr/bin/env python3
import os
maxi=0
for i in os.listdir():
    if i.startswith('chapter'):
        m=int(i[7:])
        maxi=max(maxi,m)
os.system(f"./print-worksheet.sh {maxi}")
