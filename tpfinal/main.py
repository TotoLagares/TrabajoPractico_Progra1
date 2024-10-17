import random
import time

alumnos = {
    1: {'id': 0, 'nombre': 'Sofía', 'apellido': 'González', 'curso_id': 0, 'DNI': 47856321, 'gmail': '', 'telefono': '+54 11 12345678'},
    2: {'id': 0, 'nombre': 'Lucas', 'apellido': 'López', 'curso_id': 0, 'DNI': 47912345, 'gmail': '', 'telefono': '+54 11 23456789'},
    3: {'id': 0, 'nombre': 'Martín', 'apellido': 'Pérez', 'curso_id': 1, 'DNI': 48098765, 'gmail': '', 'telefono': '+54 11 34567890'},
    4: {'id': 0, 'nombre': 'Ana', 'apellido': 'Martínez', 'curso_id': 1, 'DNI': 48123456, 'gmail': '', 'telefono': '+54 11 45678901'},
    5: {'id': 0, 'nombre': 'Valentina', 'apellido': 'Ramírez', 'curso_id': 2, 'DNI': 48234567, 'gmail': '', 'telefono': '+54 11 56789012'},
    6: {'id': 0, 'nombre': 'Diego', 'apellido': 'Hernández', 'curso_id': 2, 'DNI': 48345678, 'gmail': '', 'telefono': '+54 11 67890123'},
    7: {'id': 0, 'nombre': 'Camila', 'apellido': 'Torres', 'curso_id': 3, 'DNI': 48456789, 'gmail': '', 'telefono': '+54 11 78901234'},
    8: {'id': 0, 'nombre': 'Javier', 'apellido': 'Sánchez', 'curso_id': 3, 'DNI': 48567890, 'gmail': '', 'telefono': '+54 11 89012345'},
    9: {'id': 0, 'nombre': 'Laura', 'apellido': 'Molina', 'curso_id': 4, 'DNI': 48678901, 'gmail': '', 'telefono': '+54 11 90123456'},
    10: {'id': 0, 'nombre': 'Felipe', 'apellido': 'Cruz', 'curso_id': 4, 'DNI': 48789012, 'gmail': '', 'telefono': '+54 11 01234567'},
    11: {'id': 0, 'nombre': 'Nicolás', 'apellido': 'Jiménez', 'curso_id': 0, 'DNI': 48890123, 'gmail': '', 'telefono': '+54 11 12345678'},
    12: {'id': 0, 'nombre': 'Lucía', 'apellido': 'Salazar', 'curso_id': 0, 'DNI': 48901234, 'gmail': '', 'telefono': '+54 11 23456789'},
    13: {'id': 0, 'nombre': 'Andrés', 'apellido': 'Morales', 'curso_id': 1, 'DNI': 49012345, 'gmail': '', 'telefono': '+54 11 34567890'},
    14: {'id': 0, 'nombre': 'Isabella', 'apellido': 'Vargas', 'curso_id': 1, 'DNI': 49123456, 'gmail': '', 'telefono': '+54 11 45678901'},
    15: {'id': 0, 'nombre': 'Gabriel', 'apellido': 'Aguilar', 'curso_id': 2, 'DNI': 49234567, 'gmail': '', 'telefono': '+54 11 56789012'},
    16: {'id': 0, 'nombre': 'Renata', 'apellido': 'Ponce', 'curso_id': 2, 'DNI': 49345678, 'gmail': '', 'telefono': '+54 11 67890123'},
    17: {'id': 0, 'nombre': 'Esteban', 'apellido': 'Salas', 'curso_id': 3, 'DNI': 49456789, 'gmail': '', 'telefono': '+54 11 78901234'},
    18: {'id': 0, 'nombre': 'Samantha', 'apellido': 'Mendoza', 'curso_id': 3, 'DNI': 49567890, 'gmail': '', 'telefono': '+54 11 89012345'},
    19: {'id': 0, 'nombre': 'Hugo', 'apellido': 'Córdoba', 'curso_id': 4, 'DNI': 49678901, 'gmail': '', 'telefono': '+54 11 90123456'},
    20: {'id': 0, 'nombre': 'Valeria', 'apellido': 'Ríos', 'curso_id': 4, 'DNI': 49789012, 'gmail': '', 'telefono': '+54 11 01234567'},
    21: {'id': 0, 'nombre': 'Joaquín', 'apellido': 'Alvarado', 'curso_id': 0, 'DNI': 49890123, 'gmail': '', 'telefono': '+54 11 12345678'},
    22: {'id': 0, 'nombre': 'Martina', 'apellido': 'Benítez', 'curso_id': 0, 'DNI': 49901234, 'gmail': '', 'telefono': '+54 11 23456789'},
    23: {'id': 0, 'nombre': 'Natalia', 'apellido': 'Rincón', 'curso_id': 1, 'DNI': 50012345, 'gmail': '', 'telefono': '+54 11 34567890'},
    24: {'id': 0, 'nombre': 'Camilo', 'apellido': 'Alvarado', 'curso_id': 1, 'DNI': 50123456, 'gmail': '', 'telefono': '+54 11 45678901'},
    25: {'id': 0, 'nombre': 'Ángela', 'apellido': 'Paz', 'curso_id': 0, 'DNI': 50234567, 'gmail': '', 'telefono': '+54 11 56789012'},
    26: {'id': 0, 'nombre': 'Sebastián', 'apellido': 'Hernández', 'curso_id': 1, 'DNI': 50345678, 'gmail': '', 'telefono': '+54 11 67890123'},
    27: {'id': 0, 'nombre': 'Lucía', 'apellido': 'Salas', 'curso_id': 2, 'DNI': 50456789, 'gmail': '', 'telefono': '+54 11 78901234'},
    28: {'id': 0, 'nombre': 'Ricardo', 'apellido': 'Torres', 'curso_id': 3, 'DNI': 50567890, 'gmail': '', 'telefono': '+54 11 89012345'},
    29: {'id': 0, 'nombre': 'Fernanda', 'apellido': 'Cruz', 'curso_id': 4, 'DNI': 50678901, 'gmail': '', 'telefono': '+54 11 90123456'},
    30: {'id': 0, 'nombre': 'Diego', 'apellido': 'Jiménez', 'curso_id': 0, 'DNI': 50789012, 'gmail': '', 'telefono': '+54 11 01234567'},
}


