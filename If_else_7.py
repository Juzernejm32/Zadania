#7. Sprawdź, czy podane przez użytkownika hasło spełnia następujące warunki\n",
# -  przynajmniej jedna mała i jedna wielka litera - islower?
# -  przynajmniej jedna cyfra
# - przynajmniej jeden znak specjalny
# - minimum 3 znaki długości
# - maksymalnie 18 znaków długości
lista = []
has = input("podaj hasło: ")
if 18 >= len(has) >= 3:
    for i in range(len(has)):
        miejsce = has[i]
        lista.append(miejsce)
    print(lista)
    if lista.__contains__("h"):
        print("test")