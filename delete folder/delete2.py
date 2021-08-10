# trying to check if this will work too

def recursiveMethod(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursiveMethod(n - 1)
        print(n)


m = 3
# assert(m < 1), "Does this work" + " adding random stuff" + "Generting a random assertion error"


def factorial(n):
    """calculating the 'n' th factorial using recursion"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
recursiveMethod(4) 
# yes this does look a lot better yes?