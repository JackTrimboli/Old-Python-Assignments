"""
Jack Trimboli
CS 100 2021S Section 108
HW 08, March 26th, 2021
"""

import string


def enterNewPassword():
    while True:
        containsDigit = False
        idealLength = False
        password = input("Enter password: ")
        for x in string.digits:
            if x in password:
                containsDigit = True
        if len(password) >= 8 and len(password) <= 15:
            idealLength = True

        if not containsDigit:
            print("Password must contain at least one digit")
        if not idealLength:
            print("Password must be within 8-15 characters")
        if containsDigit and idealLength:
            print("Password created.")
            break


enterNewPassword()
