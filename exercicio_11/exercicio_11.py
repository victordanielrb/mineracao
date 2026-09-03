import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))

duracoes = [20, 21, 22, 23, 24, 25, 26, 80]

quartil_1 = np.percentile(duracoes, 25)
quartil_3 = np.percentile(duracoes, 75)
amplitude = quartil_3 - quartil_1
piso = quartil_1 - 1.5 * amplitude
teto = quartil_3 + 1.5 * amplitude

suspeitos = [duracao for duracao in duracoes if duracao < piso or duracao > teto]

print(f"Q1: {quartil_1}")
print(f"Q3: {quartil_3}")
print(f"IQR: {amplitude}")
print(f"Limite Inferior: {piso}")
print(f"Limite Superior: {teto}")
print(f"Candidatos a outlier (cálculo): {suspeitos}")

plt.figure(figsize=(5, 5))
plt.boxplot(duracoes, vert=True)
plt.title("Boxplot - tempos")
plt.ylabel("Tempo")
caminho_saida = os.path.join(DIRETORIO_ATUAL, "boxplot_tempos.png")
plt.savefig(caminho_saida, dpi=150, bbox_inches="tight")
print(f"\nGráfico salvo em {caminho_saida}")

print(
    "\nResposta: sim, o valor 80, destacado visualmente no boxplot como ponto "
    "isolado acima do 'bigode' superior, coincide com o candidato a outlier "
    "identificado numericamente pela Regra do IQR."
)
