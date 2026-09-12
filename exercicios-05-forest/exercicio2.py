import numpy as np
from sklearn.ensemble import IsolationForest

latencias = [
    [35], [42], [28], [55],
    [60], [45], [50], [38],
    [65], [30], [220], [310],
]


def classificar_latencias(amostra, contaminacao):
    modelo = IsolationForest(contamination=contaminacao, random_state=42)
    modelo.fit(amostra)

    rotulos = modelo.predict(amostra)
    escores = modelo.decision_function(amostra)

    return modelo, rotulos, escores


if __name__ == "__main__":
    amostra = np.array(latencias, dtype=float)

    modelo, rotulos, escores = classificar_latencias(amostra, 2 / len(latencias))

    print("Classificação de cada medição\n")
    for valor, rotulo, escore in zip(amostra, rotulos, escores):
        situacao = "Anomalia" if rotulo == -1 else "Normal"
        print(f"Latência: {valor[0]:.0f}ms - {situacao} (escore: {escore:.4f})")

    sinalizados = amostra[rotulos == -1]

    print(f"\nValores sinalizados pelo modelo: {[int(v[0]) for v in sinalizados]}")

    print(
        "\nResposta: 220ms e 310ms foram sinalizados como anomalia, bem acima "
        "do resto que fica entre 20 e 70ms. Pode ser congestionamento na rede, "
        "uma instabilidade momentânea do provedor ou algum pico de uso na hora."
    )

    print(
        "\nDiscussão: não, latência alta não indica falha sempre. Às vezes é só "
        "um pico pontual que passa sozinho. Só vira sinal de falha de verdade "
        "se continuar alta por várias medições seguidas."
    )
