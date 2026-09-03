import pandas as pd

registro = {
    'ID_Maquina': [1, 2, 3, 4, 5],
    'Uso_Memoria_MB': [2048, 2100, 2050, 8192, 2080]
}

tabela = pd.DataFrame(registro)

quartil_1 = tabela['Uso_Memoria_MB'].quantile(0.25)
quartil_3 = tabela['Uso_Memoria_MB'].quantile(0.75)
amplitude = quartil_3 - quartil_1
piso = quartil_1 - 1.5 * amplitude
teto = quartil_3 + 1.5 * amplitude

mascara_outlier = (tabela['Uso_Memoria_MB'] < piso) | (tabela['Uso_Memoria_MB'] > teto)
maquinas_suspeitas = tabela[mascara_outlier]

print(f"Q1: {quartil_1}")
print(f"Q3: {quartil_3}")
print(f"IQR: {amplitude}")
print(f"Limite Inferior: {piso}")
print(f"Limite Superior: {teto}")
print("\nCandidatos a outlier:")
print(maquinas_suspeitas)
