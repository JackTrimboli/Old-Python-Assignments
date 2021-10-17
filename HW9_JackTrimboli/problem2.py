"""
Jack Trimboli
CS 100 2021S Section 108
HW 09, March 26th, 2021
"""


def file_stats(in_file):
    inFile = open(in_file, "r")
    lines = inFile.readlines()
    inFile.close()
    inFile = open(in_file, "r")
    text = inFile.read()
    words = text.split()

    print("Lines: " + str(len(lines)))
    print("Words: " + str(len(words)))
    print("Characters: " + str(len(text)))
