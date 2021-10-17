"""
Jack Trimboli
CS 100 2021S Section 108
HW 08, March 26th, 2021
"""


def twoWordsV2(length, firstLetter):
    res = []
    flag = True
    while flag:
        firstWord = input("Enter a " + str(length) + "-letter word: ")
        if len(firstWord) == length:
            res.append(firstWord)
            flag = False
    flag = True
    while flag:
        secondWord = input(
            "Enter a word that begins with the letter " + firstLetter + " please:"
        )
        if secondWord[0].lower() == firstLetter.lower():
            res.append(secondWord)
            flag = False
    return res


print(twoWordsV2(4, "C"))