media_a = 100
desvio_a = 2

media_b = 100
desvio_b = 20

valor = 110

z_a = (valor - media_a) / desvio_a
z_b = (valor - media_b) / desvio_b

print(f"Z-Score no Grupo A: {z_a}")
print(f"Z-Score no Grupo B: {z_b}")

print("\nA mesma distância absoluta de 10 unidades gera um Z-Score alto no Grupo A porque o desvio-padrão é pequeno, "
      "tornando o valor incomum. No Grupo B, o desvio-padrão é grande, então a mesma distância é comum e não chama atenção.")
