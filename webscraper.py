#python program to perform web scrapping using requests and beaurifulsoup modules
import requests
from bs4 import BeautifulSoup
import re

#GET request whose output is then parsed through html parser
mainpage=requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup=BeautifulSoup(mainpage.content, "html.parser")

#By analyzing the html code, providing the CSS selectors to select the particular data to scrap
periods=soup.select("div.tombstone-container p.period-name")
periodlist=[x.get_text() for x in periods]
print(periodlist)

short_desc=soup.select("div.tombstone-container p.short-desc")
shortdesclist=[y.get_text() for y in short_desc]
print(shortdesclist)

temp=soup.select("div.tombstone-container p.temp")
templist=[z.get_text() for z in temp]
print(templist)

desc=soup.select("div.tombstone-container p img")
desclist=[w['title'] for w in desc]
print(desclist)

#Now after this we can use the lists and the regex to analyze the data
#Here now we will calculate the mean of all the temperatures that are going to occur in the future and are occuring now
avgtemp=re.compile("[\d]+\.?[\d]+ ")
avgsum=0
for i in templist:
    avgsum+=int(avgtemp.findall(i)[0])
avg=avgsum/len(templist)
print("Average Temperature is %f"% avg)