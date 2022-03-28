def digit_adder(n: int) -> int:
    ans = ''
    for i in str(n):
        ans += str(int(i) + 1)
    return int(ans)


assert(digit_adder(998) == 10109)
