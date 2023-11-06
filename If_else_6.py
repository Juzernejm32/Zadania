#6. Sprawdź, czy suma dwóch liczb wpisanych przez użytkownika jest liczbą parzystą
a = input("Podaj pierwszą liczbę: ")
b = input("Podaj drugą liczbę: ")
if a.isdigit() and b.isdigit():
    if (int(a) + int(b))%2 == 0:
        print("suma liczb [", int(a) + int(b), "] jest liczbą parzystą")
    else:
        print("suma liczb [", int(a) + int(b), "] NIE jest liczbą parzystą")
else:
    print("Błędne dane")