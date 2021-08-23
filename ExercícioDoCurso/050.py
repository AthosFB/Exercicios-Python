s = 0
for c in range(1, 7):
    num = int(input("Coloque um número: "))
    if num % 2 == 0:
        s = s + num
print(s)
