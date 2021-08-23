soma = conta = n = 0
n = float(input("Coloque um número [999 Para parar]: "))
while n != 999:
    conta += 1
    soma += n
    n = float(input("Coloque um número [999 Para parar]: "))
print("Foram {} números E a soma deles foi {}".format(conta, soma))
