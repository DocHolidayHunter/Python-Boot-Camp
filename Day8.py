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
'''
def greet_name(name,loaction):
    print(f"How do you do {name}.")
    print(f"What is it like in {loaction}.")
    
greet_name(name = "Nick", loaction = "Melbourne")

'''

'''
import math 

def paint_calc(height, width, cover):
    area = height * width
    cans = math.ceil(area / coverage)

    print(f"You'll need {cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

'''
# Checking prime number program to further use key arguments.
'''

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            #not a prime
            is_prime = False
    if is_prime:
        print("It's a prime number. ")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)


'''


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:

    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")


from art import logo
print(logo)
should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")