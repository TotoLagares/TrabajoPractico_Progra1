
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
from funciones import *

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
...
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    """
    Punto de entrada principal del programa.

    Funcionamiento:
        - Inicializa las configuraciones principales y realiza las asignaciones necesarias mediante `llamados_principales`.
        - Presenta un menú principal al usuario con opciones para gestionar diferentes entidades (alumnos, profesores, cursos y materias).
        - Para cada entidad, muestra un submenú con acciones disponibles como agregar, eliminar, modificar, ver y buscar objetos.
        - Incluye manejo de errores para entradas no válidas.
    Excepciones:
        - Maneja errores por entradas no válidas (ValueError).
        - Captura errores inesperados (Exception) y notifica al usuario.
    """
    try:
        llamados_principales()
        while True:
            # Menú principal
            opciones = ["[1] Alumnos", "[2] Profesores", "[3] Cursos", "[4] Materias", "[0] Salir"]
            for opcion in opciones:
                print(opcion)
            opcion_elec = input("Ingrese una opción: ")
            
            if opcion_elec not in ("0", "1", "2", "3", "4"):
                print("Opción no válida, intente de nuevo")
                continue

            # Gestión de Alumnos
            elif opcion_elec == "1":
                while True:
                    men_2(obtener_nombre_diccionario(alumnos))
                    elec2 = input("Ingrese una opción: ")
                    if elec2 == "1":
                        agregar(obtener_nombre_diccionario(alumnos))
                        llamados_principales()
                    elif elec2 == "2":
                        eliminar(obtener_nombre_diccionario(alumnos))
                    elif elec2 == "3":
                        alta(obtener_nombre_diccionario(alumnos))
                    elif elec2 == "4":
                        modificar(obtener_nombre_diccionario(alumnos))
                    elif elec2 == "5":
                        if input("[1] Ver todos los alumnos o [2] Uno en particular: ") == "1":
                            print_dict(alumnos)
                        else:
                            buscar(alumnos)
                    elif elec2 == "0":
                        break
                    else:
                        print("Opción no válida")
                        continue
                    repetir(alumnos)

            # Gestión de Profesores
            elif opcion_elec == "2":
                while True:
                    men_2(obtener_nombre_diccionario(profesores))
                    elec2 = input("Ingrese una opción: ")
                    if elec2 == "1":
                        agregar(obtener_nombre_diccionario(profesores))
                        llamados_principales()
                    elif elec2 == "2":
                        eliminar( obtener_nombre_diccionario(profesores))
                    elif elec2 == "3":
                        alta(obtener_nombre_diccionario(profesores))
                    elif elec2 == "4":
                        modificar(obtener_nombre_diccionario(alumnos))
                    elif elec2 == "5":
                        if input("[1] Ver todos los profesores o [2] Uno en particular: ") == "1":
                            print_dict(profesores)
                        else:
                            buscar(profesores)
                    elif elec2 == "0":
                        break
                    else:
                        print("Opción no válida")
                        continue
                    repetir(profesores)

            # Gestión de Cursos
            elif opcion_elec == "3":
                while True:
                    men_2(obtener_nombre_diccionario(cursos))
                    elec2 = input("Ingrese una opción: ")
                    if elec2 == "1":
                        agregar(obtener_nombre_diccionario(cursos))
                        llamados_principales()
                    elif elec2 == "2":
                        eliminar(obtener_nombre_diccionario(cursos))
                    elif elec2 == "3":
                        alta(obtener_nombre_diccionario(cursos))
                    elif elec2 == "4":
                        modificar(obtener_nombre_diccionario(cursos))
                    elif elec2 == "5":
                        if input("[1] Ver todos los cursos o [2] Uno en particular: ") == "1":
                            print_dict(cursos)
                        else:
                            buscar(cursos)
                    elif elec2 == "0":
                        break
                    else:
                        print("Opción no válida")
                        continue
                    repetir(cursos)

            # Gestión de Materias
            elif opcion_elec == "4":
                while True:
                    men_2(obtener_nombre_diccionario(materias))
                    elec2 = input("Ingrese una opción: ")
                    if elec2 == "1":
                        agregar(obtener_nombre_diccionario(materias))
                        llamados_principales()
                    elif elec2 == "2":
                        eliminar(obtener_nombre_diccionario(materias))
                    elif elec2 == "3":
                        alta(obtener_nombre_diccionario(materias))
                    elif elec2 == "4":
                        modificar(obtener_nombre_diccionario(materias))
                    elif elec2 == "5":
                        if input("[1] Ver todas las materias o [2] Una en particular: ") == "1":
                            print_dict(materias)
                        else:
                            buscar(materias)
                    elif elec2 == "0":
                        break
                    else:
                        print("Opción no válida")
                        continue
                    repetir(materias)

            # Salir del programa
            elif opcion_elec == "0":
                print("Gracias por usar el programa. Saliendo...")
                exit()

    except ValueError:
        print("Error: Entrada no válida, intente nuevamente.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}. Por favor, reinicie el programa.")
# Punto de entrada al programa---
main()