from random import randint
from time import sleep


def maior(a):
    print("-=" * 20)
    print("Analizando os valores...")
    sleep(1)
    lista = list()
    for c in range(0, a):
        lista.append(randint(1, 10))
    for i in lista:
        print(i, end=" ")
    print(f"Foram informados {len(lista)} valores ao todo")
    if len(lista) == 0:
        print(f"O maior valor informado foi o 0")
    else:
        print(f"O maior valor informado foi o {max(lista)}")
    print("-=" * 20)


maior(a=6)
print()
maior(a=3)
print()
maior(a=2)
print()
maior(a=1)
print()
maior(a=0)
