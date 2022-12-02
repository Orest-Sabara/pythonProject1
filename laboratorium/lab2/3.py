print(''' Jaką operację chcesz wykonać?   
      1) dodawanie   
      2) odejmowanie   
      3) mnożenie   
      4) dzielenie   
      5) potęgowanie ''')

numer = int(input("wpisz numer operacji: "))
arg1 = float(input('podaj argument 1: '))
arg2 = float(input('podaj argument 2: '))

if numer == 1:
    w = arg1 + arg2
    print(f'Wynik = {w}')
elif numer == 2:
    w = arg1 - arg2
    print(f'Wynik = {w}')
elif numer == 3:
    w = arg1 * arg2
    print(f'Wynik = {w}')
elif numer == 4:
    w = arg1 / arg2
    print(f'Wynik = {w}')
elif numer == 5:
    w = arg1 ** arg2
    print(f'Wynik = {w}')