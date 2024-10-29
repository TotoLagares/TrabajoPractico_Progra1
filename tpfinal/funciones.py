from dicts import *

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
    while True:
        id_eliminar = int(input(f"Ingrese el id del {obtener_nombre_diccionario(a)} a eliminar: "))
        if id_eliminar not in a:
            print("id no encontrado, intente de nuevo")
            continue
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
    while True:
        id_modificar = int(input(f"Ingrese el id del {obtener_nombre_diccionario(a)} a modificar: "))
        if id_modificar not in a:
            print("Id no encontrado, intente de nuevo")
            continue
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
    while True:
        id_buscar = int(input(f"Ingrese el id del {obtener_nombre_diccionario(a)} a buscar: "))
        if id_buscar not in a:
            print("Id no encontrado, intente de nuevo")
            continue
        for i in a:
            if a[i]["id"] == id_buscar:
                print(a[i])
                if str(input("Quiere buscar de nuevo? ")).lower() == "s":
                    continue
                else:
                    return False

def agregar(a:dict):
    lista_claves = []
    nuevo_a = {}   
    for valor, clave in a.items():
        for j in clave:
            clave = j
            lista_claves.append(clave)
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
        elif i== "gmail":
            nuevo_a[i] = ''
            continue
        else:
            nuevo_a[i] = input(f"Ingrese el nuevo {i}: ")
    
    a[len(a)+1] = nuevo_a
    llamados_principales()
    print(nuevo_a)


def repetir(a):
    while True:
        asdc=str(input("Desea realizar otra acción? [S/N]: ")).lower()
        if asdc=="n":
            exit()
        elif asdc=="s":
            break
        else:
            print("Opción no válida, intente de nuevo")

def generar_gmail(a):
    if a == "profesores":
        gmail = '@profe.edu.ar'
    else:
        gmail = "@edu.ar"
    
    for i in a:
        inicial = ""
        ape = ""
        for j in a[i]:
            if j == "nombre":
                inicial = a[i][j][0]
            elif j == "apellido":
                ape = a[i][j]
            elif j == "gmail":
                a[i][j] = inicial.lower() + ape.lower() + gmail
    return a
            
def llamados_principales():
    id_loop(alumnos)
    id_loop(profesores)
    id_loop(cursos)
    id_loop(materias)
    Asignacion(alumnos, cursos)
    asignacion_2(materias, profesores, "id","materias","profesor","nombre","apellido")
    asignacion_3(materias, cursos)
    generar_gmail(alumnos)
    generar_gmail(profesores)
