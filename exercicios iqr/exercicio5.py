import numpy as np


def detectar_anomalias(dados, multiplicador):
    q1 = np.percentile(dados, 25)
    q3 = np.percentile(dados, 75)
    iqr = q3 - q1
    limite_inferior = q1 - multiplicador * iqr
    limite_superior = q3 + multiplicador * iqr

    candidatos = [valor for valor in dados if valor < limite_inferior or valor > limite_superior]

    return q1, q3, iqr, limite_inferior, limite_superior, candidatos
