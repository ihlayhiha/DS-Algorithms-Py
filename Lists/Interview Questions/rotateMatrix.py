# Given an image represented by NxN matrix, write  method to rotate the image 90 degrees
import numpy as np

def rotateMatrix(array):
    size = len(array)
    endMatrix = []
    for j in range(size):
        tempList = []
        for i in range(size - 1, -1, -1):
            tempList.append(array[i][j])

        endMatrix.append(tempList)
        sol = np.array(endMatrix)

    return sol


myArray = np.array([[1, 2, 3, 4], [ 5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(myArray)
print(rotateMatrix(myArray))