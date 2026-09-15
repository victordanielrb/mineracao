import numpy as np
import pandas as pd

temperaturas = [80, 82, 85, 81, 300, 83]

df = pd.DataFrame({"Temperatura": temperaturas})

q1 = df["Temperatura"].quantile(0.25)
q3 = df["Temperatura"].quantile(0.75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

fora_do_limite = df[(df["Temperatura"] < limite_inferior) | (df["Temperatura"] > limite_superior)]
print(f"Valor fora dos limites: {fora_do_limite['Temperatura'].tolist()}")

mediana = df["Temperatura"].median()

print("\nAntes da correção:")
print(df)

df["Temperatura"] = np.where(
    (df["Temperatura"] < limite_inferior) | (df["Temperatura"] > limite_superior),
    mediana,
    df["Temperatura"],
)

print("\nDepois da correção:")
print(df)
