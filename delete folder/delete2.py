# trying to check if this will work too


def recursiveMethod(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursiveMethod(n - 1)
        print(n)


m = 3
assert(m < 1), "Does this work" + " adding random stuff" + "Generting a random assertion error"


recursiveMethod(4)