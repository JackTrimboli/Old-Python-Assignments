"""
Jack Trimboli
CS 100 2021S Section 108
HW 09, March 26th, 2021
"""


def file_copy(in_file, out_file):
    inFile = open(in_file, "r")
    outFile = open(out_file, "w")
    for line in inFile:
        outFile.write(line)
    inFile.close()
