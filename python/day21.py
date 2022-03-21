def move_zero(inlist: list) -> list:
    return [x for x in inlist if x != 0] + [x for x in inlist if x == 0]


assert(move_zero([0, 1, 0, 2]) == [1, 2, 0, 0])
assert(move_zero(["a", 1]) == ["a", 1])
