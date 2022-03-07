def capital_indexes(s: str) -> list:
    return [i for i in range(len(s)) if s[i].isupper()]


print(capital_indexes("BLAblabLa"))
