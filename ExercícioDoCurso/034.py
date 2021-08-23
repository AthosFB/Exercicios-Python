salario = float(input("\033[1;33mColoque seu salário:\033[m "))
sal1 = (salario * 1.50)
sal2 = (salario * 1.30)
sal3 = (salario * 1.10)
sal4 = (salario * 1.05)
if salario <= 1000:
    print("De R$\033[1;31m{:.2f}\033[m Você vai para R$\033[1;32m{:.2f}\033[m".format(salario, sal1))
elif salario >= 1000 and salario <= 2000:
    print("De R$\033[1;31m{:.2f}\033[m Você vai para R$\033[1;32m{:.2f}\033[m".format(salario, sal2))
elif salario >= 2000 and salario <= 7000:
    print("De R$\033[1;31m{:.2f}\033[m Você vai para R$\033[1;32m{:.2f}\033[m".format(salario, sal3))
else:
    print("De R$\033[1;31m{:.2f}\033[m Você vai para R$\033[1;32m{:.2f}\033[m".format(salario, sal4))


