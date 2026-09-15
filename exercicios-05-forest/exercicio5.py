import numpy as np
from sklearn.ensemble import IsolationForest

consumo_agua = [
    [48], [52], [50], [55],
    [49], [53], [51], [54],
    [56], [12], [180],
]


def regra_fixa(amostra, minimo=20, maximo=100):
    return [valor[0] for valor in amostra if valor[0] < minimo or valor[0] > maximo]


def classificar_consumo(amostra, contaminacao):
    modelo = IsolationForest(contamination=contaminacao, random_state=42)
    modelo.fit(amostra)
    return modelo.predict(amostra)


if __name__ == "__main__":
    amostra = np.array(consumo_agua, dtype=float)

    candidatos_regra = regra_fixa(amostra)
    print(f"Regra fixa (fora de 20-100 litros) sinalizou: {candidatos_regra}")

    rotulos = classificar_consumo(amostra, 2 / len(consumo_agua))
    candidatos_modelo = [valor[0] for valor, rotulo in zip(amostra, rotulos) if rotulo == -1]
    print(f"Isolation Forest sinalizou: {candidatos_modelo}")

    if sorted(candidatos_regra) == sorted(candidatos_modelo):
        print("\nOs dois métodos encontraram os mesmos candidatos.")
    else:
        print("\nOs métodos encontraram candidatos diferentes.")

    print(
        "\nA regra fixa só funciona bem porque a gente já sabia mais ou menos "
        "qual era a faixa normal de consumo. Se o padrão mudar (por exemplo, uma "
        "casa que gasta mais água no verão), o limite de 20-100 pode ficar "
        "errado e é preciso ajustar na mão."
    )

    print(
        "\nO Isolation Forest não precisa de um limite definido antes, ele "
        "aprende sozinho o que é normal olhando os dados. Isso ajuda quando "
        "não se sabe qual faixa usar ou quando o padrão pode mudar com o tempo."
    )

    print(
        "\nDiscussão: para esse caso, com um padrão claro e conhecido, a regra "
        "fixa já resolve e é mais simples de explicar. O Isolation Forest vale "
        "mais quando não dá pra saber de antemão qual é o limite certo."
    )
