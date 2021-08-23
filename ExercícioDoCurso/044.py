print("\033[1;97m-=-" * 4, "\033[1;31mAthos's store", "\033[1;97m-=-" * 4)
preço = float(input("Quanto Você Gastou? R$"))
print("-=-" * 10)
print("Como deseja pagar?")
print("-=-" * 10)
print("[ 1 ] à vista dinheiro/cheque.")
print("-=-" * 10)
print("[ 2 ] à vista no cartão.")
print("-=-" * 10)
print("[ 3 ] 2x Parcelas")
print("-=-" * 10)
print("[ 4 ] 3x ou mais Parcelas")
print("-=-" * 10)
op = int(input("Opção escolhida: "))
print("-=-" * 19)
p1 = preço * 0.88
p2 = preço * 0.93
if op == 1:
    print("De \033[1;31mR${:.2f}\033[m Com \033[1;32m12%\033[m de desconto sua compra foi para \033[1;32mR${:.2f}\033[m".format(preço, p1))
elif op == 2:
    print("De \033[1;31mR${:.2f}\033[m Com \033[1;32m7%\033[m de desconto sua compra foi para \033[1;32mR${:.2f}\033[m".format(preço, p2))
elif op == 3:
    print("Serão 2 parcelas de \033[1;32mR${:.2f}\033[m, E o preço das compras continua \033[1;32mR${:.2f}\033[m".format(preço/2, preço))
elif op == 4:
    parcelas = int(input("Quantas parcelas você deseja pagar: "))
    p3 = preço / 100 * (100 + (parcelas * 2))
    print("De \033[1;32mR${:.2f}\033[1;97m sua compra vai para \033[1;31mR${:.2f}\033[m".format(preço, p3))
    print("\033[1;97mSendo {} parcelas De \033[1;31mR${:.2f}".format(parcelas, p3/parcelas))
else:
    print("\033[4;31mOpção Inválida!!!")
    