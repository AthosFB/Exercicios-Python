cidade = str(input("Coloque a cidade que você nasceu: "))
a = cidade.strip()
b = a.title()
c = b.split()
d = c[0].count("Campinas")
if d == 1:
    print("True")
else:
    print("False")

print(b[:5] == "Santo")