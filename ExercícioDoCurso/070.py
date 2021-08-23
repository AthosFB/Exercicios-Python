precotot = mm = mb = 0
cont = mbn = " "
while True:
    print("===" * 10)
    np = str(input("Coloque o nome do Produto: ")).title()
    print("===" * 10)
    preco = float(input("Coloque o preço do Produto: R$"))
    precotot += preco
    if preco >= 1000:
        mm += 1
    if mb == 0:
        mb = preco
        mbn = np
    elif preco < mb:
        mb = preco
        mbn = np
    while cont not in "SN":
        print("===" * 10)
        cont = str(input("Deseja Continuar? [S/N] ")).strip().upper()[0]
    if cont == "N":
        break
    cont = " "
print("===" * 10)
print(f"O preço total das compras ficou em R${precotot}")
print("===" * 10)
print(f"Teve {mm} produtos custando mais que R$1000,00")
print("===" * 10)
print(f"O produto mais barato foi o {mbn} custando R${mb }")
print("===" * 10)
