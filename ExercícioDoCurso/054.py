import datetime
ano2 = datetime.date.today().year
k = 0
for c in range(1, 8):
    ano = int(input("Em que ano você nasceu? "))
    if 21 <= ano2 - ano:
        k = k + 1
print("Das 7 pessoas {}, Ja atingiram a maioridade ".format(k))
