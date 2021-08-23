from Ex109 import moeda
valo = float(input("Coloque o preço: R$"))
print()
print(f"O dobro de {moeda.moeda(valo)} é {moeda.dobro(valo, formatador=True)}")
print(f"A metade de {moeda.moeda(valo)} é {moeda.metade(valo, formatador=True)}")
print(f"10% a mais de {moeda.moeda(valo)} é {moeda.aumentar(valo, taxa=10, formatador=True)}")
print(f"23% a menos de {moeda.moeda(valo)} é {moeda.diminuir(valo, taxa=23, formatador=True)}")
