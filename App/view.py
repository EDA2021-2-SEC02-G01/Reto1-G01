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

    elif int(inputs[0]) == 0:
        break
    elif int(inputs[0]) == 2:
        #TODO View Requerimiento 1
        print("Busqueda de artistas por rango de años")
        ai = input("Digite el año inicial de la búsqueda: \n")
        af = input("Digite el año final de la busqueda: \n")
        lista = controller.requerimiento_1(gallery,ai,af)
        print(f"Hay {lt.size(lista)} artistas nacidos en el rango {ai}-{af}")
        
        #Función en controller params : ai, af -> retorna [int,int,tuple(dict),tuple(dict)]
        pass      
    elif int(inputs[0]) == 3:
        #TODO View Requerimiento 2
        print("Busqueda de adquisiciones por rango de fecha")
        fi = input("Digite la fecha inicial de la búsqueda: <AAAA-MM-DD>\n")
        ff = input("Digite la fecha final de la busqueda <AAAA-MM-DD>: \n")
        #Función en controller params : fi, ff -> retorna [int,int,tuple(dict),tuple(dict)]
        pass         
    elif int(inputs[0]) == 4:
        #TODO View Requerimiento 3
        try:
            print("="*8+"Clasificación de obras de artista por técnica"+"="*8)
            name = input("Dijite el nombre del artista: \n")
            data = ["A","B","C","D"] #Función en controller params: name -> retorna [int, int,str,list(dict)]
            works = data[3]
            print("="*8+"Examinar el trabajo del artista: "+name+"="*8)
            print("{} con MoMA ID {} tiene {} obras a su nombre en el museo.".format(name,data[0],data[1]))
            print("Su técnica más utilizada es {} y se presentan a continuación ({}):".format(data[2],len(works)))
            separator = "-"*70
            table_format = "| {} | {} | {} | {} |"
            print(separator)
            print(table_format.format("Titulo","Fecha de la obra","Medio","Dimensiones"))
            for work in works:
                print(separator)
                print(table_format.format(work[0],work[1],work[2],work[3]))
                print(separator)
        except:
            print("Datos ingresados incorrectamente (¿habrá ingresado correctamente el nombre?) ")

    elif int(inputs[0]) == 5:
        #TODO View Requerimiento 4
        artistas_pais = controller.sortArtist(gallery)
        print("\nObras catalogadas correctamente...")
        mejores = controller.best_artists(artistas_pais)
        print("Los países con más obras según nacionalidad de su artista son:\n")
        print("País\t\tCantidad artistas")
        for i in range(10):
            elemento = lt.getElement(mejores,i)
            print(f"{elemento[0]}\t\t{elemento[1]}")
        mejor = lt.getElement(mejores,1)[0]
        print(f"Las 3 primeras y últimas obras de autores {mejor} son:\n")
        print("""\tID\t|\tTitle\t|\tMedium\t|\tDate\t|\tDimensions\t|\tDepartment\t|
        \tClasification""")
        for i in range(3):
            actual = lt.getElement(artistas_pais[mejor],i)
            print(actual["ObjectID"],"\t",actual["Title"],"\t",actual["Medium"],"\t",actual["Date"],"\t",actual["Department"],"\t",actual["Classification"])
        for i in range(3):
            actual = lt.removeLast(artistas_pais[mejor])
            print(actual["ObjectID"],"\t",actual["Title"],"\t",actual["Medium"],"\t",actual["Date"],"\t",actual["Department"],"\t",actual["Classification"])
    elif int(inputs[0]) == 6:
        #TODO View Requerimiento 5
        print("Traslado de obras")
        department = input("Digite el nombre del departamento de dónde trasladar: \n")
        #Función en controller params: department -> retorna [int, int, float, list[dict],list[dict]]
        pass       
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
