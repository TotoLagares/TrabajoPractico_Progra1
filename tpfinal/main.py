import random
import time

alumnos={ 
        1:{"id": 0 , "nombre": "Santiago", "apellido": "Pérez", "curso_id": 3},
        2:{"id": 0 ,"nombre": "María", "apellido": "González", "curso_id": 6},
        3:{"id": 0 ,"nombre": "José", "apellido": "López", "curso_id": 6}
         }

profesores={ 
        1:{"id": 0 , "nombre": "Santiago", "apellido": "Pérez", "materias": [3,6,7,8]},
        2:{"id": 0 ,"nombre": "María", "apellido": "González", "materias": [5]},
        3:{"id": 0 ,"nombre": "José", "apellido": "López", "materias": [3,1,2]}
         }

cursos={
        1:{"id":0, "curso_nombre":"primero A", "alumnos":0, "materias": []},
        2:{"id":0, "curso_nombre":"primero A", "alumnos":0, "materias":[]}
        }

materias={
        1:{"id":0, "curso_nombre":"geografia", "profesor":[], "curso": 1},
        2:{"id":0, "curso_nombre":"historia", "profesor":[], "curso":1}
        }

def id_loop(a):
    id_count=0
    for i in a:
        a[i]["id"]=id_count
        id_count+=1
    return a

def print_dict(a):
    for i in a:
        print(a[i])

def Asignacion(alumnos, cursos):
    for i in cursos:
        cont_curso=0
        for j in alumnos:
            if cursos[i]["id"]==alumnos[j]["id"]:
                cont_curso+=1
                cursos[i]["alumnos"]=cont_curso
    return cursos

def asignacion_2(a,b,c:str,d:str,f:str,g:str):
    for i in a:
        for j in b:    
            if a[i][c] in b[j][d]:
                a[i][f].append(b[j][g]) 
    return a

def asignacion_3(materias, cursos):
    for i in materias:
        for j in cursos:
            if materias[i]["curso"] == cursos[j]["id"]:
                cursos[j]["materias"].append(materias[i]["id"])
    return cursos

def men_2(a):
    opciones=[f"[1] Ingresar {a} nuevos", f"[2] Eliminar {a}", f"[3] Modificar {a}", f"[4] Ver {a}", f"[0] Salir"]
    for i in opciones:
        print(i)

def obtener_nombre_diccionario(diccionario):
    for nombre, valor in globals().items():
        if valor is diccionario:
            return nombre
    return None

def salir():
    print("Gracias por usar el programa")
    exit()

def eliminar(a):
    id_eliminar = int(input(f"Ingrese el id del {obtener_nombre_diccionario(a)} a eliminar: "))
    claves_a_eliminar = []
    for i in a:
        if a[i]["id"] == id_eliminar:
            claves_a_eliminar.append(i)
    if input(f"Está seguro que desea eliminar {a[claves_a_eliminar[0]]}? [S/N]: ").lower() == "s":
        for clave in claves_a_eliminar:
            del a[clave]
    else:
        print(f"No se eliminó {a[claves_a_eliminar[0]]}")
    return a

def modificar(a):
    id_modificar = int(input(f"Ingrese el id del {obtener_nombre_diccionario(a)} a modificar: "))
    for i in a:
        if a[i]["id"] == id_modificar:
            elegir = input(f"Ingrese el campo a modificar: {a[i]}")
            for j in a[i]:
                if j == elegir:
                    a[i][j] = input("Ingrese el nuevo valor: ")
                    print(a[i])
                    break   
    return a

def buscar(a):
    id_buscar = int(input(f"Ingrese el id del {obtener_nombre_diccionario(a)} a buscar: "))
    for i in a:
        if a[i]["id"] == id_buscar:
            print(a[i])

def agregar(a:dict):
    print("no funca")
    

def main():
    id_loop(alumnos)
    id_loop(profesores)
    id_loop(cursos)
    id_loop(materias)
    Asignacion(alumnos, cursos)
    asignacion_2(materias, profesores, "id","materias","profesor","id")
    asignacion_3(materias, cursos)
    opciones = ["1- Alumnos", "2- Profesores", "3- Cursos", "4- Materias", "0- Salir"]
    for opcion in opciones:
        print(opcion)
    opcion_elec = input("Ingrese una opción: ")

    if opcion_elec == "1":
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
                salir()
            else:
                print("Opción no válida")
            while True:
                asdc=str(input("Desea realizar otra acción? [S/N]: ")).lower()
                if asdc=="n":
                    break
                elif asdc=="s":
                    break
                else:
                    print("Opción no válida")
            if asdc=="n":
                break 

    elif opcion_elec == "2":
        while True:
            men_2(obtener_nombre_diccionario(profesores))
            elec2=input("Ingrese una opción: ")
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
                salir()
            else:
                print("Opción no válida")
            while True:
                asdc=str(input("Desea realizar otra acción? [S/N]: ")).lower()
                if asdc=="n":
                    break
                elif asdc=="s":
                    break
                else:
                    print("Opción no válida")
            if asdc=="n":
                break
    elif opcion_elec == "3":
        men_2(obtener_nombre_diccionario(cursos))
    elif opcion_elec == "4":
        men_2(obtener_nombre_diccionario(materias))
    elif opcion_elec == "0":
        salir()
    else:
        print("Opción no válida")
main()

## 0. arreglar el bug de agregar
## 1. Mejorar los prints con lo de la clase 4
## 2. Llamar las funciones de otros archivos para dejar el main cortito
## 3. Revisar si vimos del (eliminar)
