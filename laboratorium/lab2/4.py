# Napisz skrypt, która zamienia wprowadzoną literę na przeciwną (co do wielkości)
# i wypisuje ją na ekranie.

s = input('print list :');

while len(s) > 0:
    list = s[0]
    if list>='a' and list<='z':
        print(list.upper())
    elif list>='A' and list<='Z':
        print(list.lower())
    s=s[1:]