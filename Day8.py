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

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

    # TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(plain_text=text, shift_amount=shift)
