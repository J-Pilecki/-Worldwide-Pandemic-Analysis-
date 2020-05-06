import urllib
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import urllib.request, urllib.parse, urllib.error
import ssl

#using requests module access the webpage
result = requests.get("https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?")
#print(result.status_code) #check that website was accessible, 200 = access
src = result.content #store the page content in a variable
soup = BeautifulSoup(src)  #create a BS object for later parsing
total_cases = soup.find("div", "maincounter-number")
total_cases = total_cases.text
#print('total cases of covid-19:')
#print(total_cases)  

all_divs = soup.find_all("div", "maincounter-number")
total_cases = all_divs[0]
total_deaths = all_divs[1]
total_recovered = all_divs[2]

numbers = []
for i in all_divs:
    i = i.get_text()
    numbers.append(i)
total_cases = numbers[0]
total_deaths = numbers[1]
total_recovered = numbers[2]
print('total cases of COVID-19:')
print(total_cases)
print('total deaths from COVID-19:')
print(total_deaths)
print('total recovered from COVID-19:')
print(total_recovered)


result = requests.get("https://www.cdc.gov/flu/pandemic-resources/1918-pandemic-h1n1.html")
src = result.content
soup = BeautifulSoup(src)
spanflu = soup.get_text("div", "mt-4 col-md-6")
print(spanflu)

'''
#spanish flu h1n1
#using requests module access the webpage
result = requests.get("https://en.wikipedia.org/wiki/Spanish_flu")
src = result.content #store the page content in a variable
soup = BeautifulSoup(src)  #create a BS object for later parsing
spanflu = soup.findAll("table", "infobox")
#print(spanflu)
#split up by table row or table data

'''




