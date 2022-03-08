def womensday() -> str:
    wish = "Wszystkiego najlepszego {}o!"
    name = input("Wprowadź swoje imię: ")
    if name[-1] == "a":
        return wish.format(name[:-1])
    else:
        name_other = input("Wprowadź imię bliskiej Ci kobiety: ")
        if name_other[-1] == "a":
            return "Idź i powiedz: \"" + wish.format(name_other[:-1]) + "\""
        else:
            return "Niemożliwe! Być może archiwa są niekompletne."


print(womensday())