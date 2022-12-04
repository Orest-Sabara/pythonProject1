import random

u = int(input('podai lichbe :'))
zestaw_1 = []
for i in range(u):
    x = random.randint(1, 10)
    zestaw_1.append(x)
print(zestaw_1)

u = int(input('podai lichbe :'))
zestaw_2 = []
for i in range(u):
    x = random.randint(5, 15)
    zestaw_2.append(x)
print(zestaw_2)

# u = int(input("podaj lichbe: "))
# zestaw_2 = [random.randint(5,15) for i in range(u) ]
# print(zestaw_2)


g = int(input('podai lichbe: '))
if g in zestaw_1:
    print('Liczba z zestawu_1: ')
elif g in zestaw_2:
    print('Liczba z zestawu_2: ')
else:
    print('Nie ma takiej liczby w obu zestawach')


zestaw_1_2 = zestaw_1 + zestaw_2
print('zestaw_1 + zestaw_2 :', zestaw_1_2)
