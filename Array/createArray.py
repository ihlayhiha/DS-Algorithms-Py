from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])
arr2 = array('d', [1.3, 1.5, .8])


print(arr1, arr2)


# inserting 10 as the 7 th element into arr1
print(f"the ID of arr1: {id(arr1)}", end='\n\n')
arr1.insert(6, 10)
print(arr1)
print(f"the ID of arr1: {id(arr1)}", end='\n\n')
# inserting 11 as the first element into arr1
# the array moves to the right automatically
arr1.insert(0, 11)
print(arr1)
# inserting something into the 2nd index
# moves everything after 2nd element to the right and inserts there.
arr1.insert(2, 12)
print(arr1)

# Time Complexity for inserting is dependent on where u wanna insert and the worst case is O(n)
# print(len(arr1))
arr1.insert(9, 99)
# print(len(arr1))
# just changing the value of an element in this array
arr1[0] = 100
print(f"the ID of arr1: {id(arr1)}", end='\n\n')

arr1.insert(100, 15)    # if index u want to insert > len(arrray), it inserts the element at the end of array (array elements HAVE to be continuous)
print(arr1)
print(f"the ID of arr1: {id(arr1)}", end='\n\n')

# Trying out Remove element method. Needs only one argument (the value u want to remove)
print("Removing element with value = 1")
arr1.remove(1)
print(arr1)
print(f"the ID of arr1: {id(arr1)}", end='\n\n')

print("Removing the 4th element which has value = {} ".format(arr1[3]))
arr1.remove(arr1[3])
print(arr1)
print(f"the ID of arr1: {id(arr1)}", end='\n\n')

print("*" * 50)
# trying out Traversing

def traverseArray(array):
    for n in range(len(array)):
        print(f"The {n} element in this array is {array[n]}")


def searchInArray(array, value):
    for i in array:
        if i == value:
            print(array.index(i))
            return

    print("No such value exists in this array")



# traverseArray(arr1)
searchInArray(arr1, 222)