def sum_digits(n):
    """Return the sum of digits of a positive integer number"""
    assert n > 0 and int(n) == n, "'n' has to be a positive integer"
    if n // 10 == 0:
        return n % 10
        
    return (n % 10) + sum_digits(n // 10)


def power(base, exp):
    """Return the exponential power of 'base'"""
    assert int(exp) == exp, "Calculating only the integer powers of numbers"
    if exp < 0:
        return power(1/base, -exp)
    if exp == 0:
        return 1

    return base * power(base, exp - 1)
    

print(sum_digits(4789359))
print(power(10, 2))