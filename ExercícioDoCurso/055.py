pt = pm = pmi = 0
for c in range(1, 6):
    peso = float(input("Coloque o Peso Da {}º Pessoa: ".format(c)))
    pt += peso
    if peso > pm:
        pm = peso
    if c == 1 or peso < pmi:
        pmi = peso
print()
print("A pessoa Mais leve pesa {}Kg".format(pmi))
print("A pessoa Mais pesada pesa {}Kg".format(pm))
print("Na média Cada Um pesa {}Kg".format(pt / 5))
