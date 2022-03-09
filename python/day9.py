def mid(word: str) -> str:
    if len(word) % 2 == 1:
        return word[int(len(word)/2)]
    else:
        return ""


print(mid("tesTing"))
