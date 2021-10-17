"""
Jack Trimboli
CS 100 2021S Section 108
HW 03, February 11th, 2021
"""

# 1
a = 3
b = 4
c = 5

if a < b:
    print("ok")
if c < b:
    print("ok")
if a + b == c:
    print("ok")
if a ** 2 + b ** 2 == c ** 2:
    print("ok")

# 2
if a < b:
    print("ok")
else:
    print("NOT OK")

if c < b:
    print("ok")
else:
    print("NOT OK")

if a + b == c:
    print("ok")
else:
    print("NOT OK")

if a ** 2 + b ** 2 == c ** 2:
    print("ok")
else:
    print("NOT OK")

# 3
import turtle

aScreen = turtle.Screen()
turtle = turtle.Turtle()
turtle.pencolor(input("What color?"))
turtle.width(input("What line width?"))
length = input("What line length?")
inp = input("Line, Triangle, or Square?")

if inp.upper() == "LINE":
    turtle.forward(length)
elif inp.upper() == "TRIANGLE":
    for x in range(0, 3):
        turtle.forward(length)
        turtle.left(120)
elif inp.upper() == "SQUARE":
    for x in range(0, 4):
        turtle.forward(length)
        turtle.left(90)
else:
    print("invalid input.")

aScreen.exitonclick()
