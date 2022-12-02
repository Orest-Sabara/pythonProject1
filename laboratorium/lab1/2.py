# Napisz skrypt, który pobiera od użytkownika drogę pokonaną przez samochód oraz
# średnie spalanie (w litrach na 100 km) i wyświetli informację o przewidywanym zużyciu
# paliwa oraz o szacowanych kosztach podróży (cena paliwa 6.5 zł/l).

droga = float(input('podai drogę : '))
sredneSpalanie = float(input('podai średnie spalanie : '))

z = (droga / 100) * sredneSpalanie
print('zużyciu paliwa', z)
print('kosztach podróży', (z * 6.5))
