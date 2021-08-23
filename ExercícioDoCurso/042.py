l1 = float(input("Coloque o 1º lado do triângulo: "))
l2 = float(input("Coloque o 2º lado do triângulo: "))
l3 = float(input("Coloque o 3º lado do triângulo: "))
print()
if l1 + l2 > l3:
    if l1 + l3 > l2:
        if l2 + l3 > l1:
            print("Pode formar um Triângulo", end=" ")
else:
    print("O triângulo não pode ser formado!")
if l1 == l2 ==l3:
    print("Equilátero")
elif l1 == l2 or l1 == l3 or l3 == l2:
    print("Isóscele")
else:
    print("Escaleno")