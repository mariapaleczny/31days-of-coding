def is_ugly(number: int) -> bool:
    for i in [2, 3, 5]:
        while number % i == 0:
            number = number/i
    return number == 1


assert(is_ugly(15) is True)
assert(is_ugly(22) is False)