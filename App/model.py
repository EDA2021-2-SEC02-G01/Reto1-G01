"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.arraylist import subList
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import quicksort as qu
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.Algorithms.Sorting import insertionsort as ins
assert cf
import time 

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newGallery(type):
    gallery = {"artwork":None,"artists":None}
    gallery["artwork"] = lt.newList(type)
    gallery["artists"] = lt.newList(type)
    return gallery
# Funciones para agregar informacion al catalogo
def addArtwork(gallery, artwork):
    lt.addLast(gallery["artwork"], artwork)
    

def addArtist(gallery, artist):
    lt.addLast(gallery["artists"], artist)


# Funciones para creacion de datos

"""def newArtist(artist_info):
    return artist_info"""
# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired(artwork1, artwork2):
    return artwork1["DateAcquired"] < artwork2["DateAcquired"]

# Funciones de ordenamiento
def sortArtworks(gallery, size, sort_type):
    sublist = lt.subList(gallery["artwork"],1,size)
    ordenar = sublist.copy()
    init_time = time.process_time()
    if sort_type == "1":
        sorted = sa.sort(ordenar, cmpArtworkByDateAcquired)
    elif sort_type == "2":
        sorted = qu.sort(ordenar, cmpArtworkByDateAcquired)
    elif sort_type == "3":
        sorted = mg.sort(ordenar, cmpArtworkByDateAcquired)
    else:
        sorted = ins.sort(ordenar, cmpArtworkByDateAcquired)
    stop_time = time.process_time()
    time_mseg = (stop_time - init_time)*1000
    return time_mseg, sorted