import random

droga=random.randint(1,1000)
print('droga :', droga)

sredneSpalanie = float(input('podai średnie spalanie : '))

z = (droga / 100) * sredneSpalanie
print('zużyciu paliwa', z)
print('kosztach podróży', (z * 6.5))