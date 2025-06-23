"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open("files/input/data.csv", encoding="utf-8") as f:
        x = [line.strip().split('\t') for line in f]

    x = [(fila[0], int(fila[1])) for fila in x]
    max_min = {}

    for letra, valor in x:
        valor = int(valor)
        if letra in max_min:
            max_min[letra].append(valor)
        else:
            max_min[letra] = [valor]
    resultado = [(letra, max(valores), min(valores)) for letra, valores in max_min.items()]
    return sorted(resultado)