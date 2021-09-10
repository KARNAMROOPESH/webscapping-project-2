import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import pandas as pd

DATAURL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(DATAURL)

soup = BeautifulSoup(page.text,'html.parser')

tables = soup.find_all('table')

temp = []

tablerows = tables[3].find_all('tr')

for tr in tablerows :

    tdtag = tr.find_all('td')
    row = [i.text.rstrip() for i in tdtag]
    temp.append(row)

name = []
dist = []
mass = []
radius = []

for i in range(1,len(temp)):
    name.append(temp[i][0])
    dist.append(temp[i][5])
    mass.append(temp[i][8])
    radius.append(temp[i][9])

df = pd.DataFrame(list(zip(name , dist , mass , radius ,)) , columns = ["name","distance","mass","radius"] )

nan_value = float("NaN")
df.replace("", nan_value, inplace=True)
df.dropna(subset = ["radius"], inplace=True)
print(df)

df.to_csv('drawstarsclean.csv',index=False)