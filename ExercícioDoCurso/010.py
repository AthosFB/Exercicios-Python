moeda = float(input('Quantos reais você tem? R$'))
vari = input('Qual moeda deseja? (dólar, euro ou libra)')
if (vari == 'dólar'):
    print()
    print('Você pode comprar US${:.2f} (Dólar)'.format(moeda / 5.49))
elif (vari == 'euro'):
    print()
    print('Você pode comprar €{:.2f} (Euro)'.format(moeda / 6.56))
elif (vari == 'libra'):
    print()
    print('Você pode comprar £{:.2f} (Libra)'.format(moeda / 7.62))
else:
    print()
    print('Não encontramos essa moeda!!!')