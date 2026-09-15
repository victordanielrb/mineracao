import pandas as pd

dados = {
    "Evento": ["A", "B", "C", "D", "E", "F", "G"],
    "Tentativas_Login": [3, 4, 2, 5, 3, 4, 40],
}

df = pd.DataFrame(dados)

media = df["Tentativas_Login"].mean()
desvio = df["Tentativas_Login"].std()

df["Z_Score"] = (df["Tentativas_Login"] - media) / desvio

investigar = df[df["Z_Score"].abs() > 3]

print("DataFrame completo:")
print(df)

print("\nEventos com |Z| > 3:")
print(investigar)

print("\nUm evento incomum em segurança pode ser justamente o dado mais importante da análise, "
      "pois pode indicar uma tentativa de invasão em vez de um erro de medição.")
