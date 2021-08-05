# we can increase the stack memory to deal with plausible recursion depth error

import sys
sys.setrecursionlimit(10000)    # basically has a recursive depth of 10000, i.e program limits adding stack memory at 10000 recursive steps


def factorial(n):
    """calculating the 'n' th factorial using recursion"""
    assert n >= 0 and int(n) == n, "Factorial only exits for non-negative integers, 'n' has to be non-negative integer"
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    """Return the 'n' th fibonacci number"""
    assert n > 0 and int(n) == n, "Input has to be a positive integer to find the 'n' th fibonacci number"
    if n in [1, 2]:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci (n - 2)


print(factorial(10))
print(fibonacci(20))