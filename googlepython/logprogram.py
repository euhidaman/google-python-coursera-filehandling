# program works
#I am trying to read the names of the "Source" from "logprac.csv"
#and, then I am making a dictionary of the "Source" and how many times , it occurs in logprac.csv
#the dictionary is stored in "sourcetimes.txt" (not required in this program anymore)
#cmd is ---> python logprogram.py logprac.csv
#at last, I am trying to output this dictionary (s_list),in a csv file called "sourcetimes.csv"
import re
import sys
import csv
import os

csvfile=sys.argv[1]

list=[]
dict={}
s_list=[]

with open(csvfile) as file:
    reader=csv.DictReader(file)
    for row in reader:
        list.append(row["Source"])

for source in list:
    dict[source]=dict.get(source,0)+1

s_list.append(dict)

with open('sourcetimes.csv', 'w', encoding='utf8', newline='') as output_file:
    fc = csv.DictWriter(output_file,
                        fieldnames=s_list[0].keys(),

                       )
    fc.writeheader()
    fc.writerows(s_list)
