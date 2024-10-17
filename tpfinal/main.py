
from dicts import *
from funciones import *

def main():
    llamados_principales()
    while True:
        opciones = ["1- Alumnos", "2- Profesores", "3- Cursos", "4- Materias", "0- Salir"]
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
                    modificar(alumnos)
                elif elec2 == "4":
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
                if elec2 not in ("0", "1", "2", "3", "4"):
                    print("opcion no valida, intente de nuevo")
                    continue
                if elec2 == "1":
                    agregar(profesores)
                elif elec2 == "2":
                    eliminar(profesores)
                elif elec2 == "3":
                    modificar(profesores)
                elif elec2 == "4":
                    if input("[1] Desea ver todo los profesores o [2] un profesor en particular: ") == "1":
                        print_dict(profesores)
                    else:
                        buscar(profesores)
                elif elec2 == "0":
                    main()
                repetir(profesores)
                
                
        elif opcion_elec == "3":
            while True:
                men_2(obtener_nombre_diccionario(cursos))
                elec2=input("Ingrese una opción: ")
                if elec2 not in ("0", "1", "2", "3", "4"):
                    print("opcion no valida, intente de nuevo")
                    continue
                elif elec2 == "1":
                    agregar(cursos)
                elif elec2 == "2":
                    eliminar(cursos)
                elif elec2 == "3":
                    modificar(cursos)
                elif elec2 == "4":
                    if input("[1] Desea ver todo los cursos o [2] un curso en particular: ") == "1":
                        print_dict(cursos)
                    else:
                        buscar(cursos)
                elif elec2 == "0":
                    main()
                repetir(cursos)
                        
        elif opcion_elec == "4":
            men_2(obtener_nombre_diccionario(materias))
            elec2=input("Ingrese una opción: ")
            if elec2 not in ("0", "1", "2", "3", "4"):
                print("opcion no valida, intente de nuevo")
                continue
            elif elec2 == "1":
                agregar(materias)
            elif elec2 == "2":
                eliminar(materias)
            elif elec2 == "3":
                modificar(materias)
            elif elec2 == "4":
                if input("[1] Desea ver todo los cursos o [2] un curso en particular: ") == "1":
                    print_dict(cursos)
                else:
                    buscar(cursos)
            elif elec2 == "0":
                main()
            repetir(materias)
            break
        elif opcion_elec == "0":
            print("Saliendo del programa...")
            exit()
main()

## 1. Mejorar los prints con lo de la clase 4