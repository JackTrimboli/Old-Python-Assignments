#Jack Trimboli
#CS 100 2021S Section 108
#HW 01, January 22, 2021

#5
#b
months = 12

#My three integer assignment lines for 5b:
days = 1
hours = 24
minutes = 1440

#c
#My three float assignment lines for 5c:
reallyComplicatedNumber = 231.2354123
pi = 3.14
myFloat = 2.23

#d
#My three string assignment lines for 5d:
myDogsName = "Moose"
myBrothersName = "Daniel Trimboli"
myBirthday = "March 2nd, 1999"

#1.1

#1
#print"Hello, world!")
#You get a syntax error

#2
#print(hello world) (My test code)
#NameError: name 'hello' is not defined
#You get a runtime error where the compiler tries to recognize the word 'hello' 
#as a variable rather than a string, but this variable does not exist

#3
#2++2
#You get a syntax error

#4
#print(011)
#you get a syntax error

#5
#print(1 1)
#if you have two values with no operator inbetween them you get a syntax error

#1.2
#1
seconds = 42 * 60 + 42

#2
#miles = Xkm/1.61
miles = 10/1.61

#3

#time per mile = ((seconds)/(number of miles))/(60)
timePerMile = ((42*60+42)/(10/1.61)/ 60)
#miles per hour = (60 mins in an hour) / (time per mile in minutes)
milesPerHour =  60 / timePerMile
print("Average Pace: " + str(timePerMile) + " \nMPH:" + str(milesPerHour))
#average pace is 6:52, mph is 8.73

#2.1
    # 42 = n is illegal because the variable name must be on the left side of the assignment
    # x = y = 1 is legal, x is set to the value of y which is set to the value of 1
    # In python, a semi colon denotes the separation of two statements, and would be used if someone wanted to put two statements on the same line
    # If you added a period to the end of a statement, you would get a syntax error.
    # If you try to write x * y as 'xy' in python, you would get a syntax error. This is because python will consider it to be its own separate variable but that variable does not exist or hasn't been declared



#2.2
#1
pi = 3.14159
volumeOfASphere = (4/3) * pi * 5**3
print(volumeOfASphere)

#2
priceOfBook = 24.95
discount = 0.6
numCopies = 60
shippingCost = (numCopies-1) * .75 + 3
costOfSixtyCopies = (priceOfBook * discount) * numCopies + shippingCost
print(costOfSixtyCopies)

