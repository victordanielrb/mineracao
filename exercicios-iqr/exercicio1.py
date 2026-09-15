import numpy as np

dados = [12, 15, 14, 13, 16, 12, 14, 150, 13, 15]

q1 = np.percentile(dados, 25)
q2 = np.percentile(dados, 50)
q3 = np.percentile(dados, 75)

print(f"Q1: {q1}")
print(f"Q2 (mediana): {q2}")
print(f"Q3: {q3}")
