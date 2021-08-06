def sum_digits(n):
    """Return the sum of digits of a positive integer number"""
    assert n > 0 and int(n) == n, "'n' has to be a positive integer"
    if n // 10 == 0:
        return n % 10
    else:
        return (n % 10) + sum_digits(n // 10)


print(sum_digits(4789359))