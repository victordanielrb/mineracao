import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

acessos_por_hora = [
    [120], [135], [128], [140], [132],
    [125], [138], [130], [142], [127],
    [133], [129], [136], [5], [850],
]


def classificar_acessos(amostra, contaminacao):
    modelo = IsolationForest(contamination=contaminacao, random_state=42)
    modelo.fit(amostra)

    rotulos = modelo.predict(amostra)
    escores = modelo.decision_function(amostra)

    return modelo, rotulos, escores


if __name__ == "__main__":
    amostra = np.array(acessos_por_hora, dtype=float)

    modelo, rotulos, escores = classificar_acessos(amostra, 2 / len(acessos_por_hora))

    print("Classificação de cada hora\n")
    for hora, (valor, rotulo, escore) in enumerate(zip(amostra, rotulos, escores)):
        situacao = "Anomalia" if rotulo == -1 else "Normal"
        print(f"Hora {hora}: {valor[0]:.0f} acessos - {situacao} (escore: {escore:.4f})")

    sinalizados = amostra[rotulos == -1]
    print(f"\nHoras sinalizadas pelo modelo: {[int(v[0]) for v in sinalizados]}")

    print(
        "\nOs 5 acessos numa hora provavelmente é o site fora do ar ou algum "
        "problema no servidor, já que todo o resto fica sempre acima de 100. "
        "Já os 850 acessos parecem um pico de tráfego, tipo um post que viralizou "
        "ou um ataque de bots -- precisaria olhar os logs pra confirmar."
    )

    print(
        "\nDiscussão: o critério usado foi o quanto cada valor se destaca do "
        "grupo. O Isolation Forest separa mais rápido os pontos que ficam longe "
        "da maioria, e foi isso que definiu quem virou candidato."
    )

    cores = ["red" if r == -1 else "blue" for r in rotulos]
    plt.scatter(range(len(amostra)), amostra[:, 0], c=cores)
    plt.xlabel("Hora")
    plt.ylabel("Acessos")
    plt.title("Acessos a um site por hora")
    plt.savefig("grafico_exercicio6.png")
