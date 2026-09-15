import numpy as np

amostra = [12, 15, 14, 13, 16, 12, 14, 150, 13, 15]


def calcular_limites_iqr(valores, k=1.5):
    quartil_1 = np.percentile(valores, 25)
    quartil_3 = np.percentile(valores, 75)
    amplitude = quartil_3 - quartil_1
    margem = k * amplitude
    piso = quartil_1 - margem
    teto = quartil_3 + margem
    return quartil_1, quartil_3, amplitude, margem, piso, teto


quartil_1, quartil_3, amplitude, margem, piso, teto = calcular_limites_iqr(amostra)

relatorio = {
    "Q1": quartil_1,
    "Q3": quartil_3,
    "IQR": amplitude,
    "1.5 x IQR": margem,
    "Limite Inferior": piso,
    "Limite Superior": teto,
}
for rotulo, resultado in relatorio.items():
    print(f"{rotulo}: {resultado}")

candidato = 150
dentro_da_faixa = piso <= candidato <= teto
if dentro_da_faixa:
    print(f"O valor {candidato} está dentro dos limites e não é candidato a outlier.")
else:
    print(f"O valor {candidato} ultrapassa os limites e é candidato a outlier.")
