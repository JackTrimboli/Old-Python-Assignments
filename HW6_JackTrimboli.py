"""
Jack Trimboli
CS 100 2021S Section 108
HW 06, February 19th, 2021
"""

# 1a
def hasFinalLetter(strList, letters):
    res = []
    for x in strList:
        if x[-1] in letters:
            res.append(x)
    return res


# 1b - three testcases
list1 = ["hello", "world", "python", "is", "cool"]
letters1 = "ol"
list2 = ["one", "twO", "three", "four", "fivE"]
letters2 = "eEr"
list3 = ["ThiS", "iS", "thE", "lasT", "test"]
letters3 = "QRs"
print(hasFinalLetter(list1, letters1))  # prints hello and cool
print(hasFinalLetter(list2, letters2))  # print one, three, four, and fivE
print(hasFinalLetter(list3, letters3))  # prints an empty list

# 2a
def isDivisible(maxInt: int, twoInts: tuple) -> list:
    res = []
    for x in range(1, maxInt):
        if x % twoInts[0] == 0 and x % twoInts[1] == 0:
            res.append(x)
    return res


# 2b - three testcases
tuple1 = (3, 5)
maxInt1 = 100
print(isDivisible(maxInt1, tuple1))  # returns [15, 30, 45, 60, 75, 90]
tuple2 = (4, 7)
maxInt2 = 6
print(isDivisible(maxInt2, tuple2))  # Returns an empty list
tuple3 = (4, 6)
maxInt3 = 48
print(isDivisible(maxInt3, tuple3))  # Returns [12, 24, 36]
