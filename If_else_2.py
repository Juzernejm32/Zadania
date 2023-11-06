#2. Przekonwertuj dane wpisane przez użytkownika na dane typu integer.
#Następnie napisz program który sprawdzi, czy wprowadzone przez użytkownika dane są takie same
a = input("Podaje cyfrę: ")
b = input("Podaj drugą cyfrę: ")
if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
    if a == b:
        print("Cyfry są takie same")
    else:
        print("Cyfry nie są takie same")
else:
    raise RuntimeError("Błąd, należy wprowadzić cyfry")

# if int(a) == int(b) -> taki skrót