from pathlib import Path
from string import ascii_lowercase as LETRAS


def encriptar(cadena, desplazamiento):
    """
    Encriptar una cadena aplicando el desplazamiento indicado. 
    Solo se encriptan las letras, los números y los signos de puntuación se dejan sin afectar.
    """
    salida = ""
    for letra in cadena.lower():
        pos = LETRAS.find(letra)
        if pos > -1:
            pos = (pos + desplazamiento) % len(LETRAS)
            letra = LETRAS[pos]
        salida += letra
    return salida


def desencriptar(cadena, desplazamiento):
    return encriptar(cadena, -desplazamiento)


def desencriptar_archivo(entrada, desplazamiento):
    archivo = Path(entrada)
    salida = str(archivo.with_name(archivo.stem + "-DESEN" + archivo.suffix))
    with open(archivo, "r", encoding="utf8") as f_in:
        with open(salida, "w", encoding="utf8") as f_out:
            for linea in f_in:
                f_out.write(desencriptar(linea, desplazamiento))

desplazamiento=2
desencriptar_archivo('data/Asimov, Isaac - Cómo ocurrió-CRIPTO.txt', desplazamiento)
