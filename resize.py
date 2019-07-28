#!/usr/bin/python
from PIL import Image # Libreria para manipular imagenes
import os, sys # Librerias para manipular SO

path = "Pool_Imgs/" # Ruta de las imagenes descomprimidas y listas para el tratamiento
dirs = os.listdir( path ) # Ruta individual de cada archivo en la carpeta

def resize():
    """
Funcion que permite tratar y dar un tamaño especifico a las imagenes
a traves de una estrategia,dando como retroalimentacion un mensaje 
cada que 10000 imagenes convertidas"""
    i=0
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((224,224), Image.ANTIALIAS)
            imResize.save(f + '.png', 'PNG', quality=100)
            i += 1
            if i % 10000 == 0:
                print("Iteracion {}".format(i))
    print("Tarea completa con exito")