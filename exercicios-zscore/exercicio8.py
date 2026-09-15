import numpy as np
import pandas as pd

dados = {
    "Usuario": ["ana", "bruno", "carla", "diego", "eva", "fabio"],
    "Requisicoes": [120, 135, 128, 122, 130, 400],
}

df = pd.DataFrame(dados)

media = df["Requisicoes"].mean()
desvio = df["Requisicoes"].std()

df["Z_Score"] = (df["Requisicoes"] - media) / desvio
df["Status"] = np.where(df["Z_Score"].abs() > 3, "Investigar", "Comum")

print("DataFrame completo:")
print(df)

print("\nApenas as linhas marcadas para investigação:")
print(df[df["Status"] == "Investigar"])
