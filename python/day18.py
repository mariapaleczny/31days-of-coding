def all_equal(inlist: list) -> bool:
    return len(set(inlist)) == 1


assert(all_equal([1, 1, 1]) is True)
assert(all_equal(["a", "a", "b"]) is False)
