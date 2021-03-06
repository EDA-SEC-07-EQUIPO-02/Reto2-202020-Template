"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

moviesDetails="SmallMoviesDetailsCleaned.csv"
moviesCasting= "MoviesCastingRaw-small.csv"



# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________

def printDirectorData(director):

    if director:
        print("Director encontrado: " + director["name"])
        print("Peliculas dirigidas: " + director["movies"])
        print("Numero de peliculas: " + lt.size(director["movies"]))
        print("Promedio de calificación: " + director["average"])
        iterator = it.newIterator(director["movies"])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print("Titulo: " + movie["Title"])
    else:
        print("No se encontró al director")


# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catalogo")
    print("2- Cargar información en el catálogo")
    print("3- Conocer a un actor3")
    print("4- Conocer a un director")
    print("5- Encontrar películas por país")
    print("0- Salir")

"""
Menu Principal
"""
while True:
    printMenu()
    inputs = input("Seleccione una opción para continuar\n")

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo...")
        cont = controller.initCatalog()
    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos")
        controller.loadDataMovies(cont, moviesDetails, moviesCasting)
        print("Peliculas cargadas: "+str(controller.moviesSize(cont)))
        print("Casting cargados: "+ str(controller.castingsSize(cont)))
        print("Actores cargados: "+ str(controller.actorsSize(cont)))
    elif int(inputs[0])==3:
        actor = input("A al que desea conocer: ")
        actorinformacion = controller.getMoviesByActor(catalog, actor)
        print(actorinformacion)
    elif int(inputs[0]) == 4:
        director = input("Director al que busca: ")
        directorinfo = controller.getMoviesbyDirector(director)
        printDirectorData(directorinfo)
    elif int(intput[0]) == 5:
        tiempo= process_time()
        gen= intput("Ingrese el genero deseado")
        gen=controller.inputGenre(catalog, gen)
        for genero in gen:
             Movies= controller.getMoviesByGenre(cont, gen)
        print(Movies)    
        print("la candidad de peliculas son ") + str(controller.genreSize(Movies))    
    #elif int(inputs[0]) == 6:
     #   pais = input("País al que busca: ")
      #  paisinfo = controller.

    else:
        sys.exit(0)
sys.exit(0)
