"""
Jack Trimboli
CS 100 2021S Section 108
HW 08, March 26th, 2021
"""


import random


def guessNumber():
    randNumber = random.randint(0, 50)
    print("I'm thinking of a number in the ran 0-50. You have five tries to guess it.")
    for x in range(5):
        guess = int(input("Guess " + str(x + 1) + ":"))
        if guess < randNumber:
            print("Too low!")
        if guess > randNumber:
            print("Two high!")
        if guess == randNumber:
            print("You are right! I was thinking of " + str(guess) + "!")
    print("Nice try, the answer was: " + str(randNumber))


guessNumber()
