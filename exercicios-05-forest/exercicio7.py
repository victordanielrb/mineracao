import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

dados = pd.read_csv("sensores_ambientais.csv")
print(dados.head())

caracteristicas = dados[["temperatura", "umidade"]]

modelo = IsolationForest(contamination=1 / len(dados), random_state=42)
dados["rotulo"] = modelo.fit_predict(caracteristicas)

candidatas = dados[dados["rotulo"] == -1]
print("\nLeituras candidatas:")
print(candidatas[["ambiente", "temperatura", "umidade"]])

print(
    "\nResposta: a Sala 10 é a leitura incomum, com 35°C e só 12% de umidade, "
    "bem diferente das outras salas que ficam perto de 22-25°C e 44-50% de "
    "umidade. Pode ser um sensor com defeito ou uma sala perto de alguma fonte "
    "de calor."
)

cores = ["red" if r == -1 else "blue" for r in dados["rotulo"]]
plt.scatter(dados["temperatura"], dados["umidade"], c=cores)
plt.xlabel("Temperatura (°C)")
plt.ylabel("Umidade (%)")
plt.title("Sensores ambientais")
plt.savefig("grafico_exercicio7.png")
