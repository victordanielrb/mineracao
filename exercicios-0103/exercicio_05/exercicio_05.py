import numpy as np


def identificar_valores_atipicos(amostra, fator_k):
    quartil_1 = np.percentile(amostra, 25)
    quartil_3 = np.percentile(amostra, 75)
    amplitude = quartil_3 - quartil_1
    piso = quartil_1 - fator_k * amplitude
    teto = quartil_3 + fator_k * amplitude

    suspeitos = []
    for valor in amostra:
        if valor < piso or valor > teto:
            suspeitos.append(valor)

    return quartil_1, quartil_3, amplitude, piso, teto, suspeitos


if __name__ == "__main__":
    amostra = [12, 15, 14, 13, 16, 12, 14, 150, 13, 15]
    resultado = identificar_valores_atipicos(amostra, 1.5)
    print(resultado)
