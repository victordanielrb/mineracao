import numpy as np

tensoes = [110, 115, 120, 118, 112, 220, 116, 114, 119, 12]

q1 = np.percentile(tensoes, 25)
q3 = np.percentile(tensoes, 75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

candidatos = []
for valor in tensoes:
    if valor < limite_inferior or valor > limite_superior:
        candidatos.append(valor)

print(f"Q1: {q1}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Limite inferior: {limite_inferior}")
print(f"Limite superior: {limite_superior}")
print(f"Candidatos a outlier: {candidatos}")
