"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    x =  open('D:\\Datos\\Documents\\CLASE ANALITICA DESCRIPTIVA\\LAB-01-programacion-basica-en-python-jogalvisa\\files\\input\\data.csv', 'r').readlines()
    x = [z.replace('\n','') for z in x]
    x = [z.split("\t") for z in x]
    y = [z[1] for z in x[:]]
    numeros = [int(x) for x in y]
    suma = sum(numeros)
    return suma