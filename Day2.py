# Data Types...
'''
Strings - "Hello"

Index - "Hello"[3] will grab H as we work in binary... starting from 0 going up

Integer - print(231+312) Whole number (No decimal places) e.g 421

Float - Floating point e.g 3.14

Boolean - True or False (Case sensetive)

type() - Checks type of datas
'''

# Convert a Var int to a string
'''

num = len(input("What's your name"))
new_num = str(num)
print("Name " + new_num + "is this long")


'''

# A program which splits the initial number and add its together e.g 15 = 1 + 5 
'''

two_digit_number = input("Type a two digit number: ")


first = two_digit_number[0]
second = two_digit_number[1]

num_first = int(first)
num_second = int(second)

print(int(first) + int(second))
'''

# BMI Calculator to show off how to convert an int to a float and demonstrate PEDMAS In python
'''

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


bmi = int(weight) / float(height) ** 2
# Need this to convert float to int to print correctly instead of not having a rounded number
bmi_int = int(bmi)

print(bmi_int)
'''

# fstring can remove manual labour of having to feed in int values using + signs and can be replaced using {}
'''

age = input("What is your current age? ")

int_age = int(age)

years_remaining = 90 - int_age

days_left = years_remaining * 365

weeks_left = years_remaining * 52

years_left = years_remaining * 12


print(f"You have {days_left} days, {weeks_left} weeks, and {years_left} left.")
'''

# Tying day 2 together creating a tip calculator
# This 
'''

print("Welcome to the Tip Calculator")

bill_amount = float(input("How much was the bill: "))
people = int(input("How many people ate: "))
tip_amount = int(input("What would you like the tip to be? 10, 12 or 15 "))


total = tip_amount / 100 * bill_amount + bill_amount

bill_per_person = total / people

print(f"Your total tip amount is equal to: {total} and per person comes to: {bill_per_person}")
'''