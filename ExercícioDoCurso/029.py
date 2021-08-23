import time
import sys
velo = int(input("A qual velocidade você está? "))
multa = (velo / 15) * 40

def animate():
    print("-" * 11)
    sys.stdout.write("\rloading")
    time.sleep(0.4)
    sys.stdout.write("\rloading.")
    time.sleep(0.4)
    sys.stdout.write("\rloading..")
    time.sleep(0.4)
    sys.stdout.write("\rloading...")
    time.sleep(0.4)
    sys.stdout.write("\rloading")
    time.sleep(0.4)
    sys.stdout.write("\rloading.")
    time.sleep(0.4)
    sys.stdout.write("\rloading..")
    time.sleep(0.4)
    sys.stdout.write("\rloading...")
    time.sleep(0.4)
    sys.stdout.write("\rloading")
    time.sleep(0.4)
    sys.stdout.write("\rloaded")
    time.sleep(0.8)
    sys.stdout.write("\r \n")
    print("-" * 60)
animate()
if velo <= 80:
    if velo >= 40:
        print("Você esta dentro do limite de velocidade, Boa Viagem!")
    else:
        print("Pode acelerar mais um Pouco, está muito devagar!")
else:
    print("Você esta acima do limite de velocidade e pagara um total de R${:.2f}".format(multa))
print("-" * 60)
