# functions that can be used with dictionaries

myDict = {'name': "Yella", 
'age': 32,
'sexuality': 'Male',
'education': 'College',
'address': 'London',
'interests': 'Football'}


# in operator
print('age' in myDict)
print("favorites" in myDict.keys())
print("Yella" in myDict.values())   # time complexity is O(1) because the by taking a key, it calculate the Hash value using the hash function and looks up the resulting index
print()


# for operator
for key in myDict:
    print(key, myDict[key], sep=": ")
print()


# all() function
# returns True if all elements in given iterable are True. else, it returns False
# if Empty iterable, it returns True
checkAllDict = {0: True,
1: True,
2: True}
print(all(checkAllDict))   # gives False because of 0 (False) as a key
emptyDict = {}
print(all(emptyDict))      # gives True because empty iterable


# any() function
# returns True if anything is True, False if all are False
# returns False for an empty dict
checkAnyDict = {0: 0, 1: 1}
print(any(checkAnyDict))    # returns True cause it has a 1 (True) key
print(any(emptyDict))       # returns False for empty iterable


# len() function, returns the number of pairs
myDict.setdefault("random key")
print(myDict.keys())
print(len(myDict))
print(myDict.values())
print(len(myDict.values()))


# sorted() function
# has maximum of 3 parameters: iterable, reverse=False/True, key=null
newDict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print(sorted(newDict))  # sorts the keys of our dictionary
print(sorted(newDict, reverse=True))

newDict = {'efa': 1, 'aghshs': 2, 'uag': 3, 'ojshsd': 4, 'ifaj': 5}
print(sorted(newDict, key=len))
print(sorted(newDict, reverse=True, key=len))

