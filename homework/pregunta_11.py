"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    with open("files/input/data.csv", encoding="utf-8") as f:
        x = [line.strip().split('\t') for line in f]

    suma_por_letra = {}

    for fila in x:
        numero = int(fila[1])
        letras = fila[3].split(",")

        for letra in letras:
            if letra in suma_por_letra:
                suma_por_letra[letra] += numero
            else:
                suma_por_letra[letra] = numero
    return dict(sorted(suma_por_letra.items()))
