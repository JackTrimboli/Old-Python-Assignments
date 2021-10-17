"""
Jack Trimboli
CS 100 2021S Section 108
HW 05, February 19th, 2021
"""

# 1
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

for month in months:
    if month[0].upper() == "J":
        print(month)

# 2
for x in range(0, 100):
    if x % 2 == 0 and x % 5 == 0:
        print(x)

# 3
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for letters in horton:
    if letters in vowels:
        print(letters)