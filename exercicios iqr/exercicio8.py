import pandas as pd

dados = {
    "Pedido": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Valor": [100, 120, 110, 130, 125, 115, 140, 1000],
}

df = pd.DataFrame(dados)

q1 = df["Valor"].quantile(0.25)
q3 = df["Valor"].quantile(0.75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

df["Outlier"] = (df["Valor"] < limite_inferior) | (df["Valor"] > limite_superior)

print("DataFrame completo:")
print(df)

print("\nApenas os outliers:")
print(df[df["Outlier"]])
