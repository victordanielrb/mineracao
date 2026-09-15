from exercicio5 import detectar_anomalias

dados = [45, 50, 55, 60, 48, 52, 51, 98, 49, 53]
multiplicador = 1.5

q1, q3, iqr, limite_inferior, limite_superior, candidatos = detectar_anomalias(dados, multiplicador)

print(f"Dados originais: {dados}")
print(f"Q1: {q1}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Limite inferior: {limite_inferior}")
print(f"Limite superior: {limite_superior}")
print(f"Candidatos a outlier: {candidatos}")

print()
for valor in candidatos:
    if valor > limite_superior:
        print(f"O valor {valor} ultrapassou o limite superior {limite_superior}.")
    else:
        print(f"O valor {valor} ficou abaixo do limite inferior {limite_inferior}.")
    print(f"Portanto, {valor} é candidato a outlier pela Regra do IQR.")
