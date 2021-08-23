lista = []
cont = " "
while True:
    n = int(input("Coloque um número: "))
    lista.append(n)
    while cont not in "SN":
        cont = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if cont == "N":
        break
    cont = " "
print(f"Você digitou {len(lista)} elementos")
lista.sort(reverse=True)
print(f"Os valores em ordem decresente são: {lista}")
if 5 in lista:
    print("O valor 5 enta na lista!")
else:
    print("O valor 5 não esta presente na lista!")
