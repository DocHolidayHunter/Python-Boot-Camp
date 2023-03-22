# Day 5 works on loops, range and code blocks
# Different types of for loops
import random
"""

games = ["Skyrim", "Minecraft"]
for game in games: # takes and assigns a variable to the list so game = skyrim as the first and the second then equals Minecraft
    print(game)
    print(game + " is cool")

"""

"""
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)



high_score = 0
for score in student_scores:
    if score > high_score:
       high_score = score

print(f"The highest score in the class is: {high_score}")
"""

# We've only used these for lists so far, but we can use these for much more independently.
# This uses gaus' technique of adding numbers up to 101 
# We can use the range fucntion to search a range of numbers to be used.
"""
total = 0
for numb in range(1,101):
    total += numb
    
print(total)

"""
# This checks to see if the number is even and then adds it to the final total
"""
total = 0
for numb in range(1,101):
    if numb % 2 == 0:
        total += numb

print(total)
"""
# This is another way to check what we previously had found and this allows us to see what we can do with range and for loops 
"""
for number in range(1,101):
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)

"""

# Password generator problem

#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for char in range(1, nr_letters + 1):
    password += random.choice(letters)
    print(password)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
    print(password)
    
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
    print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P