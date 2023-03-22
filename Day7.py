# Hangman challenge using Python
import random
# This is the initial code that starts us with a word and assigns it to the 
word_list = ["Trust", "Implode", "Monkey"]
chosen_word = random.choice(word_list)

display = []

for letter in chosen_word:
    print("_")

guess = input("Guess a letter and see if it's in the word: ").lower

for letter in chosen_word:
    if letter == chosen_word:
        print("Right")
    else:
        print("Wrong")




