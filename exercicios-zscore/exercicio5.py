import numpy as np

cpu = [42, 45, 47, 44, 46, 43, 48, 92]

media = np.mean(cpu)
desvio = np.std(cpu)

for leitura in cpu:
    z = (leitura - media) / desvio
    classificacao = "Investigar" if abs(z) > 3 else "Comum"
    print(f"{leitura} -> {z} -> {classificacao}")
