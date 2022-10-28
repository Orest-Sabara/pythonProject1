# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#     print("Both conditions are True")
#
# a = 200
# b = 33
# c = 500
# if a > b or c > a:
#     print("Both conditions are True")


x = 1
if x > 10:
    print('Above ten,')
    if x > 20:
        print('and also above 20!')
    else:
        print('but not above 20.')
else:
    print('Below 10.')


a = 33
b = 200
if b > a:
    pass
# перходить до наступного блоку


i = 1
while i < 6:
    print(i)
    i += 1

i = 0
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# перериває операцію повністю

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# перериває тільки 1 операцію

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print('i is not longer less than 6')


fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)

fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)
    if x == 'banana':
        break

for x in range(6):
    print(x)

for x in range(2,6):
    print(x)
print(range(2,6))

for x in range(2, 30, 3):
    print(x)
# 2-початок. 30 - кінець. 3-в скільки разів збільшується початкове число

adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']
for x in adj:
    for y in fruits:
        print(x, y)
    print()