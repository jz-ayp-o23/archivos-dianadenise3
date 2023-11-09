
"""Diana Denise Valdivia Vargas
9 de Noviembre del 2023
Otorgar a calificaciones.txt el formato de el apellido del alumno en mayúsculas, separado por una coma de su nombre, dos puntos y
, enseguida, el promedio de las calificaciones a un decimal."""

from decimal import Decimal, ROUND_HALF_UP

def procesar_calificaciones(entrada, salida):
    with open(entrada, 'r') as archivo_entrada: #Abre el archivo de entrada en modo lectura, la funcion "as archivo_entrada" es una asignación de nombre
        with open(salida, 'w') as archivo_salida: #Abre el archivo de salida en modo escritura, "as archivo_salida" es una asignación de nombre
            
            # Cuando usas un bucle for con un archivo, cada iteración del bucle obtiene la siguiente línea del archivo hasta que se alcanza el final del archivo.
            #[Sin embargo, si en algún momento necesitas trabajar a nivel de caracteres, puedes hacerlo leyendo la línea y luego iterando sobre los caracteres de esa línea.]
            for linea in archivo_entrada: 
                #divide una cadena en una lista de subcadenas basadas en un separador(es decir las regresa como una lista)
                datos_separados = linea.split() 
                #Slicing de los datos 
                nombre = datos_separados[0]
                apellido = datos_separados[1]
                #Crea una lista (califiaciones) extrae las calificaciones (de la lisa datos_separados) y los hace decimales exactos (librería decimal)
                calificaciones = [Decimal(calif) for calif in datos_separados[2:]] 
                promedio = (sum(calificaciones) / Decimal(len(calificaciones))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP) 
                #Quantize: para redondear el resultado a una décima.
                #Decimal('0.1'): Establece la escala de cuantificación en una décima, especificando que se desea redondear a la posición del primer dígito decimal.
                #rounding=ROUND_HALF_UP: Indica que se debe redondear hacia arriba si la parte decimal es igual o mayor a 0.5
                formato_salida = f"{apellido.upper()}, {nombre}: {promedio}\n"
                #La función write escribe esta cadena en el archivo, agregándola al final del archivo de salida (en este caso es el de promedios.txt)
                archivo_salida.write(formato_salida)

# El prefijo "data/" indica que el archivo calificaciones.txt se encuentra dentro de un directorio llamado data.
# Procesar_calificaiones: Aquí es donde se llama a la función procesar_calificaciones y se le pasa la ruta del archivo de entrada ('data/calificaciones.txt')- 
#-y la ruta del archivo de salida ('data/promedios.txt'). Esta llamada es lo que desencadena la lectura del archivo de calificaciones- 
#-y el procesamiento de la información para calcular los promedios y escribirlos en un nuevo archivo.

procesar_calificaciones('data/calificaciones.txt', 'data/promedios.txt') 