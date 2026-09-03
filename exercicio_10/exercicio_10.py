import numpy as np

turma_x = [48, 49, 50, 50, 51, 52, 52, 53]
turma_y = [20, 30, 40, 50, 60, 70, 80, 90]


def resumir_dispersao(identificador, valores):
    quartil_1 = np.percentile(valores, 25)
    quartil_3 = np.percentile(valores, 75)
    amplitude = quartil_3 - quartil_1
    print(f"{identificador}: Q1={quartil_1}, Q3={quartil_3}, IQR={amplitude}")
    return amplitude


amplitude_x = resumir_dispersao("Grupo A", turma_x)
amplitude_y = resumir_dispersao("Grupo B", turma_y)

print()
if amplitude_x > amplitude_y:
    print("O grupo A possui o maior IQR.")
elif amplitude_y > amplitude_x:
    print("O grupo B possui o maior IQR.")
else:
    print("Os dois grupos possuem o mesmo IQR.")

print("Os 50% centrais do Grupo B estão mais espalhados (maior IQR).")
print(
    "Um IQR maior não significa que os dados estão errados: ele apenas indica maior "
    "dispersão natural entre os valores centrais. Dispersão não é sinônimo de erro; "
    "cada conjunto pode refletir corretamente um fenômeno com variabilidade diferente."
)
