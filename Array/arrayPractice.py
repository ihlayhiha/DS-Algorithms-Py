from array import *

# Create array and Traverse
print("STEP: 1" + " *" * 30)
my_array = array('i', [1, 2, 3, 4, 5])
print(my_array)
print(f"ID of this array is: {id(my_array)}", end='\n\n')

for i in my_array:
    print(i)

# Access individual elements through indexes
print("STEP: 2" + " *" * 30)

for i in range(len(my_array)):
    print(my_array[i])

# Append any value to the array using .append() method
print("STEP: 3" + " *" * 30)

my_array.append(6)
print(my_array)
print(f"ID of this array is: {id(my_array)}", end='\n\n')

# Insert value in array using .insert() method
print("STEP: 4" + " *" * 30)

my_array.insert(0, 0)   # inserting 0 at index position: 0
print(my_array)
print(f"ID of this array is: {id(my_array)}", end='\n\n')

# Extend Python array using .extend() method
print("STEP: 5" + " *" * 30)
dummy = array('i', [10, 11, 12])
my_array.extend(dummy)
print(my_array)
print(f"ID of this array is: {id(my_array)}", end='\n\n')

# Add items from list into array using .fromlist() method
print("STEP: 6" + " *" * 30)
list1 = [20, 21, 22]
my_array.fromlist(list1)
print(my_array)
print(f"ID of this array is: {id(my_array)}", end='\n\n')

# Remove any array element using .remove() method
print("STEP: 7" + " *" * 30)
my_array.remove(20)
print(my_array)
print(f"ID of this array is: {id(my_array)}", end='\n\n')

# Remove last element from array using .pop() method
print("STEP: 8" + " *" * 30)
my_array.pop()  # by default pops the last element from the array
print(my_array)
print(f"ID of this array is: {id(my_array)}", end='\n\n')

# Fetch any element through its index using .index() method
print("STEP: 9" + " *" * 30)
print(my_array.index(6))
print(f"ID of this array is: {id(my_array)}", end='\n\n')

# Reverse a python array using .reverse() method
print("STEP: 10" + " *" * 30)
my_array.reverse()
print(my_array)
print(f"ID of this array is: {id(my_array)}", end='\n\n')

# Get array buffer information through .buffer_info() method
print("STEP: 11" + " *" * 30)
print("Buffer info of this array: {}".format(my_array.buffer_info()))
print(f"ID of this array is: {id(my_array)}", end='\n\n')

# Check the number of occurrences of an element using .count() method
print("STEP: 12" + " *" * 30)
my_array.append(10)
print("The number of occurrences of {} in this array is {}".format(10, my_array.count(10)))
print(f"ID of this array is: {id(my_array)}", end='\n\n')

# Convert array into string using .tobytes() method
print("STEP: 13" + " *" * 30)
strTemp = my_array.tobytes()
print(strTemp)
print()

tempInts = array('i')       # way to create an empty array, is the same as array('i', [])
tempInts.frombytes(strTemp)
print(tempInts)
if tempInts == my_array:
    print(True)

# Convert array into Python list using .tolist() method
print("STEP: 14" + " *" * 30)
listArray = my_array.tolist()
print(listArray)
print(type(listArray))
print(f"ID of this List is: {id(listArray)}", end='\n\n')
print(my_array)
print(f"ID of this array is: {id(my_array)}", end='\n\n')

# Append a string to char array using .frombytes() method
print("STEP: 15" + " *" * 30)
randomBytes = my_array.tobytes()

randomInts = array('i')
randomInts.frombytes(randomBytes)   # Appending using .frombytes() method
print(randomInts)
if randomInts == my_array:
    print("Just appended a bytes variable using .frombytes() method")
print(f"ID of this array is: {id(my_array)}", end='\n\n')

# Slice elements of an array
print("STEP: 16" + " *" * 30)
print(my_array[1:7])
randSlice = my_array[1:7]
print(randSlice)
print(f"ID of this Slice is: {id(randSlice)}", end='\n')
print(f"ID of this array is: {id(my_array)}", end='\n\n')
