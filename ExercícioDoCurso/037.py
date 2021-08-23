import sys
import time
print("\033[1;33m-=-" * 3)
num = int(input("Coloque um número: "))
print("\033[1;33m-=-" * 3)
print("[ 1 ] Para Binário")
print("\033[1;33m-=-" * 3)
print("[ 2 ] Para Octal")
print("\033[1;33m-=-" * 3)
print("[ 3 ] Para Hexadecimal")
print("\033[1;33m-=-" * 3)
op = int(input("Sua opção: "))
print("\033[1;33m-=-" * 3)
def animation():
    sys.stdout.write("\r\033[1;31m(")
    time.sleep(0.3)
    sys.stdout.write("\r\033[1;31m )")
    time.sleep(0.3)
    sys.stdout.write("\r\033[1;31m()")
    time.sleep(0.3)
    sys.stdout.write("\r\033[1;31m(")
    time.sleep(0.3)
    sys.stdout.write("\r\033[1;31m )")
    time.sleep(0.3)
    sys.stdout.write("\r\033[1;31m()")
    time.sleep(0.3)
    sys.stdout.write("\r\033[1;32mCarregado...")
    time.sleep(1)
    sys.stdout.write("\r \n")
    time.sleep(0.01)
animation()
print("\033[1;33m-=-" * 3)

bi = bin(num)
octa = oct(num)
hexa = hex(num)


if op == 1:
    print("O número {} em Binário é {}".format(num, bi[2:]))

elif op == 2:
    print("O número {} em Octal é {}".format(num, octa[2:]))

elif op == 3:
    print("O número {} em Hexadecimal é {}".format(num, hexa[2:]))

else:
    print("\033[1;31mColoque um número de 1 a 3!")