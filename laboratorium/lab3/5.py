 # Grupa laboratoryjna składa się z n studentów (wartość n podaje użytkownik).
 # Wprowadzamy liczbę punktów dla każdego studenta. Napisz program,
 # który obliczy średnią liczbę punktów w grupie z wykorzystaniem pętli while.

n = int(input('how many students in the class? '))
i = 1
suma = 0
while i <= n:
    x = int(input(f'podai licbę punktów studenta{i}: '))
    i += 1
    suma = suma + x
sred = suma/n
print(sred)



