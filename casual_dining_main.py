#from bs4 import BeautifulSoup
#import requests
#import re

#function to explain the program
#def dining_types():
    #print("This program will find all the type of restaurant's from your input")


#web scraping function for dinning types.
#-cjosh
def webscrape_dinning_types():
    from bs4 import BeautifulSoup 
    import requests
    from lxml import html
    url = "https://www.newegg.com/p/pl?d=macbook"
    tree = html.fromstring(page.content) 
    result = requests.get(url).text 
    macbook_type = tree.xpath('//a[@title="View Details"]/text()')


    print(macbook_type)



 



#function to find the dining type from user input
#def find_restaurant():
 #   type = input("What kind of restaurant do you want to find? " )
  #  output = str("Here is a list of the " + type + " restaurants within a 10 mile radius of your area")
   # print(output)
#find_restaurant()


