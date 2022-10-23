x = 100
y = 100
print(x is y)

print(bin(x))
# бінарна переводить

thisList = ['asd', 'asd', 'afs']
print(thisList)

print(len(thisList))
# довжина

list = ['asd', 'asd', 'afs', True, 'false' , 69]
print(type(list[0]))

print(list[-1])
# last element

list1 = ['orange', 'red', 'blue', True, 'false' , 69, 241, 24]
print(list1[2:5])
# від 2 до 5
print(list1[:4])
# до 4
print(list1[3:])
# від 3

a = 33
b = 200
# if b > a:
#     print('b is greater than a')
#     # якщо b більше а виконується
# print('test')
# # якщо a більше b виконується


if b < a:
    print('b is greater than a')
    # якщо b більше а виконується
else:
    print('a is greater than b')
    # якщо a більше b виконується


bb=15
aa=15
if bb < aa:
    print('b is greater than a')
    # якщо b більше а виконується
elif aa == bb:
    print('a and b are equal')
else:
    print('a is greater than b')
    # якщо a більше b виконується


ax = 1
bx = 2
print('A') if ax > bx else print("B")