"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

#leer el archivo data.csv y mostrarlo en pantalla
import csv

def reader_data_csv():
    with open("files\input\data.csv", "r") as file:
        data = list(csv.reader(file, delimiter = "\t"))

    return data
print(reader_data_csv())

def pregunta_01():
    # """
    # Retorne la suma de la segunda columna.

    # Rta/
    # 214

    # """
    # x =  open('D:\\Datos\\Documents\\CLASE ANALITICA DESCRIPTIVA\\LAB-01-programacion-basica-en-python-jogalvisa\\files\\input\\data.csv', 'r').readlines()
    # x = [z.replace('\n','') for z in x]
    # x = [z.split("\t") for z in x]
    # y = [z[1] for z in x[:]]
    # numeros = [int(x) for x in y]
    # suma = sum(numeros)
    # return suma
    #Retornar la suma de la columna 2
    data = reader_data_csv()
    suma = 0
    for row in data:
        suma += int(row[1])
    return suma
#imprima el valor de la suma
#print(pregunta_01())