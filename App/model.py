﻿"""
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


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newGallery():
    gallery = {"artists":None,"artwork":None}
    gallery["artists"] = lt.newList()
    gallery["artwork"] = lt.newList()
    return gallery
# Funciones para agregar informacion al catalogo
def addArtist(gallery, artwork):
    lt.addLast(gallery["artwork"], artwork)
    artist_id = artwork["ConstituentID"].split(",")
    for artist in artist_id:
        addArtwork(gallery, artist.strip(), artwork)

def addArtwork(gallery, artist_id, artwork):
    all_artists = gallery["artists"]
    posartist = lt.isPresent(all_artists, artist_id)
    if posartist > 0:
        artist = lt.getElement(all_artists, posartist)
    else:
        artist = newArtist(artist_id)
        lt.addLast(all_artists, artist)
    lt.addLast(artist["artwork"], artwork)


# Funciones para creacion de datos

def newArtist(artist_id):
    artist = {"id":"","artwork":None}
    artist["id"] = artist_id
    artist["artwork"] = lt.newList()
    return artist
# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento