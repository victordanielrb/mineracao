import pandas as pd

registro = {
    'Pedido': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'Valor': [100, 120, 110, 130, 125, 115, 140, 1000]
}

tabela = pd.DataFrame(registro)

quartil_1 = tabela['Valor'].quantile(0.25)
quartil_3 = tabela['Valor'].quantile(0.75)
amplitude = quartil_3 - quartil_1
piso = quartil_1 - 1.5 * amplitude
teto = quartil_3 + 1.5 * amplitude

tabela['Outlier'] = ~tabela['Valor'].between(piso, teto)

print(f"Q1: {quartil_1}, Q3: {quartil_3}, IQR: {amplitude}")
print(f"Limite Inferior: {piso}, Limite Superior: {teto}")

print("\nDataFrame completo:")
print(tabela)

print("\nApenas outliers (Outlier == True):")
print(tabela[tabela['Outlier']])
