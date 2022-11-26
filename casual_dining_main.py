#function to explain the program
def dining_types():
    print("This program will find all the type of restaurant's from your input")
dining_types()

#function to find the dining type from user input

def find_restaurant():
    type = input("What kind of restaurant do you want to find? " )
    output = str("Here is a list of the " + type + " restaurants within a 10 mile radius of your area")
    print(output)
find_restaurant()


