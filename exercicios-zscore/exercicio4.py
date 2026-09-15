import numpy as np

latencias = [98, 102, 101, 99, 100, 103, 97, 180]

media = np.mean(latencias)
desvio = np.std(latencias)

z = (180 - media) / desvio

print(f"Média: {media}")
print(f"Desvio-padrão: {desvio}")
print(f"Z-Score da latência 180 ms: {z}")

if abs(z) > 3:
    print("Essa latência merece investigação (|Z| > 3).")
else:
    print("Essa latência não ultrapassa o limite prático de |Z| > 3.")

print("Investigar não significa apagar o dado automaticamente.")
