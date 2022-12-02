age = int(input('wiek klienta: '))
cena = 0

if age < 4:
    cena = 0
elif age <= 18:
    cena = 10
else:
    cena = 20

print(f"bilet kosztuje {cena}z")