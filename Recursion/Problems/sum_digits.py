def sum_digits(n):
    """Return the sum of digits of a positive integer number"""
    assert n > 0 and int(n) == n, "'n' has to be a positive integer"
    if n // 10 == 0:
        return n % 10
    else:
        return (n % 10) + sum_digits(n // 10)


def power(x, n):
    """Return the nth power of x"""
    assert int(n) == n, "Calculating only the integer powers of numbers"
    if n < 0:
        return power(1/x, -n)
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
    

print(sum_digits(4789359))
print(power(1/10, -3))