# Napisz skrypt, który sprawdzi czy litera wprowadzona przez użytkownika jest duża czy mała

s = input('print list :');

while len(s) > 0:
    list = s[0]
    if list>='a' and list<='z':
        print(list, 'small')
    elif list>='A' and list<='Z':
        print(list,'big')
    s=s[1:]