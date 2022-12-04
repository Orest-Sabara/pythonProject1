# Załóżmy, że lista X składa się z 10 elementów.
# Przenieś ostatnie trzy elementy z końca na początek listy
# bez zmiany ich oryginalnej kolejności.

import random
x = [round(random.uniform(0, 30)) for i in range(10)]

print(x)
k = 1
while k <= 3:
    i = x[(len(x) - 1)]
    x.insert(0, i)
    x.pop()
    k += 1
print(x)

# • Utwórz listę Y, wykonując operację: Y = X. Następnie zmień jeden z elementów listy Y.
# Wyświetl obie listyna ekranie.
y = x
y[3] = 'add'
print(x)
print(y)