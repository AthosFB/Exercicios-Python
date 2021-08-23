md = mc = mv = 0
sexo = avan = " "
print("---" * 10)
print("   Cadastrador De Pessoas")
print("---" * 10)
while True:
    idade = int(input("Idade: "))
    print("---" * 10)
    if idade >= 18:
        md += 1
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F]")).strip().upper()[0]
        print("---" * 10)
    if sexo in "M":
        mc += 1
    if idade < 20 and sexo == "F":
        mv += 1
    while avan not in "SN":
        avan = str(input("Continuar? [S/N]")).strip().upper()[0]
        print("---" * 10)
    if avan == "N":
        break
    sexo = avan = " "
print(f"Temos {md} pessoas com mais de 18 anos")
print("---" * 10)
print(f"Temos {mc} Homens cadastrados")
print("---" * 10)
print(f"Temos ao todo {mv} mulheres com menos de 20 anos")
print("---" * 10)
