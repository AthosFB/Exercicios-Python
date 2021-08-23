from Ex107 import moeda
valo = float(input("Digite o valor: R$"))
print(f"O dobro de {valo} é {moeda.dobro(valo)}")
print(f"A metade de {valo} é {moeda.metade(valo)}")
print(f"10% a mais de {valo} é {moeda.aumentar(valo, taxa=10)}")
print(f"13% a menos de {valo} é {moeda.diminuir(valo, taxa=13)}")
