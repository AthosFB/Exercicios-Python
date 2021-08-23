print("===" * 10)
print("      Banco Agiota")
print("===" * 10)
valo = int(input("Quanto deseja sacar? R$"))
c = v = d = u = cont = 0
while True:
    if cont + 50 > valo:
        break
    cont += 50
    c += 1
while True:
    if cont + 20 > valo:
        break
    cont += 20
    v += 1
while True:
    if cont + 10 > valo:
        break
    cont += 10
    d += 1
while True:
    if cont + 1 > valo:
        break
    cont += 1
    u += 1
print("===" * 10)
print("           Notas")
print("===" * 10)
print(f"{c} cédulas de R$50,00")
print("===" * 10)
print(f"{v} cédulas de R$20,00")
print("===" * 10)
print(f"{d} cédulas de R$10,00")
print("===" * 10)
print(f"{u} cédulas de R$1,00")
print("===" * 10)
