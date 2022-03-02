def switch_case(s: str) -> str:
    out = ''
    for symbol in s:
        if symbol.isalpha():
            if symbol.islower():
                out += symbol.upper()
            else:
                out += symbol.lower()
        else:
            out += symbol
    return out


print(switch_case("hELLO! hOW ARE you?"))