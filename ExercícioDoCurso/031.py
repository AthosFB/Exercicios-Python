car = float(input("Quantos Km seu carro faz com 1L na cidade? "))
dis = float(input("Qantos Km você pretende percorrer? "))
peda = int(input("Qantos pedágios vai passar? "))
valo = (dis / car) * 4.95 + (peda * 5.5) + 10
valo2 = (dis / car) + (peda * 11) - 10
if dis >= 200:
    print("Você gastará R${:.2f}".format(valo2))
else:
    print("Você gastará R${:.2f}".format(valo))