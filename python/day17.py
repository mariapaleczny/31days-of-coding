def calculate_factorial(n: int) -> int:
    """
    Calculates factorial of non-negative integer.
    """
    if n < 0:
        raise ValueError('Input is not non-negative.')
    elif n != int(n):
        raise ValueError('Input is not an integer.')
    elif n == 0 or n == 1:
        return 1
    else:
        ans = 1
        while n > 1:
            ans = ans * n
            n = n - 1
        return ans


assert(calculate_factorial(0) == 1)
assert(calculate_factorial(5) == 120)


