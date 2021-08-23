termos = int(input("Quantos termos quer mostrar: "))
contador = termos - 2
ant = 0
novo = 1
print("~~~~" * termos)
print(0, end=", ")
print(1, end=", ")
while contador != 0:
    soma = ant + novo
    print("{}, ".format(soma), end=" ")
    contador -= 1
    ant = novo
    novo = soma
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Acabou")
print("~~~~" * 5)
