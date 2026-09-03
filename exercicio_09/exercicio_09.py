import pandas as pd

leituras_sensor = [80, 82, 85, 81, 300, 83]

tabela = pd.DataFrame({'Temperatura': leituras_sensor})

quartil_1 = tabela['Temperatura'].quantile(0.25)
quartil_3 = tabela['Temperatura'].quantile(0.75)
amplitude = quartil_3 - quartil_1
piso = quartil_1 - 1.5 * amplitude
teto = quartil_3 + 1.5 * amplitude

print("DataFrame antes da correção:")
print(tabela)
print(f"\nQ1: {quartil_1}, Q3: {quartil_3}, IQR: {amplitude}")
print(f"Limite Inferior: {piso}, Limite Superior: {teto}")

fora_da_faixa = ~tabela['Temperatura'].between(piso, teto)
leituras_suspeitas = tabela[fora_da_faixa]
print(f"\nValor(es) fora dos limites (erro confirmado do sensor):\n{leituras_suspeitas}")

valor_central = tabela['Temperatura'].median()
print(f"\nMediana do conjunto: {valor_central}")

tabela['Temperatura'] = tabela['Temperatura'].where(~fora_da_faixa, valor_central)

print("\nDataFrame depois da correção:")
print(tabela)
