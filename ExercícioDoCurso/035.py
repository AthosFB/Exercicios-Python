print("\033[33m-=-" * 10)
l1 = float(input("Coloque a medida do 1º lado: "))
print("\033[33m-=-" * 10)
l2 = float(input("Coloque a medida do 2º lado: "))
print("\033[33m-=-" * 10)
l3 = float(input("Coloque a medida do 3º lado: "))
print("\033[33m-=-" * 10)

if l1 + l2 > l3:
    if l1 + l3 > l2:
        if l3 + l2 > l1:
            print("\033[36mEssas medidas formam um triângulo!\033[33m")
            print("-=-" * 10)
        else:
            print("\033[36mEssas medidas não formam um triângulo :(\033[33m")
            print("-=-" * 10)