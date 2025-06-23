"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open("files/input/data.csv", encoding="utf-8") as f:
        x = [line.strip().split('\t') for line in f]

    suma_por_letra = {}

    for fila in x:
        letra = fila[0]
        columna_5 = fila[4]

        valores = [int(par.split(":")[1]) for par in columna_5.split(",")]

        if letra in suma_por_letra:
            suma_por_letra[letra] += sum(valores)
        else:
            suma_por_letra[letra] = sum(valores)

    return suma_por_letra 
