
"""
-----------------------------------------------------------------------------------------------
Título: Trabajo practico, primer parcial
Fecha: 1/11/2024
Autor: Ignacio Bailo, Santiago Lagares, Bautista Gioseffi, Ignacio Mones Ruiz, Tobias Picardo

Descripción: Programa orientado a la gestion academica nivel secundario con funcionalidades
para agregar, eliminar, modificar y buscar entre entidades (Alumnos, Profesores, Cursos, Materias).
Tambien relacion entre entidades y la estructura de sus datos.

Pendientes:
# Proyecto segunda parte:
#         instancias de evaluacion de las materias
#         notas de alumnos de la materias
#         informes de cursadas
#         Arreglar crud (keys)
#         Comentarios en lineas (?)
#         Mejorar docString
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
from dicts import *
from funciones import *


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    try: 
        llamados_principales()
        while True:
            opciones = ["[1] Alumnos", "[2] Profesores", "[3] Cursos", "[4] Materias", "[0] Salir"]
            for opcion in opciones:
                print(opcion)
            opcion_elec = input("Ingrese una opción: ")
            if opcion_elec not in ("0","1","2","3","4"):
                print("opcion no valida, intente de nuevo")
                continue

            elif opcion_elec == "1":
                while True:
                    men_2(obtener_nombre_diccionario(alumnos))
                    elec2=input("Ingrese una opción: ")
                    if elec2 == "1":
                        agregar(alumnos)
                    elif elec2 == "2":
                        eliminar(alumnos)
                    elif elec2 == "3":
                        alta(alumnos)
                    elif elec2 == "4":
                        modificar(alumnos)
                    elif elec2 == "5":
                        if input("[1] Desea ver todo los alumnos o [2] un alumno en particular: ") == "1":
                            print_dict(alumnos)
                        else:
                            buscar(alumnos)
                    elif elec2 == "0":
                        main()
                    else:
                        print("Opción no válida")
                        continue
                    repetir(alumnos)
                    
            elif opcion_elec == "2":
                while True:
                    men_2(obtener_nombre_diccionario(profesores))
                    elec2=input("Ingrese una opción: ")
                    if elec2 == "1":
                        agregar(profesores)
                    elif elec2 == "2":
                        eliminar(profesores)
                    elif elec2 == "3":
                        alta(profesores)                    
                    elif elec2 == "4":
                        modificar(profesores)
                    elif elec2 == "5":
                        if input("[1] Desea ver todo los profesores o [2] un profesor en particular: ") == "1":
                            print_dict(profesores)
                        else:
                            buscar(profesores)
                    elif elec2 == "0":
                        main()
                    else:
                        print("Opción no válida")
                        continue                   
                    repetir(profesores)
                    
                    
            elif opcion_elec == "3":
                while True:
                    men_2(obtener_nombre_diccionario(cursos))
                    elec2=input("Ingrese una opción: ")
                    if elec2 == "1":
                        agregar(cursos)
                    elif elec2 == "2":
                        eliminar(cursos)
                    elif elec2 == "3":
                        alta(cursos)
                    elif elec2 == "4":
                        modificar(cursos)
                    elif elec2 == "5":
                        if input("[1] Desea ver todo los cursos o [2] un curso en particular: ") == "1":
                            print_dict(cursos)
                        else:
                            buscar(cursos)
                    elif elec2 == "0":
                        main()
                    else:
                        print("Opción no válida")
                        continue
                    repetir(cursos)
                            
            elif opcion_elec == "4":
                while True:
                    men_2(obtener_nombre_diccionario(materias))
                    elec2=input("Ingrese una opción: ")
                    if elec2 == "1":
                        agregar(materias)
                    elif elec2 == "2":
                        eliminar(materias)
                    elif elec2 == "3":
                        alta(materias)
                    elif elec2 == "4":
                        modificar(materias)
                    elif elec2 == "5":
                        if input("[1] Desea ver todas las materias o [2] una materia en particular: ") == "1":
                            print_dict(cursos)
                        else:
                            buscar(cursos)       
                    elif elec2 == "0":
                        main()
                    else:
                        print("Opción no válida")
                        continue
                    repetir(materias)
            elif opcion_elec == "0":
                print("Saliendo del programa...")
                exit()
    except Exception as e:
        print("Ha ocurrido un error")


# Punto de entrada al programa
main()
