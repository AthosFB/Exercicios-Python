frase = str(input("Coloque uma Frase: "))
a = frase.strip()
b = a.lower()
print("A letra A aparece {} vezes".format(b.count("a")))
print("A 1º letra A aparece na casa", b.find("a") + 1)
print("A ultima letra A aparece na casa", b.rfind("a") + 1)