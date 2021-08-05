# we can increase the stack memory to deal with plausible recursion depth error

import sys
sys.setrecursionlimit(10000)    # basically has a recursive depth of 10000, i.e program limits adding stack memory at 10000 recursive steps


def factorial(n):
    """calculating the 'n' th factorial using recursion"""
    assert(n >= 0), "n should be > 0, Factorial only exits for non-negative integers"
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(10))