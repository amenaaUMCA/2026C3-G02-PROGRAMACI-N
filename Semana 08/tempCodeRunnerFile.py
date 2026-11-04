#FASE 1 : COTAR MEDICAMENTOS
conteo_medicamento = {}
conteo_recetas = 0

for registro in registros:
    for medicamento in registro['medicamentos']:
        if medicamento in conteo_medicamento:
            conteo_medicamento[medicamento] += 1
        else:
            conteo_medicamento[medicamento] = 1
        conteo_recetas += 1

print("\n CONTEO DE MEDICAMENTOS")
print("Total de recetas:", conteo_recetas)
print(conteo_medicamento)