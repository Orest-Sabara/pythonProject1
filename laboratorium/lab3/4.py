# Zmodyfikuj program z zad. 1 tak, aby przechodząc po kolejnych liczbach przedziału,
# wypisywać tylko liczby parzyste, a nieparzyste – pomijać. Użyj instrukcji continue

licba1 = int(input('podai liczbe 1: '))
licba2 = int(input('podai liczbe 2: '))

if licba2<licba1:
    licba1, licba2 = licba2, licba1
while licba1 <= licba2:
    if licba1%2 != 0:
        licba1 += 1
        continue
    print(licba1, end=' ')
    licba1 += 1
