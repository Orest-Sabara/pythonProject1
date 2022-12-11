a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a > b:
    a = a + b
    b = a - b
    a = a - b
if b > c:
    b = b + c
    c = b - c
    b = b - c
if a > b:
    a = a + b
    b = a - b
    a = a - b

print(a, b, c)