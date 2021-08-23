from datetime import date
ano = int(input("Coloque O ano que você nasceu: "))
idade = (date.today().year - ano)
print()
print("Você tem {} anos".format(idade))
if idade <= 9:
    print("Atleta Mirim.")
elif idade > 9 and idade <= 14:
    print("Atleta Infantil.")
elif idade > 14 and idade <= 19:
    print("Atleta Júnior.")
elif idade > 19 and idade <= 25:
    print("Atleta Sênior.")
else:
    print("Atleta Master.")
