import numpy as np

dados = [10, 11, 12, 12, 13, 13, 14, 15, 30]

q1 = np.percentile(dados, 25)
q3 = np.percentile(dados, 75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

media = np.mean(dados)
desvio = np.std(dados)
z_30 = (30 - media) / desvio

print(f"Q1: {q1}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Limite inferior: {limite_inferior}")
print(f"Limite superior: {limite_superior}")
print(f"Média: {media}")
print(f"Desvio-padrão: {desvio}")
print(f"Z-Score do valor 30: {z_30}")

print("\nO IQR aponta o 30 como outlier por estar fora do limite superior, mas o Z-Score não ultrapassa a regra "
      "prática de |Z| > 3. Técnicas diferentes podem analisar o mesmo dado por critérios diferentes e chegar "
      "a conclusões distintas sobre o que merece investigação.")
