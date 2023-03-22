# Day 4 focuses on Randomness
import random # MAIN MODULE FOR DAY 4


'''
r_int = float(random.randint(1,10))
print(r_int)

r_float = random.random()
print(r_float)

r_float * 5 # Makes this a random number that is a float -- expands range

'''
# Simple program which prints heads or tails using random
"""
toss = random.randint(1,2)

if toss == 1:
    print("Tails")
else:
    print("Heads")

"""

# Lists are an essential core to programming 
# Starting at 0 to count up 
"""
state = ["Victoria","Queensland","Sydney","Adelaide","Canberra"]

# First index of the list 
print(state[0])

# Last index of the list 
print(state[-1])

# To append the list 
state[1] = "Victorian"
print(state)

# To add a new state
state.append("Oonga")
print(state)

state.extend(["Nothern Territory", "My Land"])
print(state)

"""
# Bill picker

"""
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

items = len(names)
random = random.randint(0, items - 1)

unlucky_pick = names[random]

print(unlucky_pick + " is going to by the meal today. ")
"""
# Most common error is index out of range error.

# Nested lists 
"""
veggies = ["Cucumber", "Eggplants"]
fruits = ["Apples, Strawbs"]

nested = [fruits, veggies]
print(nested)
"""

# This is a way of showing how to change a nested list to insert and "x" to a row and column
"""

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0]) 
vertical = int(position[1])

selected_row = map[vertical - 1]

selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

    
"""


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")