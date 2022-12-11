s = input('print list (metoda 1):');

while len(s) > 0:
    list = s[0]
    if list>='a' and list<='z':
        print(list.upper())
    elif list>='A' and list<='Z':
        print(list.lower())
    s=s[1:]

x = str(input("print list (metoda 2): "))
print(x.swapcase())