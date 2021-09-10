import csv
from os import write
import pandas as pd

first=[]
with open("brightstars.csv","r")as f:
    reader = csv.reader(f)
    for row in reader:
        first.append(row)

second=[]
with open("drawstarscomplete.csv","r")as f:
    reader = csv.reader(f)
    for row in reader:
        second.append(row)

second.remove(second[0])
second.remove(second[4])

final = first+second

with open("stars.csv","a+")as f:
    writer = csv.writer(f)
    writer.writerows(final)

