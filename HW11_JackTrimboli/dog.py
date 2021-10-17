# Jack Trimboli
# CS 100 2021S Section 108
# HW 11, April 23, 2021
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []

    def teach(self, trick):
        self.tricks.append(trick)
        print(self.name + " now knows " + trick)

    def knows(self, trick):
        if trick in self.tricks:
            print("Yes, " + self.name + " knows " + trick)
            return True
        print("No, " + self.name + " does not know " + trick)
        return False
