# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

import numpy as np
from numpy.lib.function_base import append

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
    if rowIndex >= len(array) or rowIndex < -len(array) or colIndex >= len(array[0]) or colIndex < -len(array[0]):
        print("Row or Column indexes should be inbounds and non-negative integers") 
    else:
        print(array[rowIndex, colIndex])


accessElements(twoDArray, -4, -2)
