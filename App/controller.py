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
 """

import config as cf
import model
import csv
from DISClib.ADT import list as lt


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de obras
def initGallery(type):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    gallery = model.newGallery(type)
    return gallery

def initArtists():
    return model.ArtistNationGallery()

# Funciones para la carga de datos

def loadData(gallery):
    """
    Carga los datos de los archivos 
    """
    loadArtists(gallery)
    loadArtworks(gallery)

def loadArtists(gallery):
    """
    Carga los artistas de un archivo. 
    """
    artistFile = cf.data_dir + "MoMA/Artists-utf8-small.csv"
    input_file = csv.DictReader(open(artistFile, encoding="utf-8"))
    for artist in input_file:
        model.addArtist(gallery, artist)

def loadArtworks(gallery):
    """
    Carga los artworks de un archivo
    """
    artworksFile = cf.data_dir + "MoMA/Artworks-utf8-small.csv"
    input_file = csv.DictReader(open(artworksFile,encoding="utf-8"))
    for artwork in input_file:
        model.addArtwork(gallery, artwork)

# Funciones de ordenamiento

def sortArtworks(gallery, size, sort_type):
    return model.sortArtworks(gallery, size, sort_type)

def sortArtist(gallery,sorted_artists):
    nations = initArtists()
    for i in range(lt.size(gallery["artwork"])):
        model.sortArtist(gallery,nations,lt.getElement(gallery["artwork"],i),sorted_artists)
    return nations

def best_artists(artist_nations):
    return model.sortArtistsbyNation(artist_nations)

def sortByArtistID(gallery):
    return model.sortByArtistID(gallery)

def sortByArtistName(gallery):
    return model.sortByArtistName(gallery)

def encontrar_ID(artist_sorted,value):
    return model.busqueda_binaria(0,lt.size(artist_sorted)-1,artist_sorted,value)
    

    
# Funciones de consulta sobre el catálogo

def requerimiento_1(gallery,ai,af):
    return model.requerimiento_1(gallery,ai,af)
def requerimiento_2(gallery,fi,ff):
    return model.requerimiento_2(gallery,fi,ff)
def requerimiento_3(gallery,name,sorted_artists):
    return model.requerimiento_3(gallery,name,sorted_artists)
def contar_tecnica(data):
    return model.contar_tecnica(data)
def obras_departamento(gallery, department):
    return model.obras_departamento(gallery,department)
def estimar_valor(obras):
    return model.estimar_valor(obras)
def obras_antiguas(departamento):
    return model.obras_antiguas(departamento)
def obras_costosas(departamento):
    return model.obras_costosas(departamento)

