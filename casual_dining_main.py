from bs4 import BeautifulSoup
import requests

#function to explain the program
def dining_types():
    print("This program will find all the type of restaurant's from your input")
dining_types()


#web scraping function for dinning types.
#-cjosh
def webscrape_dinning_types():
    from bs4 import BeautifulSoup 
    import requests
    url = "http://ajax.googleapis.com/ajax/services/search?rlz=1C1CHBF_enUS916US916&sxsrf=ALiCzsblr3vdeNM7Crb2YxKcokERB8vrIQ:1669440028825&q=North+Italia&ludocid=1882766253883301680&gsas=1&lsig=AB86z5UbFiwXMXCE3pI1C6IeWY-5&sa=X&ved=2ahUKEwj5_pDfjMv7AhXvm2oFHXTcCq8QhecIegQIahAN&biw=2560&bih=1307&dpr=1"
    result = requests.get(url).text 
    doc = BeautifulSoup(result, "html.parser") 
    span = doc.span
    print(span)    
webscrape_dinning_types()  


#function to find the dining type from user input
def find_restaurant():
    type = input("What kind of restaurant do you want to find? " )
    output = str("Here is a list of the " + type + " restaurants within a 10 mile radius of your area")
    print(output)
find_restaurant()


