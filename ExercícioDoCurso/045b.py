from random import randint
from time import sleep
from sys import stdout
print("""[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura""")
jogador = int(input("Opção: "))
lista = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
computer = lista[computador]

def animation():
    stdout.write("\rPedra.")
    sleep(0.7)
    stdout.write("\rPapel..")
    sleep(0.7)
    stdout.write("\rTesoura...")
    sleep(0.5)
    stdout.write("\r \n")
    sleep(0.4)
animation()
if jogador == 1 and computer == "Pedra":
    print("EMPATE! Os 2 Escolhera Pedra")
elif jogador == 1 and computer == "Papel":
    print("Computador Venceu. Escolhendo Papel")
elif jogador == 1 and computer == "Tesoura":
    print("Jogador Venceu! Escolhendo Pedra")

if jogador == 2 and computer == "Pedra":
    print("Jogador Venceu! Escolhendo Papel")
elif jogador == 2 and computer == "Papel":
    print("EMPATE! Os 2 Escolhera Papel")
elif jogador == 2 and computer == "Tesoura":
    print("Computador Venceu. Escolhendo Tesoura")

if jogador == 3 and computer == "Pedra":
    print("Computador Venceu. Escolhendo Pedra")
elif jogador == 3 and computer == "Papel":
    print("Jogador Venceu! Escolhendo Tesoura")
elif jogador == 3 and computer == "Tesoura":
    print("EMPATE! Os 2 Escolhera Tesoura")