#4. Sprawdź, czy użytkownik wpisał liczbę parzystą.
a = input("podaj liczbę: ")
if a.isdigit():
    if int(a)%2 == 0:
        print("liczba jest parzysta")
    elif int(a)%2 != 0:
        print("liczba nie jest parzysta")
else:
    print("Błąd, należy wprowadzić cyfrę ")

