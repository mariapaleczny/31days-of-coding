import pandas as pd
from random import randint

names_xls = "../data/100_najpopularniejszych_imion_wystepujacych_w_pesel_18.01.2017.xls"
surnames_xls = "../data/100_najpopularniejszych_nazwisk_wystepujacych_w_bazie_pesel_-_stan_na_18.01.2017.xls"
names = pd.read_excel(io=names_xls, sheet_name="IMIONA_MEN", header=2, usecols="A")
surnames = pd.read_excel(io=surnames_xls, sheet_name="NAZWISKA_MEN", header=2, usecols="A")

#normal name generator
#print(names.iloc[randint(0,99)][0], surnames.iloc[randint(0,99)][0])

for i in range(10):
    name1 = names.iloc[randint(0,99)][0]
    name2 = names.iloc[randint(0,99)][0]
    n = randint(1, min(len(name1), len(name2)))

    surname1 = surnames.iloc[randint(0,99)][0]
    surname2 = surnames.iloc[randint(0,99)][0]
    s = randint(1, min(len(surname1), len(surname2)))

    print(name1[0:n]+name2[n:]+" "+surname1[0:s]+surname2[s:])

