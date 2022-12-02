# 1 + 2
# 1 + 4.5
# 3 / 2
# 4 / 2
# 3 // 2
# -3 // 2
# 11 % 2
# 2 ** 10
# 8 ** (1/3)

# x = 1 + 2
# print(x, type(x))
#
# x = 1 + 4.5
# print(x, type(x))
#
# x = 3 / 2
# print(x, type(x))
#
# x = 4 / 2
# print(x, type(x))
#
# x = 3 // 2
# print(x, type(x))
#
# x = -3 // 2
# print(x, type(x))
#
# x = 11 % 2
# print(x, type(x))
#
# x = 2 ** 10
# print(x, type(x))
#
# x = 8 ** (1/3)
# print(x, type(x))


x = int(3.0)
print(x, type(x))
x = float(3)
print(x, type(x))
x = float("3")
print(x, type(x))
x = str(12.4)
print(x, type(x))
x = bool(0)
print(x, type(x))

# Napisz skrypt, który pobiera długości boków prostokąta, a następnie oblicza jego pole i obwód
# oraz wyświetla wyniki na ekranie.
a = int(input('bok a: '))
b = int(input('bok b: '))

perimeter = 2*(a+b)
area = a*b
print('perimeter: ', perimeter)
print('area: ', area)

# Wykorzystaj f-stringi do wyświetlenia wyników
print(f"perimeter: {perimeter}")
print(f"area: {area}")