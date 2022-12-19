# Napisz funkcję potęga(), która podniesie wartości z pierwszej listy do potęg z drugiej listy.
# Sprawdź,czy listy są tej samej długości. Parametrami funkcji są dwie listy.
# Funkcja ma zwracać listę z wynikami.

def potega(list1, list2):
    list3 = []
    for i in range(len(list1)):
        x = list1[i] ** list2[i]
        list3.append(x)
    return  list3
print(potega([1,2,3,4,5], [6,7,8,9,10]))

L1 = [2,3,4]
L2 = [2,4,1]
L3 = potega(L1, L2)
print(L3)
L3 = potega(L2, L1)
print(L3)