listap = []
listai = []
lista = []
cont = " "
add = 0
while True:
    n = int(input("Coloque um valor: "))
    lista.append(n)
    while cont not in "SN":
        cont = str(input("Deseja continuar: [S/N] ")).strip().upper()[0]
    if cont == "N":
        break
    cont = " "
tot = len(lista)
while add != tot:
    if lista[add] % 2 == 0:
        listap.append(lista[add])
    else:
        listai.append(lista[add])
    add += 1
lista.sort()
listap.sort()
listai.sort()
print(f"A lista inteira {lista}")
print(f"A lista de pares {listap}")
print(f"A lista de impares {listai}")
