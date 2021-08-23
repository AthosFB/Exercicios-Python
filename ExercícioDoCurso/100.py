from random import randint
from time import sleep
numeros = list()


def sorteia():
    print("---" * 12)
    print("Sorteando os 5 valores da lista: ", end="")
    for c in range(0, 5):
        numeros.append(randint(1, 10))
        print(numeros[c], end="... ")
        sleep(0.5)
    print()
    print("---" * 12)


def somapar():
    print("---" * 12)
    soma = 0
    print(f"Somando os valores pares de {numeros}, temos ", end="")
    sleep(1.5)
    for i in range(0, len(numeros)):
        if numeros[i] % 2 == 0:
            soma += numeros[i]
    print(soma)
    print("---" * 12)


sorteia()
print()
somapar()

