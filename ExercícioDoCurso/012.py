valor = float(input('Coloque o preço do produto: R$'))
cinco = valor / 100 * 95
dez = valor / 100 * 90
quinze = valor / 100 * 85
vinte = valor / 100 * 80
vintecinco = valor / 100 * 75
trinta  = valor / 100 * 70
print('5% de desconto {:.2f}'.format(cinco))
print('10% de desconto {:.2f}'.format(dez))
print('15% de desconto {:.2f}'.format(quinze))
print('20% de desconto {:.2f}'.format(vinte))
print('25% de desconto {:.2f}'.format(vintecinco))
print('30% de desconto {:.2f}'.format(trinta))
