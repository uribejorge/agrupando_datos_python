import pandas as pd

# Crear el DataFrame con los datos de estudiantes
data = {
    'Nombre': ['Ana', 'Juan', 'Pedro', 'Sofía', 'Carlos', 'María', 'Luis'],
    'Edad': [18, 19, 18, 17, 20, 18, 19],
    'Género': ['Mujer', 'Hombre', 'Hombre', 'Mujer', 'Hombre', 'Mujer', 'Hombre'],
    'Calificación': [8.5, 7.0, 9.2, 9.8, 6.5, 8.0, 7.8]
}

df = pd.DataFrame(data)

# Agrupar por Género
grupo_genero = df.groupby('Género')

# Resumen de Edad: Calcular la edad promedio por género
edad_promedio = grupo_genero['Edad'].mean()

# Resumen de Calificaciones: Calcular calificación promedio y calificación máxima por género
calificacion_promedio = grupo_genero['Calificación'].mean()
calificacion_maxima = grupo_genero['Calificación'].max()

# Crear la tabla de resumen
resumen = pd.DataFrame({
    'Edad Promedio': edad_promedio,
    'Calificación Promedio': calificacion_promedio,
    'Calificación Máxima': calificacion_maxima
})

print("Tabla de Resumen:")
print(resumen)

# Calcular la cantidad de estudiantes por género
cantidad_estudiantes = grupo_genero.size()
print("\nCantidad de Estudiantes por Género:")
print(cantidad_estudiantes)

# Ordenar la tabla de resumen por la calificación promedio de forma descendente
resumen_ordenado = resumen.sort_values(by='Calificación Promedio', ascending=False)
print("\nTabla de Resumen Ordenada por Calificación Promedio:")
print(resumen_ordenado)

# Agregar una nueva columna con la categoría de edad ("Joven" o "Adulto")
df['Categoría Edad'] = df['Edad'].apply(lambda x: 'Joven' if x < 19 else 'Adulto')
print("\nDataFrame con Categoría de Edad:")
print(df)
