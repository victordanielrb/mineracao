import numpy as np

leituras_tensao = [110, 115, 120, 118, 112, 220, 116, 114, 119, 12]

quartil_1 = np.percentile(leituras_tensao, 25)
quartil_3 = np.percentile(leituras_tensao, 75)
amplitude = quartil_3 - quartil_1
piso = quartil_1 - 1.5 * amplitude
teto = quartil_3 + 1.5 * amplitude


def fora_da_faixa(valor):
    return valor < piso or valor > teto


leituras_suspeitas = [tensao for tensao in leituras_tensao if fora_da_faixa(tensao)]

print(f"Q1: {quartil_1}")
print(f"Q3: {quartil_3}")
print(f"IQR: {amplitude}")
print(f"Limite Inferior: {piso}")
print(f"Limite Superior: {teto}")
print(f"Candidatos a outlier: {leituras_suspeitas}")
