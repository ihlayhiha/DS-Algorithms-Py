# finding max product of 2 integers in an array where all elements are positive
import numpy as np

def maxProduct(array):

    # Using np.sort() function
    # array = np.sort(array)
    # print("Max product:", array[-1] * array[-2])
    # print(max(array))


    maxArray = max(array)
    localMax = 0

    # count = (array == maxArray).sum()   # counts how many times there's a value 'maxArray' in given array and adds them
    count = np.count_nonzero(array == maxArray)     # using .count_nonzero() function to count repetitions of 'maxArray' in 'array'
    if count > 1:
        print(maxArray ** 2)
    else:
        for value in array:
            if value != maxArray and value > localMax:
                localMax = value

        print("Max product:", localMax * maxArray)


myArray = np.array([1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21, 70, 70])

maxProduct(myArray)


print()
print(type(myArray))
print(myArray == 13)    # checks every element and returns True/False statement
print(type(myArray == 13))      # an  numpy.ndarray
print((myArray == 13)[10])      # prints the 10 th value 
print((myArray == 13).sum())    # returns how many times it's True

print(True + False)     # True + False = 1
print(True + True + False )                 # True + True + False = 2
print((True + True + False) * False )       #(....) * False = 0
print(True + True * False + False )         # True + (True * False) + False = 1
