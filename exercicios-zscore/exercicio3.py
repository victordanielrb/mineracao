temperaturas = [21, 23, 25, 27, 29]
media = 25
desvio = 2

z_scores = [(temperatura - media) / desvio for temperatura in temperaturas]

for temperatura, z in zip(temperaturas, z_scores):
    print(f"Temperatura {temperatura} -> Z-Score {z}")

mais_incomum = max(zip(temperaturas, z_scores), key=lambda item: abs(item[1]))

print(f"\nA leitura mais incomum é {mais_incomum[0]}, com Z-Score {mais_incomum[1]} (maior valor absoluto de Z).")
