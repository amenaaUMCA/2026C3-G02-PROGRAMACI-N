import pandas as pd

datos = {
    "nombre": ['Daniel', 'Moises', 'Diana', 'Jimena', 'Emanuel'],
    "edad": [16, 14, 14, 15, 13],
    "nota": [90, 96, 85, 62, 70]
}

estudiantes = pd.DataFrame(datos) # int('18')

print(estudiantes)

print(estudiantes.info())
print("\nColumnas: ", estudiantes.columns)

print(estudiantes['nombre'])

print("\nNotas:\n",estudiantes['nota'])
print("Nota menor:", estudiantes['nota'].min())
print("Nota mayor:", estudiantes['nota'].max())
print("Promedio:", estudiantes['nota'].mean())


