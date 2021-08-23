cont = "S"
tot = maior = contador = 0
menor = 9999999999999999999999999999999999999999
while cont in "S":
    n = float(input("Coloque um número: "))
    cont = str(input("Deseja Continuar: [S/N]")).upper().strip()[0]
    tot += n
    contador += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
media = tot / contador
print("Foram digitados {} números, a média entre ele foi de {}.".format(contador, media))
print("O maior Foi {} e o menor {}".format(maior, menor))
