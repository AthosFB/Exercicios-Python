peso = float(input("Qual é o seu peso? (Kg)"))
altura = float(input("Qual é a sua altura? (m)"))
print()
imc = (peso / altura ** 2)
print("Seu IMC é de {:.2f}".format(imc))
if imc <= 18.5:
    print("\033[1;31mVocê está Abaixo do peso!")
elif 18.5 < imc <= 25:
    print("\033[1;32mVocê está no Peso ideal!")
elif 25 < imc <= 30:
    print("\033[1;33mVocê está acima do peso!")
elif 30 < imc <= 40:
    print("\033[1;31mVocê está Obeso!")
else:
    print("\033[4;31mVocê tem Obesidade Mórbida!!!")