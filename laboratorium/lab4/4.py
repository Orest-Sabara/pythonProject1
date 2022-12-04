imiona = ['Kasia', 'Tomek', 'Jan', 'Ola', 'Jerzy', 'Marek', 'Piotr', 'Zuzia', 'Bartek', 'Jacek']

# Zmień imię znajdujące się na czwartej pozycji
imiona[3] = 'Oleg'
print(imiona)

# • Wstaw dowolne imię jako piąty element
imiona.insert(4, 'Igor')
print(imiona)

# • Usuń siódmy element z listy
imiona.pop(6)
print(imiona)

# • Dodaj do listy trzy ulubione imienia na trzech pierwszych pozycjach
imiona.insert(0,'Diana')
imiona.insert(1,'Orest')
imiona.insert(2,'Tom')
print(imiona)

# • Usuń z listy imię podane przez użytkownika
i = input('podai imię: ')
if i in imiona:
    imiona.remove(i)
    print(imiona)
else:
    print('nema takogo')

# • Zmień ostatnie imię na liście
imiona.insert(len(imiona),'Johny')
print(imiona)

# • Wyświetl trzy pierwsze oraz trzy ostatnie imienia na liście
print(imiona[:3])
print(imiona[-3:])

# • Pobierz imię od użytkownika. Wyświetl informację, czy podane imię znajduje się na Twojej liście.
im = input('podai imię: ')
if im in imiona:
    print(im, '- jest take imię')
else:
    print('nema takogo')

# • Wyświetl posortowaną listę
imiona.sort()
print(imiona)

# • Wyświetl imiona w kolejności od Z do A
imiona.sort(reverse=True)
print(imiona)

# • Wyczyść drugą połowę listy, następnie wyświetl liczbę elementów listy.
j = int(len(imiona)/2)
while j < len(imiona):
    imiona.pop(j)
print(imiona)