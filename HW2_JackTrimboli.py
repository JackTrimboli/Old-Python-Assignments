"""
Jack Trimboli
CS 100 2021S Section 108
HW 02, February 3rd, 2021
"""

#1
def getNumScores(list1, list2):
    list2.append(list1.count('A'))
    list2.append(list1.count('B'))
    list2.append(list1.count('C'))
    list2.append(list1.count('D'))
    list2.append(list1.count('F'))

grades = ['A', 'A', 'B', 'A', 'C', 'A', 'F', 'B', 'F', 'D']
frequency = []
getNumScores(grades, frequency)
print(frequency)

#Created a function which counts the number of each grade in one list and appends each count to a second list

#2a
dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua']

#2b
herding_dogs = dog_breeds[0:2]
print(herding_dogs)

#2c
tiny_dogs = [dog_breeds[-1]]

#2d
dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua']
print('Persian' in dog_breeds)
