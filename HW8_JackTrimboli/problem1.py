"""
Jack Trimboli
CS 100 2021S Section 108
HW 08, March 26th, 2021
"""


def twoWords(length, firstLetter):
    res = []
    while True:
        firstWord = input("Enter a " + str(length) + "-letter word: ")
        if len(firstWord) == length:
            res.append(firstWord)
            break
    while True:
        secondWord = input(
            "Enter a word that begins with the letter " + firstLetter + " please:"
        )
        if secondWord[0].lower() == firstLetter.lower():
            res.append(secondWord)
            break
    return res


print(twoWords(4, "C"))