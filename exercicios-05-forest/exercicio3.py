import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

consumo = [
    [10, 1.0], [20, 1.8], [30, 2.6],
    [40, 3.5], [50, 4.3], [60, 5.1],
    [70, 6.0], [80, 7.0], [90, 8.0],
    [100, 20.0],
]


def classificar_consumo(amostra, contaminacao):
    modelo = IsolationForest(contamination=contaminacao, random_state=42)
    modelo.fit(amostra)

    rotulos = modelo.predict(amostra)
    escores = modelo.decision_function(amostra)

    return modelo, rotulos, escores


if __name__ == "__main__":
    amostra = np.array(consumo, dtype=float)

    modelo, rotulos, escores = classificar_consumo(amostra, 1 / len(consumo))

    print("Classificação de cada registro\n")
    for valor, rotulo, escore in zip(amostra, rotulos, escores):
        situacao = "Anomalia" if rotulo == -1 else "Normal"
        print(f"Distância: {valor[0]:.0f}km, Litros: {valor[1]:.1f} - {situacao} (escore: {escore:.4f})")

    sinalizados = amostra[rotulos == -1]
    print(f"\nCombinações sinalizadas pelo modelo: {sinalizados.tolist()}")

    print(
        "\nResposta: 100km com 20 litros é a combinação incomum. O resto dos "
        "carros gasta perto de 0.1 litro por km, e esse caso gastou o dobro disso."
    )

    print(
        "\nDistância e litros precisam ser olhados juntos porque, sozinho, cada "
        "valor parece normal (100km e 20 litros não são extremos isolados). O "
        "problema só aparece quando se compara a relação entre os dois."
    )

    cores = ["red" if r == -1 else "blue" for r in rotulos]
    plt.scatter(amostra[:, 0], amostra[:, 1], c=cores)
    plt.xlabel("Distância (km)")
    plt.ylabel("Litros consumidos")
    plt.title("Consumo de combustível")
    plt.savefig("grafico_exercicio3.png")
