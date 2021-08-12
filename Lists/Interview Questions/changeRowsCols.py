def interchangeRowsCols(array):
    endMatrix = []
    size = len(array)

    for i in range(size):
        tempList = []
        for j in range(size):
            tempList.append(array[j][i])

        endMatrix.append(tempList)

    return endMatrix


print(interchangeRowsCols([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
