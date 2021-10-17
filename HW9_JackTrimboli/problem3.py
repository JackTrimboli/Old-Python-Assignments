"""
Jack Trimboli
CS 100 2021S Section 108
HW 09, March 26th, 2021
"""

import string


def repeat_words(in_file, out_file):
    inFile = open(in_file, "r")
    outFile = open(out_file, "w")
    for line in inFile:
        occurred = []
        nextLine = ""
        for words in line.split():
            words = words.lower().strip(string.punctuation)
            if words in occurred and words not in nextLine.split():
                nextLine += words + " "
            occurred.append(words)
        outFile.write(nextLine + "\n")
