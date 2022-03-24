def is_geometric(numbers: list) -> bool:
    if len(numbers) < 2:
        return True
    sorted_numbers = sorted(numbers)
    q = sorted_numbers[1]/sorted_numbers[0]
    for i in range(len(numbers)-1):
        if q*sorted_numbers[i] != sorted_numbers[i+1]:
            return False
    return True


assert(is_geometric([1,1,1]) is True)
assert(is_geometric([0.5,0.2]) is True)
assert(is_geometric([4,1,8,16,2]) is True)
assert(is_geometric([1,2,3]) is False)
