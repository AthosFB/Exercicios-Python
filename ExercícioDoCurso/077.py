palavras = ("COMPUTADOR", "TECNOLOGIA", "DINHEIRO", "JOGOS", "CERTIFICADO")
print()
print("Consoantes")
print()
for p in palavras:
    print(f"\nNa palavra {p} temos as consoantes: ", end=" ")
    for letra in p:
        if letra in "BCDFGHJKLMNPQRSTVWXYZ":
            print(letra, end=" ")
print("\n")
print("Vogais")
print()
for pa in palavras:
    print(f"\nNa palavra {pa} temos as vogais: ", end=" ")
    for letra in pa:
        if letra in "AEIOU":
            print(letra, end=" ")
