dia = int(input('Quantos dias ficou com o carro? '))
km = float(input('Quantos kilometros foram rodados? '))
gas = float(input('Sobrou alguma gasolina que você pagou no tanque? (em litros) '))
calc = dia * 60 + km * 0.15 - gas
print('O valor total do aluguel por {} dias e {}km menos R$1 por litro ficou R${:.2f}'.format(dia, km, calc))
