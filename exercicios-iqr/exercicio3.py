dados = [100, 150, 200, 250, 300, 350]


def mediana(valores):
    n = len(valores)
    meio = n // 2
    if n % 2 == 0:
        return (valores[meio - 1] + valores[meio]) / 2
    else:
        return valores[meio]


n = len(dados)
meio = n // 2

if n % 2 == 0:
    metade_inferior = dados[:meio]
    metade_superior = dados[meio:]
else:
    metade_inferior = dados[:meio]
    metade_superior = dados[meio + 1:]

print(f"Metade inferior: {metade_inferior}")
print(f"Metade superior: {metade_superior}")

q1 = mediana(metade_inferior)
q3 = mediana(metade_superior)
iqr = q3 - q1

print(f"\nQ1: {q1}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
