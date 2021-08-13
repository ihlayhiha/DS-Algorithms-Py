newTuple = 'a', 'b', 'c', 'd', 'e'
print(newTuple)

newTuple2 = ('a')   # python will consider this as a string if there's no commma
print(type(newTuple2))
print(newTuple2)

newTuple1 = ('a',)  # python will consider this as a tuple if there's a commma
print(type(newTuple1))
print(newTuple1)

usingFunc = tuple()
print(usingFunc)
print(type(usingFunc))

anotherTuple = tuple('abc')
print(anotherTuple)

# traversing
for i in newTuple:
    print(i)

for i in range(len(newTuple)):
    print(newTuple[i])


# searching for element in a tuple

def inOperator(tuple, element):
    return(element in tuple)


def linearSearch(tuple, element):
    """Return a tuple of index and element if the element is there in the tuple"""
    for value in tuple:
        if value == element:
            return tuple.index(value), value
    return f"{element} does not exist in this tuple"


print(inOperator(newTuple, 'g'))
print(linearSearch(newTuple, 'g'))
