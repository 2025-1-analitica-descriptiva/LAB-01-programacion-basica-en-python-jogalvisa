"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
# import csv

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    # with open("data.csv", "r") as file:
    #     data = list(csv.reader(file, delimiter = "\t"))
    x =  open('D:\\Datos\\Documents\\CLASE ANALITICA DESCRIPTIVA\\LAB-01-programacion-basica-en-python-jogalvisa\\files\\input\\data.csv', 'r').readlines()
    x = [z.replace('\n','') for z in x]
    x = [z.split("\t") for z in x]
    # data = []

    # with open(input_file, "r", encoding="utf-8") as f:
    #     reader = csv.DictReader(f)
    #     for row in reader:
    #         data.append(row)
    y = [z[1] for z in x[:]]
    numeros = [int(x) for x in y]
    suma = sum(numeros)
    return suma