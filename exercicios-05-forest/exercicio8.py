import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

dados = pd.read_csv("vendas_ecommerce.csv")
print(dados.head())

caracteristicas = dados[["valor_total", "quantidade_itens", "desconto_percentual"]]

modelo = IsolationForest(contamination=2 / len(dados), random_state=42)
dados["rotulo"] = modelo.fit_predict(caracteristicas)

candidatas = dados[dados["rotulo"] == -1]
print("\nVendas candidatas:")
print(candidatas)

print(
    "\nResposta: a venda 11 chama atenção por ter um valor bem alto (2000) com "
    "só 1 item e sem desconto -- pode ser a compra de um produto caro mesmo, "
    "tipo um eletrônico. Já a venda 12 tem 90% de desconto, o que é raro e pode "
    "ser erro de cadastro ou uma promoção agressiva demais."
)

cores = ["red" if r == -1 else "blue" for r in dados["rotulo"]]
plt.scatter(dados["valor_total"], dados["desconto_percentual"], c=cores)
plt.xlabel("Valor total")
plt.ylabel("Desconto (%)")
plt.title("Vendas de e-commerce")
plt.savefig("grafico_exercicio8.png")
