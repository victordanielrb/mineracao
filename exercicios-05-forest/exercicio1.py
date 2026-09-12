import numpy as np
from sklearn.ensemble import IsolationForest

vendas = [
    [80], [85], [90], [88],
    [92], [87], [95], [89],
    [91], [400],
]


def classificar_vendas(amostra, contaminacao):
    modelo = IsolationForest(contamination=contaminacao, random_state=42)
    modelo.fit(amostra)

    rotulos = modelo.predict(amostra)
    escores = modelo.decision_function(amostra)

    return modelo, rotulos, escores


if __name__ == "__main__":
    amostra = np.array(vendas, dtype=float)

    modelo, rotulos, escores = classificar_vendas(amostra, 0.1)

    print("Classificação de cada venda\n")
    for valor, rotulo, escore in zip(amostra, rotulos, escores):
        situacao = "Anomalia" if rotulo == -1 else "Normal"
        print(f"Venda: {valor[0]:.0f} - {situacao} (escore: {escore:.4f})")

    sinalizados = amostra[rotulos == -1]

    print(f"\nValores sinalizados pelo modelo: {[int(v[0]) for v in sinalizados]}")

    print(
        "\nResposta: o valor 400 foi o único sinalizado como anomalia. Uma venda "
        "muito acima do padrão pode ser uma promoção (muita gente comprando no "
        "mesmo dia), uma encomenda grande feita por um único cliente ou um erro "
        "de registro (por exemplo, digitar 400 no lugar de 40)."
    )

    print(
        "\nDiscussão: o valor 400 NÃO deve ser removido automaticamente. O "
        "Isolation Forest apenas aponta o candidato, sem saber o motivo. Como o "
        "modelo não distingue um evento legítimo de um erro, a remoção automática "
        "poderia descartar uma venda real; o correto é investigar o contexto antes "
        "de decidir."
    )
