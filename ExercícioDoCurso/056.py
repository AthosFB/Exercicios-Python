ida = 0
mida = 0
med = 0
hmv = "Não Tem"
for c in range(1, 5):
    print("+" * 5, "{}º Pessoa".format(c), "+" * 5)
    nome = input("Coloque Seu Nome: ")
    idade = int(input("Coloque Sua Idade: "))
    HM = input("Homem Ou Mulher: [H/M] ").upper()
    ida += idade
    if HM == "H":
        if idade > med:
            hmv = nome
            med = idade
    if HM == "M" and idade < 20:
            mida += 1
print()
print("A idade média do grupo é {}".format(ida / 4))
print("O Homem mais velho é o {} Com {} Anos".format(hmv, med))
print("Tem {} Mulhere(s) Com Menos de 20 Anos".format(mida))

