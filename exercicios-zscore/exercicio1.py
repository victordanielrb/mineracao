media = 100
desvio = 5
valor = 115

distancia = valor - media
n_desvios = distancia / desvio
z = (valor - media) / desvio

print(f"Distância até a média: {distancia}")
print(f"Número de desvios-padrão: {n_desvios}")
print(f"Z-Score: {z}")
print(f"O valor {valor} está {z} desvios-padrão acima da média.")
