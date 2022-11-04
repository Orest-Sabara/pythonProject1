# thistuple = ('apple', 'banana', 'cherry')
#
# print(thistuple)
#
# print(len(thistuple))
#
# thistuple1 = ('apple',)
# print(type(thistuple1))
# # <class 'tuple'>
#
# thistuple1 = ('apple')
# print(type(thistuple1))
# # <class 'str'>
#
# tuple1 = ('abc', 34, True, 40, 'male')
# print(tuple1[0])
#
#
# thistuple = tuple(('apple', 'banana', 'cherry'))
# print(thistuple)
# # подвійні дужки tuple
#
# thistuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
# print(thistuple[-1])
# print(thistuple[2:5])
#
# thistuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
# if 'apple' in thistuple:
#     print('yes "apple" is in the fruits tuple')
#
# x = ('apple', 'banana', 'cherry')
# y = list(x)
# y[1] = 'kiwi'
# x = tuple(y)
#
# print(x)
# # ('apple', 'kiwi', 'cherry')
#
# thistuple = ('apple', 'banana', 'cherry')
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)
# # thistuple += y
#
# thistuple = ('apple', 'banana', 'apple', 'cherry')
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)
#
# thistuple = ('apple', 'banana', 'apple', 'cherry')
# del thistuple
# print(thistuple)

# print('-------------------------------')
# fruits = ('apple', 'banana', 'cherry')
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)
#
# print('-------------------------------')
# fruits = ('apple', 'banana', 'cherry')
# (green, *yellow) = fruits
# print(green)
# print(yellow)
#
# print('-------------------------------')
# fruits = ('apple', 'mango', 'papaya', 'pineapple', 'cherry')
# (green, *tropic, red) = fruits
# print(green)
# print(tropic)
# print(red)
#
# print('-------------------------------')
# fruits = ('apple', 'mango', 'papaya', 'pineapple', 'cherry')
# for x in fruits:
#     print(x)
#
# print('-------------------------------')
# print((len(fruits)))
# print(range (len(fruits)))
# for i in range (len(fruits)):
#     print(i, fruits[i])
#
# print('-------------------------------')
# thistuple = ('apple', 'mango', 'papaya', 'pineapple', 'cherry')
# i = 0
# while i < len(thistuple):
#     print(i, thistuple[i])
#     i += 1
#
# print('-------------------------------')
# tuple1 = ('a', 'b', 'c')
# tuple2 = (1,2,3)
# tuple3 = tuple1 + tuple2
# print(tuple3)
#
# print('-------------------------------')
# tuple1 = ('a', 'b', 'c')
# mytuple = tuple1 * 2
# print(mytuple)

print('-------------Sety------------------')
# ne indexowanui
thisset = {'apple', 'banana', 'cherry'}
print(thisset)

thisset = {'apple', 'banana', 'cherry', 'apple'}
print(thisset)

thisset = {'apple', 'banana', 'cherry', 'apple'}
thisset.add('pear')
print(thisset)

thisset = {'apple', 'banana', 'cherry', 'apple'}
print(len(thisset))
# 3

thisset = {'apple', 'banana', 'cherry', 'apple'}
print(type(thisset))

thisset = {'apple', 'banana', 'cherry', 'apple'}
for x in thisset:
    print(x)

print('banana' in thisset)
# True

thisset = set(('apple', 'banana', 'cherry', 'apple'))
print('banana' in thisset)
# True

thisset = {'apple', 'banana', 'cherry'}
thisset.add('orange')
print(thisset)

thisset = {'apple', 'banana', 'cherry'}
tropical = {'pineapple', 'mango', 'papaya'}
thisset.update(tropical)
print(thisset)

thisset = {'apple', 'banana', 'cherry'}
mylist = ['kiwi', 'orange']
thisset.update(mylist)
print(thisset)

thisset = {'apple', 'banana', 'cherry'}
thisset.remove('banana')
print(thisset)

print('--------------------------------')
thisset = {'apple', 'banana', 'cherry'}
thisset.discard('banana')
print(thisset)

print('--------------------------------')
thisset = {'apple', 'banana', 'cherry'}
x = thisset.pop()
print(x)
print('--------------------------------')
print(thisset)
