﻿"""
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

def initGallery(type):
    return controller.initGallery(type)

def loadGallery(gallery):
    controller.loadData(gallery)


"""def printSorted(ord_gallery, sample_size=10):
    size = lt.size(ord_gallery)
    if size > sample_size:
        print("Las primeras", sample_size, "obras de arte ordenados son:")
        i = 1
        while i <= sample_size:
            artwork_1 = lt.getElement(ord_gallery,i)
            for k in artwork_1:
                print(f"{k}: {artwork_1[k]}")
"""
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        print("\nSeleccione el tipo de lista con el que desea cargar el catálogo:")
        print("\n1 - Array list\n2 - Linked list")
        op = input("Ingrese la opción seleccionada: ")
        if op == 1:
            type = "ARRAY_LIST"
        else:
            type = "LINKED_LIST"
        gallery = initGallery(type)
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
        print("\nOrdenando artistas...\n")
        sorted_artists = controller.sortByArtistID(gallery)
    elif int(inputs[0]) == 0:
        break
    elif int(inputs[0]) == 2:
        #TODO View Requerimiento 1
        print("Busqueda de artistas por rango de años")
        ai = input("Digite el año inicial de la búsqueda: \n")
        af = input("Digite el año final de la busqueda: \n")
        lista = controller.requerimiento_1(gallery,ai,af)
        print(f"\nHay {lt.size(lista)} artistas nacidos en el rango {ai}-{af}")
        print("\nLos primeros 3 artistas son:\n")
        for i in range(3):
            actual = lt.getElement(lista,i)
            print(actual["DisplayName"],"\t",actual["BeginDate"],"\t",actual["EndDate"],"\t",actual["Gender"],"\t",actual["Nationality"])
        print("\nLos últimos 3 artistas son:\n")
        for i in range(3):
            actual = lt.lastElement(lista)
            print(actual["DisplayName"],"\t",actual["BeginDate"],"\t",actual["EndDate"],"\t",actual["Gender"],"\t",actual["Nationality"])
            lt.removeLast(lista)
        #Función en controller params : ai, af -> retorna [int,int,tuple(dict),tuple(dict)]
            
    elif int(inputs[0]) == 3:
        #TODO View Requerimiento 2
        print("Busqueda de adquisiciones por rango de fecha")
        fi = input("Digite la fecha inicial de la búsqueda: <AAAA-MM-DD>\n")
        ff = input("Digite la fecha final de la busqueda <AAAA-MM-DD>: \n")
        adquisiciones = controller.requerimiento_2(gallery,fi,ff)
        print(f"Hay {lt.size(adquisiciones[0])} obras adquiridas en el rango {fi}-{ff}")
        print(f"\n{adquisiciones[1]} obras fueron compradas.")
        print("\nLas primeras 3 obras son:\n")
        
        for i in range(3):
            actual = lt.getElement(adquisiciones[0],i)
            art_artists = actual["ConstituentID"]
            artists = ""
            if not "," in art_artists:
                art_artists = art_artists[1:len(art_artists)-1]
                art_artists = [art_artists]
            else:
                art_artists = art_artists.split(",")
                art_artists[0] = art_artists[0][1:]
                art_artists[len(art_artists)-1] = art_artists[len(art_artists)-1][:len(art_artists[len(art_artists)-1])-2]
                for i in art_artists:
                    pos = controller.encontrar_ID(sorted_artists, i)
                    artists+=lt.getElement(sorted_artists,pos)["DisplayName"]
            print(actual["Title"],"\t",artists,"\t",actual["Date"],"\t",actual["Medium"],actual["Dimensions"])
            print("\n\n")
        print("\n\nLas últimas 3 obras son:\n")
        for i in range(3):
            actual = lt.lastElement(adquisiciones[0])
            art_artists = actual["ConstituentID"]
            artists = ""
            if not "," in art_artists:
                art_artists = art_artists[1:len(art_artists)-1]
                art_artists = [art_artists]
            else:
                art_artists = art_artists.split(",")
                art_artists[0] = art_artists[0][1:]
                art_artists[len(art_artists)-1] = art_artists[len(art_artists)-1][:len(art_artists[len(art_artists)-1])-2]
                for i in art_artists:
                    pos = controller.encontrar_ID(sorted_artists, i)
                    artists+=lt.getElement(sorted_artists,pos)["DisplayName"]
            print(actual["Title"],"\t",artists,"\t",actual["Date"],"\t",actual["Medium"],actual["Dimensions"])
            lt.removeLast(sorted_artists)
            print("\n\n")
        
        #Función en controller params : fi, ff -> retorna [int,int,tuple(dict),tuple(dict)]       
    elif int(inputs[0]) == 4:
        #TODO View Requerimiento 3
        #try:
        print("="*8+"Clasificación de obras de artista por técnica"+"="*8)
        name = input("Digite el nombre del artista: \n")
        print("\nOrdenando artistas por nombre...")
        sorted_list = controller.sortByArtistName(gallery)
        print("\nArtistas ordenados satisfactoriamente...")
        data = controller.requerimiento_3(gallery,name,sorted_list) #Función en controller params: name -> retorna [int, int,str,list(dict)]
        print("="*8+"Examinar el trabajo del artista: "+name+"="*8)
        print(f"{name} tiene {lt.size(data)} obras a su nombre en el museo.")
        tecnicas = controller.contar_tecnica(data)
        tec = lt.getElement(tecnicas,0)["Medium"]
        print(f"Su técnica más utilizada es {tec} y se presentan a continuación ({lt.size(tecnicas)}):")
        separator = "-"*70
        table_format = "| {} | {} | {} | {} |"
        print(separator)
        print(table_format.format("Titulo","Fecha de la obra","Medio","Dimensiones"))
        for i in range(lt.size(tecnicas)):
            actual = lt.getElement(tecnicas,i)
            print(separator)
            print(table_format.format(actual["Title"],actual["Date"],actual["Medium"],actual["Dimensions"]))
            print(separator)
        """except:
            print("Datos ingresados incorrectamente (¿habrá ingresado correctamente el nombre?) ")
        """
    elif int(inputs[0]) == 5:
        #TODO View Requerimiento 4
        artistas_pais = controller.sortArtist(gallery,sorted_artists)
        print("\nObras catalogadas correctamente...")
        mejores = controller.best_artists(artistas_pais)
        print("Los países con más obras según nacionalidad de su artista son:\n")
        print("País\t\tCantidad artistas")
        for i in range(10):
            elemento = lt.getElement(mejores,i)
            print(f"{elemento[0]}\t\t{elemento[1]}")
        mejor = lt.getElement(mejores,1)[0]
        print(f"\n\nLas 3 primeras y últimas obras de autores {mejor} son:\n")
        print("""\tID\t|\tTitle\t|\tMedium\t|\tDate\t|\tDimensions\t|\tDepartment\t|
        \tClasification""")
        for i in range(3):
            actual = lt.getElement(artistas_pais[mejor],i)
            print(actual["ObjectID"],"\t",actual["Title"],"\t",actual["Medium"],"\t",actual["Date"],"\t",actual["Department"],"\t",actual["Classification"])
            print("\n")
        print("\n\n")
        for i in range(3):
            actual = lt.lastElement(artistas_pais[mejor])
            print(actual["ObjectID"],"\t",actual["Title"],"\t",actual["Medium"],"\t",actual["Date"],"\t",actual["Department"],"\t",actual["Classification"])
            lt.removeLast(artistas_pais[mejor])

    elif int(inputs[0]) == 6:
        #TODO View Requerimiento 5
        print("Traslado de obras")
        department = input("Digite el nombre del departamento de dónde trasladar: \n")
        obras_departamento = controller.obras_departamento(gallery,department)
        print(f"\nHay un total de {lt.size(obras_departamento)} obras para transportar")
        estimado = controller.estimar_valor(obras_departamento)
        print(f"\nEl costo estimado de transporte es de {estimado}")
        obras_antiguas = controller.obras_antiguas(obras_departamento)
        print("Las 5 obras más antiguas a transportar son:\n")
        table_format = "| {} | {} | {} | {} |"
        separator = "-"*70
        print(separator)
        print(table_format.format("Titulo","Fecha de la obra","Medio","Dimensiones"))
        for i in range(5):
            actual = lt.getElement(obras_antiguas,i)
            print(separator)
            print(table_format.format(actual["Title"],actual["Date"],actual["Medium"],actual["Dimensions"]))
            print(separator)
        #Función en controller params: department -> retorna [int, int, float, list[dict],list[dict]]
        obras_costosas = controller.obras_costosas(obras_departamento)
        print("Las 5 obras más costosas a transportar son:\n")
        table_format = "| {} | {} | {} | {} | {} | {} | {} |"
        print(separator)
        print(table_format.format("Titulo","Artista","Clasificacion","Fecha","Medio","Dimensiones","Costo transporte"))
        for i in range(5):
            actual = lt.getElement(obras_costosas,i)
            print(separator)
            print(table_format.format(actual["Title"],actual["Date"],actual["Medium"],actual["Dimensions"]))
            print(separator)
        op = input(f"Hay {lt.size(obras_departamento)} obras a ser transportadas, ¿desea visualizarlas?(Y/N): ")
        if op.lower() == "y":
            for i in range(lt.size(obras_departamento)):
                actual = lt.getElement(obras_departamento,i)
                print(separator)
                print(table_format.format(actual["Title"],actual["ConstituentID"],actual["Classification"],actual["Date"],actual["Medium"],actual["Dimensions"],actual["cost"]))
                print(separator)
        
              
    elif int(inputs[0])== 7:
        #TODO View Requerimiento 6 BONO
        pass
    elif int(inputs[0]) == 3:
        size = int(input("Indique tamaño de la muestra: "))
        if size > lt.size(gallery["artwork"]):
            print("\nTamaño de muestra inválido.")
            continue
        print("\nSeleccione el método de ordenamiento a utilizar:")
        print("\n1 - Shellsort\n2 - Quicksort\n3 - Mergesort\n4 - Insertionsort")
        opt = input("\nOpción seleccionada: ")
        result = controller.sortArtworks(gallery, int(size), opt)
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(round(result[0],2)))

        #printSorted(result[1])

    else:
        sys.exit(0)
sys.exit(0)
