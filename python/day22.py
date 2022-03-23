def perfectly_balanced(word: str) -> bool:
    if len(word.replace("x", "").replace("y", "")) > 0:
        raise ValueError('Given string contains characters different from x or y')
    return word.count("x") == word.count("y")


assert(perfectly_balanced("xxyy") is True)
assert(perfectly_balanced("xyx") is False)
