# List Operations / Functions

# + operator / concatenate

a = [1, 2, 3, 4, 5, 6, 7]
empty = [8, 9, 10]
c = a + empty
print(c)

# * operator
rand = [0, 1, 2]
rand = rand * 4
print(rand)

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