profesores = {
    1: {"id": 0, "nombre": "Santiago", "apellido": "Pérez", "materias": [1, 9, 19], "DNI": 25473829, "telefono": "+54 11 12345678", "gmail": ""},
    2: {"id": 0, "nombre": "María", "apellido": "López", "materias": [2, 10, 20], "DNI": 25846712, "telefono": "+54 11 23456789", "gmail": ""},
    3: {"id": 0, "nombre": "Carlos", "apellido": "García", "materias": [3, 11, 21], "DNI": 26158976, "telefono": "+54 11 34567890", "gmail": ""},
    4: {"id": 0, "nombre": "Ana", "apellido": "Fernández", "materias": [4, 12, 22], "DNI": 26542315, "telefono": "+54 11 45678901", "gmail": ""},
    5: {"id": 0, "nombre": "Javier", "apellido": "Martínez", "materias": [5, 15, 25], "DNI": 26987451, "telefono": "+54 11 56789012", "gmail": ""},
    6: {"id": 0, "nombre": "Lucía", "apellido": "Gómez", "materias": [6, 16, 26], "DNI": 27234678, "telefono": "+54 11 67890123", "gmail": ""},
    7: {"id": 0, "nombre": "Ricardo", "apellido": "Sánchez", "materias": [7, 17, 27], "DNI": 27548923, "telefono": "+54 11 78901234", "gmail": ""},
    8: {"id": 0, "nombre": "Paola", "apellido": "Ramírez", "materias": [8, 18, 28], "DNI": 27987654, "telefono": "+54 11 89012345", "gmail": ""},
    9: {"id": 0, "nombre": "Diego", "apellido": "Torres", "materias": [29, 31, 41], "DNI": 28345671, "telefono": "+54 11 90123456", "gmail": ""},
    10: {"id": 0, "nombre": "Valentina", "apellido": "Hernández", "materias": [30, 32, 42], "DNI": 28765432, "telefono": "+54 11 01234567", "gmail": ""},
    11: {"id": 0, "nombre": "Fernando", "apellido": "Alvarez", "materias": [33, 34, 44], "DNI": 29098765, "telefono": "+54 11 12345678", "gmail": ""},
    12: {"id": 0, "nombre": "Natalia", "apellido": "Benítez", "materias": [35, 36, 45], "DNI": 29432107, "telefono": "+54 11 23456789", "gmail": ""},
    13: {"id": 0, "nombre": "Emilio", "apellido": "Castro", "materias": [37, 38, 46], "DNI": 29876543, "telefono": "+54 11 34567890", "gmail": ""},
    14: {"id": 0, "nombre": "Camila", "apellido": "Ríos", "materias": [39, 40, 47], "DNI": 30123456, "telefono": "+54 11 45678901", "gmail": ""},
    15: {"id": 0, "nombre": "Gabriel", "apellido": "Ponce", "materias": [41, 42, 48], "DNI": 30567890, "telefono": "+54 11 56789012", "gmail": ""}
}

