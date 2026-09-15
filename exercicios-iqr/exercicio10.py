import numpy as np

grupo_a = [48, 49, 50, 50, 51, 52, 52, 53]
grupo_b = [20, 30, 40, 50, 60, 70, 80, 90]


def calcular_iqr(dados):
    q1 = np.percentile(dados, 25)
    q3 = np.percentile(dados, 75)
    iqr = q3 - q1
    return q1, q3, iqr


q1_a, q3_a, iqr_a = calcular_iqr(grupo_a)
q1_b, q3_b, iqr_b = calcular_iqr(grupo_b)

print(f"Grupo A - Q1: {q1_a}, Q3: {q3_a}, IQR: {iqr_a}")
print(f"Grupo B - Q1: {q1_b}, Q3: {q3_b}, IQR: {iqr_b}")

print(
    "\nO grupo B tem o maior IQR, então os 50% centrais dele estão mais "
    "espalhados que os do grupo A."
)

print(
    "\nUm IQR maior não quer dizer que os dados estão errados. Ele só mostra "
    "que os valores centrais variam mais. O grupo B pode ser assim naturalmente, "
    "por exemplo medindo algo com mais variação real."
)
