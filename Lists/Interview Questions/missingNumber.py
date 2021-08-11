# find a missing number in an integer array from 1 to 100
from array import *
from random import randint

def missingNum(array):
    for i in range(1, len(array) + 1):
        if i != array[i - 1]:
            print("Missing number is:", end=' ')
            return i

def anotherway(array):
    total = array[-1] * (array[-1] + 1) / 2
    given = sum(array)
    print("Missing number is:", int(total - given))


# Generating a random array from 1-100 and removing a random element from it
arrayGenerator = array('i', [])
for n in range(1, 101):
    arrayGenerator.append(n)
element = randint(1, 100)
print("Element:", element)
arrayGenerator.remove(element)

print()

# calling the functions
print(missingNum(arrayGenerator))
anotherway(arrayGenerator)