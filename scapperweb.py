import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver

DATAURL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome("chromedriver")
browser.get(DATAURL)

time.sleep(10)

def scrap():
    headers = ["name","distance","mass","radius"]

    planetdata = [ ]

    for i in range(1,90):
        soup = BeautifulSoup(browser.page_source , "html.parser")

        for trtag in soup.find_all("tr"):
            tdtags = trtag.find_all("td")
            temp=[ ]
            for index,tdtag in enumerate(tdtags):
                
                if index == 1 : 
                    try:
                        temp.append(tdtag.text.rstrip())
                    except:
                        temp.append(" ")
                if index == 3 :
                    try:
                        temp.append(tdtag.text.rstrip())
                    except:
                        temp.append(" ")
                if index == 5 :
                    try:
                        temp.append(tdtag.text.rstrip())
                    except:
                        temp.append(" ")
                if index == 6 :
                    try:
                        temp.append(tdtag.text.rstrip())
                    except:
                        temp.append(" ")
                    
            planetdata.append(temp)
          

    with open("data.csv","w")as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(planetdata)

scrap()

    



