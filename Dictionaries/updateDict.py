# Update / add an element to a dictionary

myDict = {'name': "Yella",
'age': 26,}
# print(myDict)

# Updating Value for "age" key
myDict["age"] = 27
# print(myDict)

# adding element for myDict
myDict['address'] = "London"
# print(myDict)

# Traversing through a dictionary

def traverseDict(dict):
    for key in dict:
        print(key, dict[key], sep=": ")
        

# traverseDict(myDict)

# Finding an element in a dictionary

def findKey(dict, key):
    if key in dict:
        print(key, dict[key], sep=": ")
    else:
        print("There's no such key named: " + key + " in this dictionary")


# findKey(myDict, "name")


def findValue(dict, value):
    for key in dict:
        if dict[key] == value:
            return True
        
    return False


# print(findValue(myDict, "London"))

# Delete or remove element from dictionary

# Using .pop() method. Unlike Lists, .pop() for dictionaries need at least one argument because keys in dictionary don't have indexes

myDict['education'] = "Engineering"

print(myDict.pop('age') + 100)      #  Pops the element and returns a the value of myDict['age']
print(myDict)

# using .popitem() method 

myDict['age'] = 26
myDict['sexuality'] = 'male'

print(myDict.popitem())         # Pops a random element from the dictionary and returns a tuple of (key, value) of the element it popped
print(myDict)

# using .clear() method
# clears the whole dictionary
# print(myDict)

# myDict.clear()
# print(myDict)

# using del method
del myDict['age']
print(myDict)

del myDict      # if u don't define a keyword, it will delete the entire dictionary
print(myDict)   # Raises error because there will be no dictionary 

