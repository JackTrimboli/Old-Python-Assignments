"""
Jack Trimboli
CS 100 2021S Section 108
HW 03, February 11th, 2021
"""
import turtle

aScreen = turtle.Screen()
turtle = turtle.Turtle()
# 1a: Draw a triangle
for x in range(0, 3):
    turtle.forward(100)
    turtle.left(120)

# 1b: Draw a square
for x in range(0, 4):
    turtle.forward(100)
    turtle.left(90)

# 1c: Draw a regular pentagon, with each side length 100
for x in range(0, 5):
    turtle.forward(100)
    turtle.left(72)

# 2: draw 4 concentric circles with the radii 50, 100, 150, 200.
turtle.penup()
for x in range(50, 201, 50):
    turtle.right(90)
    turtle.forward(x)
    turtle.right(270)
    turtle.pendown()
    turtle.circle(x)
    turtle.penup()
    turtle.home()

aScreen.exitonclick()

import math

# 3a: write the code to perform !100
print(math.factorial(100))

# 3b: log based 2 of 1,000,000
print(math.log(1000000, 2))
# OR
print(math.log2(1000000))

# 3c: Get the GCD of 63 and 49
print(math.gcd(49, 63))