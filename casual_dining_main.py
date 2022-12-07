from bs4 import BeautifulSoup 
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import html5lib
from lxml import html
import re
import csv 

import requests

url = "https://www.newegg.com/p/pl?d=macbook"
soup = BeautifulSoup(url, 'html5lib')
r = requests.get(url)

#macbooks=[] #a list to store macbooks 

content = soup.findAll('div', {"class": "item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell"})
pattern = 'Macbook'
title = soup.find_all('a', text = pattern)
print(title)




