dados_brutos = [100, 150, 200, 250, 300, 350]


def calcular_mediana(sequencia):
    tamanho = len(sequencia)
    centro = tamanho // 2
    if tamanho % 2 == 0:
        return (sequencia[centro - 1] + sequencia[centro]) / 2
    return sequencia[centro]


def dividir_em_metades(sequencia):
    tamanho = len(sequencia)
    centro = tamanho // 2
    bloco_menor = sequencia[:centro]
    bloco_maior = sequencia[centro + 1:] if tamanho % 2 else sequencia[centro:]
    return bloco_menor, bloco_maior


total_elementos = len(dados_brutos)
bloco_menor, bloco_maior = dividir_em_metades(dados_brutos)

print(f"Quantidade de elementos: {total_elementos}")
print(f"Metade inferior: {bloco_menor}")
print(f"Metade superior: {bloco_maior}")

quartil_1 = calcular_mediana(bloco_menor)
quartil_3 = calcular_mediana(bloco_maior)
amplitude_interquartil = quartil_3 - quartil_1

print(f"Q1 (mediana da metade inferior): {quartil_1}")
print(f"Q3 (mediana da metade superior): {quartil_3}")
print(f"IQR: {amplitude_interquartil}")
