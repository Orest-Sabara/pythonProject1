d = str(input("pada deszcz? Enter Y/N:" ))
a = str(input("autobus na przystanku? Enter Y/N:" ))

if d == "Y" and a == "Y":
    print("„Weź parasol”, „Dostaniesz się na uczelnie”")
elif d == "Y" and a == "N":
    print("„Nie dostaniesz się na uczelnię”")
elif d == "N" and a == "Y":
    print("„Dostaniesz się na uczelnie”, „Miłego dnia i pięknej pogody”")