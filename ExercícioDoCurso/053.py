a = str(input("Coloque um Frase: "))
print()
b = a.replace(" ", "").upper()
if b == b[::-1]:
    print("A frase {} é um Palíndromo {}".format(a, a[::-1]))
else:
    print("A frase {} Não é um Palíndromo {}".format(a, a[::-1]))
