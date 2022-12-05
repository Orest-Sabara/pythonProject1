# Napisz funkcję o zmiennej liczbie parametrów, która wyświetla wartości parametrów na ekranie.
# Następnie zmodyfikuj funkcję tak, aby znajdowała i zwracała wartość maksymalną.

def zad_3(*args):
    print(args)
    for i in args:
        print(i)
    print()

zad_3(2,4,5,6,7,8,436,247,247)
zad_3('hi', 2, True)

def maximum(arg1, *args):
    print(args)
    k = arg1
    for i in args:
        if i>k:
            k = i
    return k

print(maximum('fs','asdf','asf','y'))
print(maximum(2,421,-215,152,12))
