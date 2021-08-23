num = int(input("Coloque um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
dm = num // 10000 % 10
cm = num // 100000 % 10
mm = num // 1000000 % 10
print("======================")
print("= Unidade           ", u,  "=")
print("= Dezena            ", d,  "=")
print("= Centena           ", c,  "=")
print("= Milhar            ", m,  "=")
print("= Dezena de Milhar  ", dm, "=")
print("= Centena de Milhar ", cm, "=")
print("= Milhão            ", mm, "=")
print("======================")