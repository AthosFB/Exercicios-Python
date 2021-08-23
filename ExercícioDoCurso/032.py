ano = int(input("Que ano quer analisar? "))
if ano % 4 == 0:
    print("(*)=" * 6)
    print("O Ano de {} é BISSEXTO".format(ano))
    print("(*)=" * 6)
else:
    print("(*)=" * 7)
    print("O Ano de {} não é BISSEXTO".format(ano))
    print("(*)=" * 7)