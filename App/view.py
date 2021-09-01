"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por nacionalidad de autor")
    print("6- Transportar obras de un departamento")
    print("7- Proponer una nueva exposición en el museo")
    print("0- Salir")

gallery = None

def initGallery():
    return controller.initGallery()

def loadGallery(gallery):
    controller.loadData(gallery)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        gallery = initGallery()
        loadGallery(gallery)
        size_artists = lt.size(gallery["artists"])
        size_artworks = lt.size(gallery["artwork"])
        print("Artistas cargados:",size_artists)
        print("Obras cargadas: ", size_artworks)
        print("Ultimos 3 artistas y obras: ")
        for i in range(1,4):
            print(f"\nArtista {i}")
            objeto_1 = lt.getElement(gallery["artists"],size_artists-i)
            for j in objeto_1:
                print("{}: {}".format(j, objeto_1[j]))
            print(f"\nObra {i}")
            objeto_2 = lt.getElement(gallery["artwork"],size_artworks-i)
            for k in objeto_2:
                print("{}: {}".format(k, objeto_2[k]))
    elif int(inputs[0]) == 0:
        pass

    else:
        sys.exit(0)
sys.exit(0)
