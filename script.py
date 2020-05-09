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
plt.xlabel('Pandemics')
plt.ylabel('Case Fatality')
plt.title('Pandemic Case Fatality: (deaths/contractions) = CF')
plt.bar(dev_x, dev_y)
plt.show()

#source: https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports
jan21, jan22, jan23, jan24, jan25, jan26, jan27, jan28, jan29, jan30, jan31 = 282, 314, 581, 846, 1320, 2014, 2798, 4593, 6065, 7818, 9826
dev_janx = ['Jan 21', 'Jan 22', 'Jan 23', 'Jan 24', 'Jan 25', 'Jan 26', 'Jan 27', 'Jan 28', 'Jan 29', 'Jan 30', 'Jan 31']
dev_jany = [jan21, jan22, jan23, jan24, jan25, jan26, jan27, jan28, jan29, jan30, jan31]
plt.plot(dev_janx, dev_jany, color = "#444444")
plt.title('Worldwide Coronavirus cases in January 2020')
plt.xlabel('Days')
plt.ylabel('Cases')
plt.grid(True)
plt.show()

feb1, feb2, feb3, feb4, feb5, feb6, feb7, feb8, feb9, feb10, feb11, feb12, feb13, feb14, feb15, feb16, feb17, feb18, feb19, feb20, feb21, feb22, feb23, feb24, feb25, feb26, feb27, feb28, feb29 = 11953, 14557, 17391, 20630, 24554, 28276, 31481, 34886, 37558, 40554, 43103, 45171, 46997, 49053, 50580, 51857, 71429, 73332, 75204, 75748, 76769, 77794, 78811, 79331, 80239, 81109, 82294, 83652, 85403
dev_feb1x = ['Feb 1', 'Feb 2', 'Feb 3', 'Feb 4', 'Feb 5', 'Feb 6', 'Feb 7', 'Feb 8', 'Feb 9', 'Feb 10', 'Feb 11', 'Feb 12', 'Feb 13', 'Feb 14']
dev_feb1y = [feb1, feb2, feb3, feb4, feb5, feb6, feb7, feb8, feb9, feb10, feb11, feb12, feb13, feb14]
plt.plot(dev_feb1x, dev_feb1y)
plt.title('Worldwide Coronavirus cases in February 1 - 14, 2020')
plt.xlabel('Days')
plt.ylabel('Cases')
plt.grid(True)
plt.show()

dev_feb2x = ['Feb 15', 'Feb 16', 'Feb 17', 'Feb 18', 'Feb 19', 'Feb 20', 'Feb 21', 'Feb 22', 'Feb 23', 'Feb 24', 'Feb 25', 'Feb 26', 'Feb 27', 'Feb 28', 'Feb 29']
dev_feb2y = [feb15, feb16, feb17, feb18, feb19, feb20, feb21, feb22, feb23, feb24, feb25, feb26, feb27, feb28, feb29]
plt.plot(dev_feb2x, dev_feb2y)
plt.title('Worldwide Coronavirus cases in February 15 - 29, 2020')
plt.xlabel('Days')
plt.ylabel('Cases')
plt.grid(True)
plt.show()

mar1, mar2, mar3, mar4, mar5, mar6, mar7, mar8, mar9, mar10, mar11, mar12, mar13, mar14, mar15, mar16, mar17, mar18, mar19, mar20, mar21, mar22, mar23, mar24, mar25, mar26, mar27, mar28, mar29, mar30, mar31 = 87137, 88948, 90870, 93091, 95324, 98189, 101924, 105586, 109577, 113702, 118319, 125260, 132758, 142534, 153517, 167499, 179104, 191122, 209842, 234073, 266072, 292136, 332924, 372749, 413461, 462680, 509164, 571676, 634825, 693212, 750867
dev_mar1x = ['Mar 1', 'Mar 2', 'Mar 3', 'Mar 4', 'Mar 5', 'Mar 6', 'Mar 7', 'Mar 8', 'Mar 9', 'Mar 10', 'Mar 11', 'Mar 12', 'Mar 13', 'Mar 14', 'Mar 15']
dev_mar1y = [mar1, mar2, mar3, mar4, mar5, mar6, mar7, mar8, mar9, mar10, mar11, mar12, mar13, mar14, mar15]
plt.plot(dev_mar1x, dev_mar1y)
plt.title('Worldwide Coronavirus cases in March 1 - 15, 2020')
plt.xlabel('Days')
plt.ylabel('Cases')
plt.grid(True)
plt.show()

dev_mar2x = ['Mar 16', 'Mar 17', 'Mar 18', 'Mar 19', 'Mar 20', 'Mar 21', 'Mar 22', 'Mar 23', 'Mar 24', 'Mar 25', 'Mar 26', 'Mar 27', 'Mar 28', 'Mar 29', 'Mar 30', 'Mar 31']
dev_mar2y = [mar16, mar17, mar18, mar19, mar20, mar21, mar22, mar23, mar24, mar25, mar26, mar27, mar28, mar29, mar30, mar31]
plt.plot(dev_mar2x, dev_mar2y)
plt.title('Worldwide Coronavirus cases in March 16 - 31, 2020')
plt.xlabel('Days')
plt.ylabel('Cases')
plt.grid(True)
plt.show()




#black_death_total_death = (200000000 - 75000000) / 2
#print('\nblack death total deaths:\n')
#print(black_death_total_death)