cursos={
    0: {"id": 0, "curso_nombre": "Primer Año", "materias": [], "alumnos": 0},
    1: {"id": 0, "curso_nombre": "Segundo Año", "materias": [], "alumnos": 0},
    2: {"id": 0, "curso_nombre": "Tercer Año", "materias": [], "alumnos": 0},
    3: {"id": 0, "curso_nombre": "Cuarto Año", "materias": [], "alumnos": 0},
    4: {"id": 0, "curso_nombre": "Quinto Año", "materias": [], "alumnos": 0},
}
materias= {
    1: {"id": 0, "materia_nombre": "Lengua y Literatura I", "profesor": [], "curso": 0},
    2: {"id": 0, "materia_nombre": "Matemática I", "profesor": [], "curso": 0},
    3: {"id": 0, "materia_nombre": "Ciencias Sociales I", "profesor": [], "curso": 0},
    4: {"id": 0, "materia_nombre": "Ciencias Naturales I", "profesor": [], "curso": 0},
    5: {"id": 0, "materia_nombre": "Educación Física I", "profesor": [], "curso": 0},
    6: {"id": 0, "materia_nombre": "Inglés I", "profesor": [], "curso": 0},
    7: {"id": 0, "materia_nombre": "Tecnología I", "profesor": [], "curso": 0},
    8: {"id": 0, "materia_nombre": "Arte I", "profesor": [], "curso": 0},
    9: {"id": 0, "materia_nombre": "Lengua y Literatura II", "profesor": [], "curso": 1},
    10: {"id": 0, "materia_nombre": "Matemática II", "profesor": [], "curso": 1},
    11: {"id": 0, "materia_nombre": "Historia I", "profesor": [], "curso": 1},
    12: {"id": 0, "materia_nombre": "Geografía I", "profesor": [], "curso": 1},
    13: {"id": 0, "materia_nombre": "Biología I", "profesor": [], "curso": 1},
    14: {"id": 0, "materia_nombre": "Química I", "profesor": [], "curso": 1},
    15: {"id": 0, "materia_nombre": "Educación Física II", "profesor": [], "curso": 1},
    16: {"id": 0, "materia_nombre": "Inglés II", "profesor": [], "curso": 1},
    17: {"id": 0, "materia_nombre": "Tecnología II", "profesor": [], "curso": 1},
    18: {"id": 0, "materia_nombre": "Arte II", "profesor": [], "curso": 1},
    19: {"id": 0, "materia_nombre": "Lengua y Literatura III", "profesor": [], "curso": 2},
    20: {"id": 0, "materia_nombre": "Matemática III", "profesor": [], "curso": 2},
    21: {"id": 0, "materia_nombre": "Historia II", "profesor": [], "curso": 2},
    22: {"id": 0, "materia_nombre": "Geografía II", "profesor": [], "curso": 2},
    23: {"id": 0, "materia_nombre": "Física I", "profesor": [], "curso": 2},
    24: {"id": 0, "materia_nombre": "Química II", "profesor": [], "curso": 2},
    25: {"id": 0, "materia_nombre": "Educación Física III", "profesor": [], "curso": 2},
    26: {"id": 0, "materia_nombre": "Inglés III", "profesor": [], "curso": 2},
    27: {"id": 0, "materia_nombre": "Tecnología III", "profesor": [], "curso": 2},
    28: {"id": 0, "materia_nombre": "Arte III", "profesor": [], "curso": 2},
    29: {"id": 0, "materia_nombre": "Lengua y Literatura IV", "profesor": [], "curso": 3},
    30: {"id": 0, "materia_nombre": "Matemática IV", "profesor": [], "curso": 3},
    31: {"id": 0, "materia_nombre": "Historia III", "profesor": [], "curso": 3},
    32: {"id": 0, "materia_nombre": "Geografía III", "profesor": [], "curso": 3},
    33: {"id": 0, "materia_nombre": "Biología II", "profesor": [], "curso": 3},
    34: {"id": 0, "materia_nombre": "Física II", "profesor": [], "curso": 3},
    35: {"id": 0, "materia_nombre": "Química III", "profesor": [], "curso": 3},
    36: {"id": 0, "materia_nombre": "Educación Física IV", "profesor": [], "curso": 3},
    37: {"id": 0, "materia_nombre": "Inglés IV", "profesor": [], "curso": 3},
    38: {"id": 0, "materia_nombre": "Tecnología IV", "profesor": [], "curso": 3},
    39: {"id": 0, "materia_nombre": "Arte IV", "profesor": [], "curso": 3},
    40: {"id": 0, "materia_nombre": "Lengua y Literatura V", "profesor": [], "curso": 4},
    41: {"id": 0, "materia_nombre": "Matemática V", "profesor": [], "curso": 4},
    42: {"id": 0, "materia_nombre": "Historia IV", "profesor": [], "curso": 4},
    43: {"id": 0, "materia_nombre": "Geografía IV", "profesor": [], "curso": 4},
    44: {"id": 0, "materia_nombre": "Ciencias Naturales I", "profesor": [], "curso": 4},
    45: {"id": 0, "materia_nombre": "Orientación Vocacional I", "profesor": [], "curso": 4},
    46: {"id": 0, "materia_nombre": "Inglés V", "profesor": [], "curso": 4},
    47: {"id": 0, "materia_nombre": "Educación Física V", "profesor": [], "curso": 4},
    48: {"id": 0, "materia_nombre": "Tecnología V", "profesor": [], "curso": 4},
    49: {"id": 0, "materia_nombre": "Arte V", "profesor": [], "curso": 4},
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
            if cursos[i]["id"]==alumnos[j]["curso_id"]:
                cont_curso+=1
                cursos[i]["alumnos"]=cont_curso
    return cursos

def asignacion_2(a,b,c:str,d:str,f:str,g:str,h:str):
    for i in a:
        for j in b:    
            if a[i][c] in b[j][d]:
                a[i][f].append(b[j][g]+" "+b[j][h]) 
    return a

def asignacion_3(materias, cursos):
    for i in materias:
        for j in cursos:
            if materias[i]["curso"] == cursos[j]["id"]:
                cursos[j]["materias"].append(materias[i]["materia_nombre"])
    return cursos

def men_2(a):
    opciones=[f"[1] Ingresar {a} nuevos", f"[2] Eliminar {a}", f"[3] Modificar {a}", f"[4] Ver {a}", f"[0] Atras"]
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
            elegir = input(f"Ingrese el campo a modificar: {a[i]} - ")
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
    lista_claves = []
    nuevo_a = {}   
    for valor, clave in a.items():
        for j in clave:
            clave = j
            lista_claves.append(clave)
            print(clave)
        break
    for i in lista_claves:
        if i == "id":
            nuevo_a[i] = len(a)
            continue
        elif i == "alumnos":
            nuevo_a[i] = 0
            continue
        elif i == "profesor" or i=="materias": 
            nuevo_a[i] = []
            continue
        else:
            nuevo_a[i] = input(f"Ingrese el nuevo {i}: ")
    
    a[len(a)+1] = nuevo_a
    Asignacion(alumnos, cursos)
    asignacion_2(materias, profesores, "id","materias","profesor","nombre","apellido")
    asignacion_3(materias, cursos)
    print(nuevo_a)



def repetir(a):
    while True:
        asdc=str(input("Desea realizar otra acción? [S/N]: ")).lower()
        if asdc=="n":
            main()
        elif asdc=="s":
            break
        else:
            print("Opción no válida")

def main():
    id_loop(alumnos)
    id_loop(profesores)
    id_loop(cursos)
    id_loop(materias)
    Asignacion(alumnos, cursos)
    asignacion_2(materias, profesores, "id","materias","profesor","nombre","apellido")
    asignacion_3(materias, cursos)
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
                print_dict(materias)
            elif elec2 == "0":
                main()
            repetir(materias)
            break



            
        elif opcion_elec == "0":
            print("Saliendo del programa...")
            exit()
main()

## 0. arreglar el bug de agregar
## 1. Mejorar los prints con lo de la clase 4
## 2. Llamar las funciones de otros archivos para dejar el main cortito
## 3. Revisar si vimos del (eliminar)
## 4. Nombre de profesores repetidos en materias["profesor"]