print(''' Jaką operację chcesz wykonać?   
      1) dodawanie   
      2) odejmowanie   
      3) mnożenie   
      4) dzielenie   
      5) potęgowanie ''')

dzialangie = int(input("wpisz numer operacji: "))
arg1 = float(input('podaj argument 1: '))
arg2 = float(input('podaj argument 2: '))

if dzialangie == 1:
    w = arg1 + arg2
elif dzialangie == 2:
    w = arg1 - arg2
elif dzialangie == 2:
    w = arg1 * arg2
elif dzialangie == 2:
    w = arg1 / arg2
elif dzialangie == 2:
    w = arg1 ** arg2

print(f'Wynik = {w}')