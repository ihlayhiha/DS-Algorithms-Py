import sampleLambda

# Using decorators 
def div(a, b):
    return a // b


# Nesting more functions cause functions are also objects in python

def anotherDiv(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


div1 = anotherDiv(div)


print(div1(4, 19))

print(__name__)
