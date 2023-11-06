#10. Napisz program, który sprawdzi która z 3 podanych przez użytkownika jest największa oraz najmniejsza
lista = []
for i in range(3):
    lista.append(int(input("Daj liczbę ")))
print("Najmniejsza podana liczba to: ",min(lista))
print("Największa podana liczba to: ",max(lista))