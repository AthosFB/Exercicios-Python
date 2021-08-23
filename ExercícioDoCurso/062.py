t1 = float(input("Coloque o 1º Termo: "))
rz = float(input("Coloque A Razão: "))
c = 10
r = t1
total = 10
mais = 1
while c != 0:
    print("{}".format(r), end=" > ")
    r = r + rz
    c -= 1
print("Fim")
while mais != 0:
    mais = int(input("\nQuantos Termos a Mais Você quer ver: "))
    for k in range(1, mais + 1):
        print(r, end=" > ")
        r = r + rz
        total += 1
    print("Pausa" if mais != 0 else " ", "\nFim. Foram mostrados {} termos".format(total))
