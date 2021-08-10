from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])
arr2 = array('d', [1.3, 1.5, .8])


print(arr1, arr2)


# inserting 10 as the 7 th element into arr1
arr1.insert(6, 10)
print(arr1)
# inserting 11 as the first element into arr1
# the array moves to the right automatically
arr1.insert(0, 11)
print(arr1)
# inserting something into the 2nd index
# moves everything after 2nd element to the right and inserts there.
arr1.insert(2, 12)
print(arr1)

# Time Complexity for inserting is dependent on where u wanna insert and the worst case is O(n)
print(len(arr1))
arr1.insert(9, 99)
print(len(arr1))
