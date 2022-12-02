# Wejście: 10, 5
# Wyjście: 5, 6, 7, 8, 9, 10

x = int(input('podai lichbe 1: '))
y = int(input('podai lichbe 2: '))
if y < x:
    x, y = y, x
while x<=y:
    print(x, end=' ')
    x += 1