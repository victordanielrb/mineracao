casos = [85, 100, 120]
media = 100
desvio = 10

for valor in casos:
    z = (valor - media) / desvio

    if z < 0:
        posicao = "abaixo da média"
    elif z > 0:
        posicao = "acima da média"
    else:
        posicao = "exatamente na média"

    print(f"Valor {valor} -> Z-Score {z} -> está {posicao}")

print("\nSinal negativo indica valor abaixo da média, sinal positivo indica valor acima da média e zero indica valor igual à média.")
