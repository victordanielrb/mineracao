import numpy as np
import matplotlib.pyplot as plt

tempos = [20, 21, 22, 23, 24, 25, 26, 80]

q1 = np.percentile(tempos, 25)
q3 = np.percentile(tempos, 75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

candidatos = [valor for valor in tempos if valor < limite_inferior or valor > limite_superior]

print(f"Q1: {q1}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Limite inferior: {limite_inferior}")
print(f"Limite superior: {limite_superior}")
print(f"Candidatos a outlier: {candidatos}")

print(
    "\nResposta: sim, o ponto destacado no boxplot é o 80, que é exatamente o "
    "mesmo valor encontrado pela Regra do IQR."
)

plt.boxplot(tempos)
plt.title("Boxplot dos tempos")
plt.savefig("boxplot_tempos.png")
