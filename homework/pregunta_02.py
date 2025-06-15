"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from collections import Counter
def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    x =  open('D:\\Datos\\Documents\\CLASE ANALITICA DESCRIPTIVA\\LAB-01-programacion-basica-en-python-jogalvisa\\files\\input\\data.csv', 'r').readlines()
    x = [z.replace('\n','') for z in x]
    x = [z.split("\t") for z in x]
    conteo = {}

    for fila in x:
        letra = fila[0]
        if letra in conteo:
            conteo[letra] += 1
        else:
            conteo[letra] = 1
    return sorted(conteo.items())
