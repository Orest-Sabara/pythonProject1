import random

# punkty = []
#
# for i in range(15):
#     p = round(random.uniform(0, 50), 2)
#     # p = round(p, 2)
#     punkty.append(p)
# print(punkty)

punkty = [round(random.uniform(0, 50), 2) for i in range(15)]
print(punkty)

print(f'Maximum = {max(punkty)}')
print(f'Minimum = {min(punkty)}')

# • Wyświetl indeks pierwszego wystąpienia punktów podanych przez użytkownika .
# Jeżeli taka liczba punktów nie występuje na liście, wyświetl odpowiedni komunikat

p = float(input('podai licbe: '))

if p in punkty:
    x = punkty.index(p)
    print('index', x)
else:
    print('nema lichbe v pynkty')

# • Oblicz średnią punktów liczbę punktów z egzaminu

sr = round(sum(punkty)/len(punkty), 2)
print('srednie: ', sr)


# • Oblicz, ile osób zdobyło punkty powyżej, a ile poniżej średniej
upper = []
lower = []
for i in punkty:
    if i > sr:
        upper.append(i)
    elif i < sr:
        lower.append(i)
print(lower, upper)
print('lower:',len(lower), '| upper:',len(upper))






