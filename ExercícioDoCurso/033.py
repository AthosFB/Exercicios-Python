op1 = float(input("Coloque o 1º valor: "))
op2 = float(input("Coloque o 2º valor: "))
op3 = float(input("Coloque o 3º valor: "))


"""print("_-=-_" * 5)
if op1 > op2:
    if op1 > op3:
        print("A opção 1 é a maior {}".format(op1))
    else:
        print("A opção 3 é a maior {}".format(op3))
elif op2 > op3:
    print("A opção 2 é a maior {}".format(op2))
else:
    print("A opção 3 é a maior {}".format(op3))

print("_-=-_" * 5)

if op1 < op2:
    if op1 < op3:
        print("A opção 1 é a menor {}".format(op1))
    else:
        print("A opção 3 é a menor {}".format(op3))
elif op2 < op3:
    print("A opção 2 é a menor {}".format(op2))
else:
    print("A opção 3 é a menor {}".format(op3))
print("_-=-_" * 5)"""

#Estrutura end
print("_-=-_" * 5)
if op1 > op2 and op1 > op3:
    print("A opção 1 é a maior {}".format(op1))
elif op2 > op1 and op2 > op3:
    print("A opção 2 é a maior {}".format(op2))
else:
    print("A opção 3 é a maior {}".format(op3))

print("_-=-_" * 5)

if op1 < op2 and op1 < op3:
    print("A opção 1 é a menor {}".format(op1))
elif op2 < op1 and op2 < op3:
    print("A opção 2 é a menor {}".format(op2))
else:
    print("A opção 3 é a menor {}".format(op3))
print("_-=-_" * 5)
