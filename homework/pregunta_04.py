"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    x =  open('D:\\Datos\\Documents\\CLASE ANALITICA DESCRIPTIVA\\LAB-01-programacion-basica-en-python-jogalvisa\\files\\input\\data.csv', 'r').readlines()
    x = [z.replace('\n','') for z in x]
    x = [z.split("\t") for z in x]
    y = [fila[2].split("-")[1] for fila in x]
    conteo = {}
    for mes in y:
        if mes in conteo:
            conteo[mes] += 1 
        else:
            conteo[mes] = 1
    z = sorted(conteo.items())
    return z
