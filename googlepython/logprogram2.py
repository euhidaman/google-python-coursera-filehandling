# *****************DO NOT EXECUTE*****************
#incorrect program----answer asked in stackoverflow
#this program converts data stored in "sourcetimes.txt" into a csv file
#the output is stored in "sourcetimes2.csv"

import csv
import os
import sys

sourcefile=sys.argv[1]

keys=["source","times"]

with open("sourcetimes2.csv","w") as file:
    writer=csv.DictWriter(file,fieldnames=keys)
    writer.writeheader()
    writer.writerows(sourcefile)
