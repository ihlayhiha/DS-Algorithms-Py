# dictionary methods

myDict = {'name': "Yella", 
'age': 32,
'sexuality': 'Male',
'education': 'College',
'address': 'London',
'interests': 'Football'}

# .clear() method
# does not take any argument and does not return any value
# myDict.clear()

# .copy() method
# returns a shallow copy of a dictionary
copyDict = myDict.copy()
print(copyDict)

# .fromkeys() method
# creates a new dictionary from given set of keys and their values in the current dictionary
newDict = {}.fromkeys([1, 2, 3], 0)
print(newDict)
partDict = {}.fromkeys(list(myDict.keys()), 10)
print(partDict)

# .get() method
# returns the value of a specified key, if no such key exists, defaults to None
print(myDict.get("name"))
print(myDict.get('age') + 100)
print(myDict.get('what the fuck'), "See, it shows None doesn't it", sep=", ")
print(myDict.get('what the fuck', "Don't show None"), "Doesn't show None", sep=", ")

# .items() method
# returns a view object that displays a list of dictionary's (key, value) tuple pairs
print(myDict.items())

allitems = list(myDict.items())
for pair in allitems:
    print(pair)

# .keys() method
# returns a view object list as dict_keys containing all keys in the dictionary
print(myDict.keys())

# .popitem() method
# removes a random element from the dictionary and returns it as a (key, value) tuple
print(myDict.popitem())
print(myDict.keys())

# .setdefault() method
# returns the value of key if key is in the dictionary.
# if no such key exists, it inserts the key with a value provided
print(myDict.setdefault('age'))     
print(myDict)

print(myDict.setdefault('randomKey'))   # returns None as no default value provided for the new key
print(myDict)

print(myDict.setdefault('interests', "Football"))   # returns "Football" meaning there is no such key in the dictionary
print(myDict)       # adds the new key and value since they didn't exist before

del myDict['randomKey']
print(myDict.keys())

# .pop() method
# returns the value of key argument provided
myDict.setdefault('randomKey')
if not myDict.pop('randomKey'):
    print("Just popped the newly  added randomKey with no value")

print(myDict.keys())

# .values() method
# returns a view object that is a list of all the values in the dictionary
print(myDict.values())

# .update() method
# updates the dictionary with elements from another dictionary (or) from an iterable of (key, value) pairs, i.e takes either a dictionary or a tuple as a parameter
# adds elements to the dictionary if the key isn't present before
# updates key values with new values if the key is present already

updateDict = {'a': 1, 'b': 2, 'c': 3}
myDict.update(updateDict)

listTuple = [('adding from tuple', 'YES'), ('adding another', 'DOUBLE YES')]
myDict.update(listTuple)
print(myDict)

