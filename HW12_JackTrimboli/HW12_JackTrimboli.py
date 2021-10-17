"""
Jack Trimboli
CS 100 2021S Section 108
HW 12, April 30th, 2021
"""


def safeOpen(inFile):
    try:
        f = open(inFile, "r")
        return f
    except IOError:
        print("File does not exist!")


def safeFloat(myValue):
    try:
        return float(myValue)

    except ValueError:
        print("The value '" + myValue + "' could not be converted to a float.")


def averageSpeed():
    trys = 0
    avg = 0
    total = 0
    count = 0

    while trys != 2:
        fileName = input("Enter Filename: ")
        inputFile = safeOpen(fileName)
        if not inputFile:
            print("please try again.")
            trys += 1
        else:
            break
    if (
        not inputFile
    ):  # if we reached this point and the file does not exist, we exceeded the two-try limit.
        print("Operation Failed. Programed exited.")
        exit()

    for line in inputFile:  # for each line in the file
        # check each num on each line (regex is an empty space)
        for num in line.split():
            # use the safeFloat function to safely convert the string to a floating point value
            num = safeFloat(num)
            if num and num > 2:  # if the number is valid and greater than 2
                count += 1
                total += num
    try:
        avg = total / count
    except ZeroDivisionError:
        print("No valid floats in the list!")
    print("The average speed is " + str(round(avg, 2)) + " miles per hour.")
    return avg


# function tests
f = safeOpen("ghost.txt")
myFloat = safeFloat("abc")
averageSpeed()
