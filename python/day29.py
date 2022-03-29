def additive_persistence(n: int) -> int:
    ans = 0
    while len(str(n)) > 1:
        n = sum([int(i) for i in list(str(n))])
        ans += 1
    return ans


assert(additive_persistence(1) == 0)
assert(additive_persistence(12) == 1)
assert(additive_persistence(1234) == 2)
assert(additive_persistence(199) == 3)