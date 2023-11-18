from pantalla_fin import *

def obtener_puntajes(path):
    """Funcion encargada de obtener los puntajes de partidas anteriores

    Args:
        path (type): path relativo de archivo csv donde se encuentras los puntajes

    Returns:
        Str: devuelve un string con todos los puntajes separados por coma
    """
    with open(path,"r") as archivo:
        texto = archivo.read()
    return texto

def formatear_puntajes(puntaje):
    """Funcion encargada de separar los puntajes y meterlos en una lista

    Args:
        puntaje (type): string donde se ecuentras los puntajes separados por comas
    Returns:
        List: lista con los puntajes
    """
    retorno = puntaje.split(",")
    return retorno

def obtener_mejores_puntajes(lista_puntajes):
    """Funcion encargada de comparar los puntajes y delvolver una lista ordenanda de mayor a menor

    Args:
        lista_puntajes (list): lista de todos los puntajes

    Returns:
        list: una lista donde se ecuentran todos los puntajes ordenados de mayor a menor
    """
    lista = lista_puntajes
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if int(lista[j]) > int(lista[i]):
                lista[i],lista[j] = lista[j], lista[i]
    return lista

def agregar_puntaje(lista_puntajes,puntaje,path):
    """Funcion encargada de agregar el puntaje de la partida al archivo csv

    Args:
        lista_puntajes (type): lista donde estan todos los puntajes
        puntaje (type): puntaje de la partida
        path (type): path relativo del archivo csv
    """
    lista_puntajes.append(str(puntaje))
    texto = ','
    texto = texto.join(lista_puntajes)
    with open(path,"w") as archivo:
        archivo.write(texto)