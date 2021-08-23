from random import randint
a = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print("Os números sorteados são: ", end="")
for n in sorted(a):
    print(n, end=", ")
b = sorted(a)[0]
c = sorted(a)[4]
tot = (a[0] + a[1] + a[2] + a[3] + a[4]) / 5
print(f"\nO menor é o \033[1;32m{b}\033[m, e o maior é o \033[1;32m{c}\033[m, com uma média de \033[1;32m{tot:.2f}")
#ou
print(f"\033[mO maior valor {min(a)} e o menor valor {max(a)}")

