# Lists vs Arrays
import numpy as np

# Pick Arrays if we want to do any arthematic operations
# Arrays are optimized for arthematic computations among other things
myArray = np.array([1, 2, 3, 4, 5, 6])
myList = [1, 2, 3, 4, 5, 6]

print(myArray/2)    
# print(myList/2)     # gives an error
print()


# array must have the same data type for all elements in the array
sampleArray = np.array([1, 2, 3, 4, 5, 'a'])    # because of 'a', the rest of the elements in array gets converted to strings
sampleList = [1, 2, 3, 4, 5, 'a']

print(sampleArray)
print(sampleList)
