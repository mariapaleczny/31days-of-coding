def womensday(s: str) -> str:
    wish = "Wszystkiego najlepszego {}o!"
    if s[-1] == "a":
        return wish.format(s[:-1])
    else:
        return 'Życzenia będą w czwartek :)'


print(womensday("Maria"))
print(womensday("Ryszard"))
