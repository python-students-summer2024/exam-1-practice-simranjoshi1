"""
Your job is to complete the definitions of each function mentioned in the comments so that it achieves its indicated behavior.

Do not run this file directly.
Rather, call whichever functions defined in this file that you want to run from within the file named main.py and run that file directly.
"""

import random

##--------------------- Function #1 ---------------------##
# Define a function named 'get_random_int'.  
# This function accepts two arguments: a minimum value and a maximum value.
# The function must return a random integer between these two values, inclusive.
# Use the function random.randint() to generate the pseudo-random number.
def get_random_int(minnumber, maxnumber):
    return random.randint(minnumber, maxnumber)


##--------------------- Function #2 ---------------------##
# Define a function named 'get_guess'.
# This function accepts a single argument - an integer that serves as a max value.
# This function asks the user once to guess a random integer between 1 and the max value, inclusive.
# The function calls the function named get_random_int in order to generate the random integer in this range.
# If the user has entered an invalid response (i.e. anything that is not an integer in this range), the function returns an integer, -1.
# If the user has guessed the random integer correctly, this function returns a boolean True.
# If the user has guessed incorrectly, this function returns a boolean False.
def get_guess(integer):
    guess = input("Guess a random number between 1 and"+str(integer)+". ")
    randomvalue = get_random_int(1, integer)
    if guess.isdigit():
        guess = int(guess)
        if int(guess) < 1 or int(guess) > integer:
            return -1
        elif int(guess) == int(randomvalue):
            return True
        else:
            return False
    else:
        return -1 



##--------------------- Function #3 ---------------------##
# Define a function named 'play_game'.
# This function does not accept any arguments.
# This function uses the get_guess function to ask the user four times to guess a random integer between 1 and 5, inclusive.
# Each time the user guesses, they are immediately informed whether they guessed correctly or not, with the printed output, "Correct!" or "Wrong!"
# If at any time, the user enters an invalid response, the program immediately prints out the text, "Invalid response!" and does not print out anything further.
# At the end, the function, assuming the user has entered all valid guesses, the program prints out the percent of guesses that user guessed correctly, following the format: "You guessed 75% of the random numbers correctly."
def play_game():
    correct = 0
    guess1 = get_guess(5)
    if guess1 is True:
        print("Correct!")
        correct = correct + 1
    elif guess1 is False:
        print("Wrong!")
    else:
        print("Invalid response!")
        return
    guess2 = get_guess(5)
    if guess2 is True:
        print("Correct!")
        correct = correct + 1
    elif guess2 is False:
        print("Wrong!")
    else:
        print("Invalid response!")
        return
    guess3 = get_guess(5)
    if guess3 is True:
        print("Correct!")
        correct = correct + 1
    elif guess3 is False:
        print("Wrong!")
    else:
        print("Invalid response!")
        return
    guess4 = get_guess(5)
    if guess4 is True:
        print("Correct!")
        correct = correct + 1
    elif guess4 is False:
        print("Wrong!")
    else:
        print("Invalid response!")
        return
    
    correctpercentage = correct/4
    print("You guessed "+format(correctpercentage, '.0%')+" of the random numbers correctly.")