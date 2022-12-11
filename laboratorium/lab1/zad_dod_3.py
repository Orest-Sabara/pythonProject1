# ax^2 + bx + c = 0

import math
print('ax^2 + bx + c = 0')
print('Enter a b c')

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = b**2-4*a*c
print('Discriminant', d)

if d > 0:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print(f'x1 = {x1:.2f}, x2 = {x2:.2f}')
elif d == 0:
     x = (-b)/(2*a)
     print('x =', x)
elif d < 0:
    print("nie ma rozwiązań")



