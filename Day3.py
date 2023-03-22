# If Else Statements are represented like this 
# This can be known as an overflow statement also 
'''

if condtion:
    do this
else:
    do this 
'''

# In referenece to this being a coffee cup that is being overflown with coffee,
# we can write a snippet of code which tells the machine when to stop the coffee pour.
'''
c_shot = 10

if c_shot >= 30:
    stop_pour
else:
    pour
'''

# Another example can be a roller coaster asking for height to ride.
# One = sign means that we are assigning to a variable while == is checking if it is equal to the number assigned.
'''

print(" Welcome to the ride!")
height = int(input("How tall are you in cm: "))

if height >= 100: # 
    print("Hop on in!") # This part is the true part 
else:
    print("Your too short to ride! Maybe next time...") # This is the false part
'''

# A simple even or odd check using modulo and an if statement
'''

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")
'''

# Checking for age and height using nested if statement 
# This can be used to check multiple variables for an instance.

'''
print(" Welcome to the ride!")
height = int(input("How tall are you in cm: "))
age = int(input("How old are you in years: "))

if height >= 100:
    if age > 11-17:
        print("This ride costs $7")
    elif age < 12:
        print(" The ride will cost $5")
    elif age >= 18:
        print(" The ride will cost $12")
    else:
        print("Not old enough! ")
else:
    print("Sorry your not tall enough to ride")
'''
# Updated to use if else statements to check bmi 
'''

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


bmi = round(int(weight) / float(height) ** 2)

bmi_int = int(bmi)

if bmi_int < 18.5:
    print(f"Your BMI is {bmi_int}, you are underweight.")
elif bmi_int < 25:
    print(f"Your BMI is {bmi_int}, you have a normal weight.")
elif bmi_int < 30:
    print(f"Your BMI is {bmi_int}, you are slightly overweight.")
elif bmi_int < 35:
    print(f"Your BMI is {bmi_int}, you are obese.")
elif bmi_int > 35:
    print(f"Your BMI is {bmi_int}, you are clinically obese.")
'''

# Combining Modulo and nested for loops to create a leap year checker
'''

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print ("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")

'''

# Using Multiple if statements in succession 
# Addding a global variable to the rollercoaster so that we can now charge a bill to the photo charge.
'''
print(" Welcome to the ride!")
height = int(input("How tall are you in cm: "))
age = int(input("How old are you in years: "))
bill = 0


if height >= 100:
    if age > 11-17:
        bill = 7
        print("This ride costs $7")
        
    elif age < 12:
        bill = 5
        print(" The ride will cost $5")
        
    elif age >= 18:
        bill = 12
        print(" The ride will cost $12")
        
    else:
        print("Not old enough! ")
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3 # += is bill = bill + 3
        print(f"The final bill is ${bill}")
    else:
        print(F"The final bill is ${bill}")
else:
    print("Sorry your not tall enough to ride")
    
'''
# Buidling my own pizza store using what i've learnt
# Can simply this to just these statements instead of printing everything

'''print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0


if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
    
print(f"Your final bill is ${bill}")

'''
# Logical Operators
# A and B is used for when both variables are true and is false when one is false
# Or Operator can be used for when A or B is true or false.
# This extends until both values are false which then means that the overall is false
# Not operator reverses a condition so A becomes B which is true but when B becomes A it's False
# Below is the rollercoaster situation but we are adding a new part for 45 - 55 year olds

'''
print(" Welcome to the ride!")
height = int(input("How tall are you in cm: "))
age = int(input("How old are you in years: "))
bill = 0


if height >= 100:
    if age <= 18: 
        bill = 7
        print("The ticket is $7")
        
    elif age < 12:
        bill = 5
        print("The ticket is $5")
    elif age >= 45 and age <= 55: # Added statement for and 
        bill = 0
        print(" Mid life crisis alert....")    
    else:
        bill = 12
        print("The ticket is $12")
        
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3 # += is bill = bill + 3
        print(f"The final bill is ${bill}")
else:
    print("Sorry your not tall enough to ride")
    
'''

# Issues i struggled with was that i didn't know how to get the love and true to combine
# This led me to look at the solution which wasn't a good idea until i had a crack at it.
# Sorted it out after that part as i finished the if statements by myself and figured out 
# The str to int error in line 236

'''
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


combined_string = name1 + name2
lower_case_string = combined_string.lower()


t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")

'''

# Tying it all together making a small game.
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice_1 = input("You stumble across a road which heads right or left... Do you want to go right or left: ").lower()

if choice_1 == "left":
        Choice_2 = input("After a long journey you come across a crossing which is flooded. \n You can either swim or wait: ").lower()
        if Choice_2 == "swim":
            print("You just swam to your DEATH!")
        else:
            choice_3 = input("You stumble into a field with a strange house... \n There are three doors which are red, blue and yellow.. Choose a door: ").lower()
            if choice_3 == "yellow":
                print("You get sucked into the void forever chasing sunflowers.")
            elif choice_3 == "red":
                print("Suck it loser.")
            elif choice_3 == "blue":
                print("Winner Winner Chicken Dinner!")
            else:
                print("You chose no door.. Game over.")
                
else:
    print("GAME OVER!")
    
