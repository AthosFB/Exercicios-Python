s = 0
k = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c
        k = k + 1
print()
print("A soma desses {} valores resulta {}".format(k, s))
