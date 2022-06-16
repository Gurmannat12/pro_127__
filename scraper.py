from turtle import distance
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import csv


START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page_source = requests.get(START_URL)
soup = bs(page_source.text,'html.parser')

star_table = soup.find('table')
temp_list= []
rows = star_table.find_all('tr')

for tr_tag in rows:
    td_tags = tr_tag.find_all('td')
    row = [i.text.rstrip() for i in td_tags]
    temp_list.append(row)

star_names = []
dist = []
mass = []
radius = []
lum = []

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    dist.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    lum.append(temp_list[i][7])

df2 = pd.DataFrame(list(zip(star_names, dist, mass, radius, lum)), columns = ['Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity'])
df2.to_csv("star.csv")