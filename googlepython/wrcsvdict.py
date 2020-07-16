import os
import csv

os.remove("softare.csv")
users=[
{"name":"Aman","usernumber":"1","version":"5.34"},
{"name":"Euhid","usernumber":"2","version":"1.25"},
{"name":"ChickenWing","usernumber":"3","version":"0.34"}
]

keys=["name","usernumber","version"]

with open("software.csv","w") as file:
    writer=csv.DictWriter(file,fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)


