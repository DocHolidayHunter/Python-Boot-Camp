# Hashes Turn into comments
# Make code as simple as Possible 

# This is a function to print a phrase and then take and input 
# from the user to then feed into the print string after
'''
print("Welcome! " + input("Enter your names: "))
'''

# This is a simple ask your name and convert it into an integer
''' 
string = input("what is your name? Enter name here ")
print('Your name is equal to this many letters!')
print(len(string))
'''

# Variables can store information that can be refered to in the future
# Variables can come into two sets: Global and Local - More about this later.
"""
string = input("what is your name? Enter name here ")
print(string)
"""
#Simple Switch of variables

"""
a = input("a: ")
b = input("b: ")

# This is where the change occurs for the switching of a and b

c = a
a = b
b = c 


print("a: " + a)
print("b: " + b)
"""

# Tying it all together for Day 1 
'''
print("Welcome... to the Band Name Generator!!")
city = input(" First Question.. What city did you grow up in: ")
pet = input("Second Question.. What is your pets name: ")

print("Your band name is Loading....")
print(city + pet)
'''