
import sys
import os
import re

try:
    logfile= sys.argv[1]  #this line works only on command prompt
except:
    logfile="sample.log"

sdict={}
sum=0


with open(logfile) as f:
    for line in f:
        if "[DEBUG]" not in line:
            continue
        pattern=r"\d\s([A-Za-z]+\d)\s\[\w*\]\s\w*\s\w*\s\w*\s([\d]*)$"
        result=re.search(pattern,line)
        if result is None:
            continue
        sdict[result[1]]=sdict.get(result[1],0)+1
        sum=sum+int(result[2])

print("sample class dictionary for [DEBUG] instance:\n")
print(sdict)

print("\nSum of id numbers:\n")
print(sum)
