n = int(input('how many students in the class? '))
i = 1
suma = 0
while i <= n:
    x = int(input(f'podai licbę punktów studenta{i}: '))
    if x<0 or x>100:continue
    i += 1
    suma = suma + x
sred = suma/n
print(sred)


# while True
#     i += 1
#     suma = suma + x
#     if i > n:
#       if i>=+1
#         break