nome = str(input("Coloque seu Nome: "))
a = nome.title()
b = a.strip()
c = a.count("Favaron")
k = a.count("Bernardo")
print("Você tem Favaron no nome?", c == 1)
print("Você tem Bernardo no nome?", k == 1)