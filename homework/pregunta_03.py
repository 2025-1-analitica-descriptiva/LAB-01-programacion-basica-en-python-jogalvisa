"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    data = {}
    with open("files/input/data.csv", "r") as f:
        for line in f:
            columnas = line.strip().split("\t")
            if columnas:
                letra = columnas[0]
                x= int(columnas[1])
                data[letra] = data.get(letra, 0) + x
                suma_letra = sorted(data.items())
    return suma_letra

