import datetime
ano = int(input("Em que ano você nasceu: "))
ano2 = datetime.date.today().year
idade = (ano2 - ano)
alistamento = 18 - idade
anoalistamento = alistamento + ano2
anoalistamento2 = idade - 18
anolist = ano2 - anoalistamento2
print()
print("Quem nasceu em {} Tem {} Anos".format(ano, idade))
if idade == 18:
    print("\033[1;31mÉ, esse ano você tem que se alistar!")
elif idade < 18:
    print("\033[1;32mFaltam {} anos para seu alistamento".format(alistamento))
    print("Ele ocorrerá no ano de {}\033[m".format(anoalistamento))
else:
    print("\033[1;32mVocê ja se alistou a {} anos".format(anoalistamento2))
    print("\033[1;32mO alistamento foi no ano de {}".format(anolist))
