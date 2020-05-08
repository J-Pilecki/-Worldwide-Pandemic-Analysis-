import urllib
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import urllib.request, urllib.parse, urllib.error
import ssl
from matplotlib import pyplot as plt
import numpy as np

#using requests module access the webpage
result = requests.get("https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?")
#print(result.status_code) #check that website was accessible, 200 = access
src = result.content #store the page content in a variable
soup = BeautifulSoup(src)  #create a BS object for later parsing
#total_cases = soup.find("div", "maincounter-number")
#total_cases = total_cases.text
#print('total cases of covid-19:')
#print(total_cases)  

all_divs = soup.find_all("div", "maincounter-number")
#covid_total_cases = all_divs[0]
#covid_total_deaths = all_divs[1]
#covid_total_recovered = all_divs[2]

numbers = []
for i in all_divs:
    i = i.get_text()
    i = i.replace("\n","").replace(" ", "").replace(",","")
    numbers.append(i)
covid_total_cases = int(numbers[0])
covid_total_deaths = int(numbers[1])
covid_total_recovered = int(numbers[2])
#covid_total_cases = covid_total_cases.replace(",", "")
#covid_total_deaths = covid_total_deaths.replace(",", "")

print('data from: https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?')
print('total cases of COVID-19:')
print(covid_total_cases)
print('total deaths from COVID-19:')
print(covid_total_deaths)
print('total recovered from COVID-19:')
print(covid_total_recovered)


result = requests.get("https://www.cdc.gov/flu/pandemic-resources/1918-pandemic-h1n1.html")
src = result.content
soup = BeautifulSoup(src)
spanflu = soup.get_text("div", "mt-4 col-md-6")
span_total_cases = 500000000
span_total_deaths = 50000000
print('data from: https://www.cdc.gov/flu/pandemic-resources/1918-pandemic-h1n1.html')
print('\ntotal cases of 1918 Spanish flu H1N1:\n')
print(span_total_cases)
print('\ntotal estimated deaths of 1918 Spanish flu 1918:\n')
print(span_total_deaths)
#print(spanflu)

print('\ndata from: https://pubmed.ncbi.nlm.nih.gov/21850217/ and https://www.who.int/csr/don/2010_08_06/en/ \n')
swine_total_cases = 350000000 #(1400000000 - 700000000) / 2
swine_total_deaths = 284000
print('total cases of 2009 Swine flu H1N1:\n') 
print(swine_total_cases)
print('\ntotal deaths of 2009 Swine flu H1N1:\n') 
print(swine_total_deaths)

print('\ndata from: https://web.archive.org/web/20190329172619/https://files.unaids.org/en/media/unaids/contentassets/documents/unaidspublication/2011/JC2216_WorldAIDSday_report_2011_en.pdf')
hiv_total_cases = 1800000 #(35200000 - 31600000) / 2 #average of estimates
hiv_total_deaths = 150000 #int((1900000 - 1600000) / 2)
print('\ntotal cases of HIV in 2010:\n')
print(hiv_total_cases)
print('\ntotal deaths of HIV in 2010:\n')
print(hiv_total_deaths)

#for reference
#span_total_cases = 500,000,000
#span_total_deaths = 50,000,000
#swine_total_cases = 350,000,000 
#swine_total_deaths = 284,000
#hiv_total_cases = 1,800,000
#hiv_total_deaths = 150,000 

print('deaths/contractions = case fatality')
span_CF = 0.1
swine_CF = 0.0008
hiv_CF = 0.08
covid_CF = covid_total_deaths/covid_total_cases
print('spanish flu case fatality: ')
print(span_CF)
print('swine flu case fatality: ')
print(swine_CF)
print('hiv case fatality: ')
print(hiv_CF)
print('coronavirus case fatality: ')
print(covid_CF)

dev_x = ['spanish flu', 'hiv', 'swine flu', 'coronavirus']
dev_y = [span_CF, hiv_CF, swine_CF, covid_CF]
plt.bar(dev_x, dev_y)
plt.show()

#black_death_total_death = (200000000 - 75000000) / 2
#print('\nblack death total deaths:\n')
#print(black_death_total_death)



