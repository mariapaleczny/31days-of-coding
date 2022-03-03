def reverse_string(s: str) -> str:
    out = ''
    for symbol in s:
        out = symbol + out
    return out

def reverse_string_oneliner(s: str) -> str:
    return s[::-1]


print(reverse_string("I did, did I?..."))
print(reverse_string_oneliner("I did, did I?..."))