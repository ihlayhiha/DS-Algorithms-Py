# create a dictionary

# using dict() function

myDict = dict()
print(myDict)

# another way
anotherDict = {}
print(anotherDict)

translateDict = {"one": "uno",
"two": "dos",
"three": "tres",}

print(translateDict)
for num in translateDict:
    print(num)

for key in translateDict.keys():
    print(key)

print(translateDict.get("three"))
print(translateDict.get("four", "does not exit here dumbass"))
print(translateDict["three"])
try: print(translateDict["four"])    # raises error
except KeyError:
    print("this generated a KeyError, alternate way is to use the .get() method for dictionaries")

# order of the dictionary will not be the same as the order we entered.
# Hence we can't call dictionary keys will index numbers unless we create a new list 
# this  created new list can have keys in any random order possible. 

keysList = list(translateDict.keys())
print(keysList[0])