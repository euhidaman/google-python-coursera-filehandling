#the input of the program is taken from "Actors.txt" using pipeline
#the output of the program is sent to the some other textfile, using empty '>'

#cmd prompt cmd --->  type Actors.txt|python actorprog.py "A" > actorsdictionary.txt
#In the above cmd, I am making a dictionary with names starting from "A"
#And the output, in this case is stored in "actorsdictionary.txt" file

import sys
import re

ls=[]
namedic={}


for line in sys.stdin:
    pattern=r"[\d]+,([\w ]*)"
    result=re.search(pattern,line)
    if result is None:
        continue

    wordstart=sys.argv[1]
    if result[1].startswith(wordstart):
        ls.append(result[1])

for name in ls:
    namedic[name]=namedic.get(name,0)+1

print(namedic)
