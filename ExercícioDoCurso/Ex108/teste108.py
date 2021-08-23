from Ex108 import moeda
valo = float(input("Coloque o preço: R$"))
print(f"O dobro de {valo} é {moeda.moeda(moeda.dobro(valo))}")
print(f"A metade de {valo} é {moeda.moeda(moeda.metade(valo))}")
print(f"10% a mais de {valo} é {moeda.moeda(moeda.aumentar(valo, taxa=10))}")
print(f"23% a menos de {valo} é {moeda.moeda(moeda.diminuir(valo, taxa=23))}")
