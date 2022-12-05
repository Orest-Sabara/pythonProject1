# Napisz funkcje oblicz(), która ma dwa parametry i oblicza ich sumę oraz różnicę.
# Ponadto zwraca jednocześnie jak wynik dodawania, tak i odejmowania.

def oblicz(arg1, arg2):
    sum = arg1 + arg2
    riz = arg1 - arg2
    return sum, riz

print(oblicz(2,2))

zm1, zm2 = oblicz(2, 6)
print(f'suma = {zm1}, rizn = {zm2}')