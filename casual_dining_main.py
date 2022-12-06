from bs4 import BeautifulSoup 
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import html5lib
from lxml import html
import re
import csv 


url = "https://www.newegg.com/p/pl?d=macbook"
soup = BeautifulSoup(url, 'html.parser')
content = soup.find('div', {"class": "item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell"})

page = ''
for i in content.find('Macbook'):
    #page = page + '' + i.text
    with open('scraped_text.txt', 'w') as file:
        file.write(page)


