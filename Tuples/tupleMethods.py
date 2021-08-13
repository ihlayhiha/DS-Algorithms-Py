# Operations and methods on tuples

from typing import OrderedDict


myTuple = (1, 2, 3, 4, 5, 6, 2)
myTuple1 = (1, 2, 6, 9, 8, 7)

print(myTuple + myTuple1)   # concatenation of 2 tuples
print(myTuple * 5)         # each element gets repeated 10 times

print(1 in myTuple)

# We have only 2 methods available for a tuple as they're immutable

# .count() method
# counts the repetition of an element in the tuple
print(myTuple.count(2))  

# .index() method
# returns the index value of the first occurrence of an element
print(myTuple.index(6))


#  FUNCTIONS on tuples

# len() function
print(len(myTuple * 10))

# max() function
print(max(myTuple1))
print(min(myTuple1))

# tuple() method
# can convert a list or string into a tuple
print(tuple([1, 2, 3, 4]))

# sum(), all(), any(), sorted() functions

myTuple1 = sorted(myTuple1)
print(myTuple1)


myTuple1 = 0, 1, 2, 3, 4, 5
print(all(myTuple1))
print(any(myTuple1))
print(sum(myTuple1))

