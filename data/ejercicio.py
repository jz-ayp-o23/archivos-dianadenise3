def calcular_promedio(calificaciones):
    return round(sum(calificaciones) / len(calificaciones), 1)

def procesar_calificaciones(entrada, salida):
    with open(entrada, 'r') as archivo_entrada:
        with open(salida, 'w') as archivo_salida:
            for linea in archivo_entrada:
                datos = linea.split()
                nombre = datos[0]
                apellido = datos[1]
                calificaciones = list(map(float, datos[2:]))
                promedio = calcular_promedio(calificaciones)

                formato_salida = f"{apellido.upper()}, {nombre}: {promedio}\n"
                archivo_salida.write(formato_salida)

# Llamada a la función para procesar calificaciones y generar el archivo
procesar_calificaciones('data/calificaciones.txt', 'data/promedios.txt')
