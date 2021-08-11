# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

print(twoDArray)
print(type(twoDArray))

# trying Inserting a column or row

newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=1)  # axis=1 adds as a column
print(newTwoDArray)

print()

# inserting new values at the index 2
anotherTwoDArray = np.insert(twoDArray, 2, [[1, 2, 3, 4]], axis=0)  # axis=0 adds as a row
print(anotherTwoDArray)

print()
# appending at the end using np.append() function. Mention row or column
appendedTwoDArray = np.append(twoDArray, [[1, 2, 3, 4]], axis=0)
print(appendedTwoDArray)


def accessElements(array, rowIndex, colIndex):
    """Print the desired element if the rowIndex and colIndex are plausible"""
    if rowIndex >= len(array) or rowIndex < -len(array) or colIndex >= len(array[0]) or colIndex < -len(array[0]):
        print("Row or Column indexes should be inbounds and non-negative integers") 
    else:
        print(array[rowIndex, colIndex])


accessElements(twoDArray, -4, -2)
print()

# traversing along the TwoDArray
for i in range(len(twoDArray)):
    for j in range(len(twoDArray[0])):
        print(twoDArray[i][j])

print()

# another way
for row in range(len(twoDArray)):
    for value in twoDArray[row]:
        print(value)

print()

# function for traversing
def traverseTwoDArray(array):
    for row in range(len(array)):
        for value in array[row]:
            print(value)


traverseTwoDArray(twoDArray)
print()

# function for linear search in 2D array
def linearSearchTwoDArray(array, value):
    """Check and print the row and column index of value in the array"""
    for row in range(len(array)):
        for col in range(len(array[row])):
            if value == array[row][col]:
                print(f"Element: {value} has one occurrence at row={row}, col={col} in this array")
                return
    else:
        print("No such value exists in this array")
    

linearSearchTwoDArray(twoDArray, 10)
print()
