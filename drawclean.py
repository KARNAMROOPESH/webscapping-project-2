import csv
from os import write
import pandas as pd


second=[]
with open("drawstarsclean.csv","r")as f:
    reader = csv.reader(f)
    for row in reader:
        second.append(row)

second.remove(second[0])

data = pd.read_csv('drawstarsclean.csv')
rdata = data['radius']
names = data['name']
dist = data['distance']
mdata = data['mass']

rvalues = []

radi = rdata[0]
values = radi*0.102763

radi1 = rdata[1]
values1 = radi1*0.102763

radi2 = rdata[2]
values2 = radi2*0.102763

radi3 = rdata[3]
values3 = radi3*0.102763

radi4 = rdata[4]
values4 = radi4*0.102763

radi5 = rdata[5]
values5 = radi5*0.102763

rvalues.append(values)
rvalues.append(values1)
rvalues.append(values2)
rvalues.append(values3)
rvalues.append(values4)
rvalues.append(values5)
print(rvalues)

mvalues = []

madi = mdata[0]
valuesm = float(madi)*0.000954588


madi1 = mdata[1]
values1m = float(madi1)*0.000954588

madi2 = mdata[2]
values2m = float(madi2)*0.000954588

madi3 = mdata[3]
values3m = float(madi3)*0.000954588

#madi4 = mdata[4]
#values4m = float(madi4)*0.000954588
#print(madi3)

madi5 = mdata[5]
values5m = float(madi5)*0.000954588

mvalues.append(valuesm)
mvalues.append(values1m)
mvalues.append(values2m)
mvalues.append(values3m)
mvalues.append(0)
mvalues.append(values5m)
print(mvalues)

df = pd.DataFrame(list(zip(names , dist , mvalues , rvalues ,)) , columns = ["name","distance","mass","radius"] )


df.to_csv('drawstarscomplete.csv',index=False)
