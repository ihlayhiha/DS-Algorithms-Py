# List Operations / Functions

# + operator / concatenate

a = [1, 2, 3, 4, 5, 6, 7]
randList = a
empty = [8, 9, 10]
c = a + empty
print(c)

# * operator
sample = [0, 1, 2]
sample = sample * 4
print(sample)

# len() function
print(len(a))

# max(), min() functions
print(max(a), min(a), sep=", ")

# sum() function
print(sum(a))


def findAverage():
    chosenList = []
    value = input("Enter a numeric value ('q' if you want to stop): ")
    while value != "q":

        # check whether the given input can be converted to 'float' values
        try:
            float(value)
        except ValueError:
            print("Please Enter numeric values only")
            pass
        else:
            chosenList.append(float(value))
    
        value = input("Enter a numeric value ('q' if you want to stop): ")

    if chosenList:
        print(sum(chosenList)/len(chosenList))
    else:
        print("Cannot calculate average for an empty list")
    

# findAverage()


# Strings to Lists and Vice-Versa
a = 'spam'
empty = list()  # one way to create empty list
b = list(a)
print(empty)
print(b)

a2 = "spam spam spam"
b2 = a2.split(" ")
print(b2)
c2 = a2.split()     # default sep=" "
print(c2)
d2 = a2.split("a")
print(d2)
sepS = a2.split("s")
print(sepS)

# using .join() method
print('s'.join(sepS))
print(" ".join(b2))
print("a".join(d2))


# checking ID's
print(randList)
print(id(randList))

randList.append(10)     # modifies the old list and still has the same ID
print(randList)
print(id(randList))

randList = randList + [11]  # breaks down and allocates new space by creating a new list
print(randList)
print(id(randList))

randList.sort()
print(randList)
print(id(randList))

randList = [9, 8, 7, 6, 6, 5, 4, 3]
print(randList)
print(id(randList))
checkList1 = randList       # just assigning it to randList
checkList2 = randList[:]    # assigning values from randList
randList.sort()           
print()
print(checkList1)   # changes as we when it's called, it's value will be called as randList
print(checkList2)   # already has a value assigned. Doesn't change when randList is sorted
