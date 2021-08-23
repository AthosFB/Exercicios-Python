s = 0
k = 0
n = int(input("Coloque um número inteiro: "))
'''print()
for c in range(2, 11):
    if n % c > 0:
        k = k + 1
if k == 9:
    print("número Primo")
else:
    print("Número não Primo")'''

for c in range(1, n+1):
    if n % c == 0:
        print("\033[33m{}".format(c), end=" ")
        k = k + 1
    else:
        print("\033[31m{}".format(c), end=" ")
print("\n\033[1;97mO número {}, foi divisível {} vezes.".format(n, k))
if k == 2:
    print("Então ele  é um número primo")
else:
    print("Então ele não é um número primo.")
