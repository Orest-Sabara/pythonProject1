# Napisz funkcję find(), która w liście sprawdza czy występuje podana wartość. Lista i wartość są
# parametrami funkcji. Funkcja ma zwracać listę indeksów, pod którymi wystąpiła wartość. Nie wolno korzystać z
# operatora in w celu sprawdzenia czy wartość występuje w liście.

def find (lista, wartosc):
    lista2 = []
    ind = 0
    for i in lista:
        if wartosc == i:
            lista2.append(ind)
        ind += 1
    return lista2

print(find([1,2,2,4,2,451,15,2],9))
