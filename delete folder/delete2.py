# trying to check if this will work too


def recursiveMethod(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursiveMethod(n - 1)
        print(n)


recursiveMethod(4)