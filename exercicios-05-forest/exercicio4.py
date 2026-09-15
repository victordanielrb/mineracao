import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

viagens = [
    [32, 3], [45, 5], [50, 4],
    [60, 6], [55, 5], [70, 7],
    [65, 6], [80, 8], [75, 7],
    [10, 45],
]


def classificar_viagens(amostra, contaminacao):
    modelo = IsolationForest(contamination=contaminacao, random_state=42)
    modelo.fit(amostra)

    rotulos = modelo.predict(amostra)
    escores = modelo.decision_function(amostra)

    return modelo, rotulos, escores


if __name__ == "__main__":
    amostra = np.array(viagens, dtype=float)

    modelo, rotulos, escores = classificar_viagens(amostra, 1 / len(viagens))

    print("Classificação de cada viagem\n")
    for valor, rotulo, escore in zip(amostra, rotulos, escores):
        situacao = "Anomalia" if rotulo == -1 else "Normal"
        print(f"Passageiros: {valor[0]:.0f}, Atraso: {valor[1]:.0f}min - {situacao} (escore: {escore:.4f})")

    sinalizados = amostra[rotulos == -1]
    print(f"\nViagens sinalizadas pelo modelo: {sinalizados.tolist()}")

    print(
        "\nResposta: a viagem com 10 passageiros e 45 minutos de atraso é a "
        "candidata. Nas outras, o atraso cresce um pouco conforme mais gente "
        "embarca, mas essa teve poucos passageiros e um atraso enorme, o que "
        "não segue o padrão."
    )

    print(
        "\nPossíveis causas: congestionamento no trajeto, um acidente no "
        "caminho ou uma falha mecânica no ônibus que forçou uma parada."
    )

    cores = ["red" if r == -1 else "blue" for r in rotulos]
    plt.scatter(amostra[:, 0], amostra[:, 1], c=cores)
    plt.xlabel("Passageiros")
    plt.ylabel("Atraso (min)")
    plt.title("Viagens de ônibus urbano")
    plt.savefig("grafico_exercicio4.png")
