import numpy as np


def identificar_valores_atipicos(amostra, fator_k):
    quartil_1 = np.percentile(amostra, 25)
    quartil_3 = np.percentile(amostra, 75)
    amplitude = quartil_3 - quartil_1
    piso = quartil_1 - fator_k * amplitude
    teto = quartil_3 + fator_k * amplitude
    suspeitos = [valor for valor in amostra if valor < piso or valor > teto]
    return quartil_1, quartil_3, amplitude, piso, teto, suspeitos


medicoes = [45, 50, 55, 60, 48, 52, 51, 98, 49, 53]
fator_k = 1.5

quartil_1, quartil_3, amplitude, piso, teto, suspeitos = identificar_valores_atipicos(
    medicoes, fator_k
)

print(f"Dados originais: {medicoes}")
print(f"Q1: {quartil_1}")
print(f"Q3: {quartil_3}")
print(f"IQR: {amplitude}")
print(f"Limite Inferior: {piso}")
print(f"Limite Superior: {teto}")
print(f"Candidatos a outlier: {suspeitos}")

print("\nInterpretação:")
for valor in suspeitos:
    lado = "superior" if valor > teto else "inferior"
    limite_atingido = teto if valor > teto else piso
    print(f"O valor {valor} ultrapassou o limite {lado} {limite_atingido}.")
    print(f"Portanto, {valor} é candidato a outlier pela Regra do IQR.")
