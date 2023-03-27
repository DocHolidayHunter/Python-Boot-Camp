# The project we are working on today will be to make a caesar cipher.
# Functions with inputs and Arguments and Paramaters.\



    
"""
def greet():
    print("Welcome")
    print("Booga")
    print("Ooga")   
greet()
"""
# Function that allows for us to use an input to pass it over.
# Can use difference variables to make multi - variable inputs.
# This is a positional argument 

# def greet_name(name,loaction):
#    print(f"How do you do {name}.")
#    print(f"What is it like in {loaction}.")

# This is a keyword argument which is where we assign a key to the word so that we can use it in any order.
def greet_name(name,loaction):
    print(f"How do you do {name}.")
    print(f"What is it like in {loaction}.")
    
greet_name(name = "Nick", loaction = "Melbourne")

import math 

def paint_calc(height, width, cover):
    area = height * width
    cans = math.ceil(area / coverage)

    print(f"You'll need {cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)



