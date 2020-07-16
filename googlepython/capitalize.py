import sys

filename=sys.argv[1]

with open(filename) as file:
    for line in file:
        line=line.strip()
        line=line.capitalize()
        print(line)
