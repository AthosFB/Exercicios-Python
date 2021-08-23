pessoas = list()
info = list()
pmp = list()
cont = " "
mp = ml = 0
while True:
    pessoas.append(str(input("Coloque seu nome: ")))
    pessoas.append(float(input("Coloque seu peso: ")))
    info.append(pessoas[:])
    pessoas.clear()
    while cont not in "SN":
        cont = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if cont == "N":
        break
    cont = " "
print("-=-" * 12)
print(f"Foram cadastradas {len(info)} pessoas.")
for enu, p in enumerate(info):
    if enu == 0:
        mp = p[1]
    elif p[1] > mp:
        mp = p[1]
print(f"O maior pesso foi {mp}Kg. Peso de ", end=" ")
for p in info:
    if p[1] == mp:
        print(p[0], end=" ")

for enu2, p2 in enumerate(info):
    if enu2 == 0:
        ml = p2[1]
    elif p2[1] < ml:
        ml = p2[1]
print(f"\nO menor pesso foi {ml}Kg. Peso de ", end=" ")
for p2 in info:
    if p2[1] == ml:
        print(p2[0], end=" ")
print()
