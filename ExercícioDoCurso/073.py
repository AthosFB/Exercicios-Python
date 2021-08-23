times = ("Palmeiras", "Cruzeiro", "Grêmio", "Santos", "Corinthians", "Flamengo", "Atlético Mineiro",
         "Athletico Paranaense", "Internacional", "Chapecoense", "Botafogo", "São Paulo", "Fluminense", "Vasco da Gama",
         "Bahia", "Sport", "Vitória", "Ponte Preta", "América", "Coritiba")
print("---" * 20)
for enu, t in enumerate(times):
    print(f"{enu + 1}º {t}")
print("---" * 20)
print(f"Os 5 primeiros são {times[:5]}")
print("---" * 20)
print(f"Os 4 ultimos são {times[-4:]}")
print("---" * 20)
print(f"Times em ordem alfabética {sorted(times)}")
print("---" * 20)
print(f"O Chapecoense esta na {times.index('Chapecoense') + 1} posição")
