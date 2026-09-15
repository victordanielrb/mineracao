def interpretar_z(z):
    if abs(z) > 3:
        return "Investigar"
    if z < 0:
        return "Abaixo da média"
    if z > 0:
        return "Acima da média"
    return "Na média"


valores_z = [-3.5, -1.2, 0, 0.8, 3.7]

for z in valores_z:
    print(f"{z} -> {interpretar_z(z)}")
