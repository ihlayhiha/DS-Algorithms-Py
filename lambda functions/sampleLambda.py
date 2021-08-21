from functools import reduce

# using simple lambda functions

addFunction = lambda a, b: a + b

sampleFunction = lambda a: a**2

anotherFunction = lambda *a: sum(a)

print(addFunction(1, 10))
print(sampleFunction(10))
print(anotherFunction(1, 2, 3, 4))



nums = [3, 2, 66, 8, 4, 2, 9, 11]
isEven = lambda a: a % 2 ==0
# Filter in-built functions that needs another function to check what values it needs to filter.
# The isEven  function returns a boolean value indicating to filter out the False values 
# evens = list(filter(isEven, nums))

filterSequence  = filter(lambda a: a % 2 ==0, nums)
print(filterSequence)
# returns a filter object that's an interable sequence

print("iterating through filter object")
for value in filterSequence:
    print(value, end=" ")

print()

anotherEvens = list(filter(lambda a: a % 2 ==0, nums))
print(anotherEvens)


# using map inbuilt function
doubles = list(map(lambda a: a*2, nums))
print(doubles)

# using reduce function imported from functools module
sum = reduce(lambda a, b: a + b, nums)
print(sum)


__name__ = "Changing the name lol"
print("This is Lambda functions exercise module", __name__)
