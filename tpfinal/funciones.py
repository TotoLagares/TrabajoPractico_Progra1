"""
-----------------------------------------------------------------------------------------------
Título: Trabajo practico, primer parcial.
Fecha: 1/11/2024
Autor: Ignacio Bailo, Santiago Lagares, Bautista Gioseffi, Ignacio Mones Ruiz, Tobias Picardo

Descripción: Hoja de python dedicada a las funciones del programa

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import json


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------


def print_dict(a):
    """
    Imprime los elementos activos (estado=True) de un diccionario cargado desde un archivo JSON.
    """
    nombre=obtener_nombre_diccionario(a)
    f= open(f"jsons/{nombre}_json", mode="r", encoding="utf-8")
    a= json.load(f)
    f.close()
    for i in a:
        if a[i]["estado"]:
            print(f"ID: {i} | ", end="")    
            for key, value in a[i].items():
                print(f"{key.capitalize()}: {value} | ", end="")
            print()



def Asignacion():
    """
    Cuenta la cantidad de alumnos por curso y actualiza el campo "alumnos" en los datos de los cursos.
    """
    try:
        # Abro los archivos JSON
        f=open("jsons/alumnos_json", mode="r", encoding="utf-8")
        alumnos=json.load(f)
        f.close()

        f=open("jsons/cursos_json", mode="r", encoding="utf-8")
        cursos=json.load(f)
        f.close()
        # Cuento la cantidad de alumnos por curso
        for i in cursos:
            cont_curso = 0
            for j in alumnos:
                if str(alumnos[j]["curso_id"]) == i:
                    cont_curso += 1
            cursos[i]["alumnos"] = cont_curso  

        # Actualizo el campo "alumnos" en los datos de los cursos
        f=open("jsons/cursos_json", mode="w", encoding="utf-8")
        json.dump(cursos, f, indent=4, ensure_ascii=False)
        f.close()

    except ValueError:
        print("Valor ingresado no válido, intente de nuevo")
    except FileNotFoundError:
        print(f"Archivo JSON no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON.")
    

def asignacion_2():
    """
    Vincula los nombres completos de los profesores con las materias que dictan, actualizando el campo "profesor".
    """
    try:
        # Abro los archivos JSON

        f=open("jsons/materias_json", mode="r", encoding="utf-8")
        materias=json.load(f)
        f.close()

        f=open("jsons/profesores_json", mode="r", encoding="utf-8")
        profesores=json.load(f)
        f.close()

        # Vinculo los nombres completos de los profesores con las materias que dictan
        for i in materias:
            for j in profesores:
                if int(i) in profesores[j]["materias"]:
                    if profesores[j]["nombre"]+" "+profesores[j]["apellido"] not in materias[i]["profesor"]:
                        materias[i]["profesor"].append(profesores[j]["nombre"]+" "+profesores[j]["apellido"])

        # Actualizo el campo "profesor" en los datos de las materias
        f=open("jsons/materias_json", mode="w", encoding="utf-8")
        json.dump(materias, f, indent=4, ensure_ascii=False)
        f.close()

    except ValueError:
        print("Valor ingresado no válido, intente de nuevo")
    except FileNotFoundError:
        print(f"Archivo JSON no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON.")

def asignacion_3():
    """
    Asocia los nombres de las materias a los cursos correspondientes, actualizando el campo "materias" de cada curso.
    """
    try:
        # Abro los archivos JSON
        f=open("jsons/materias_json", mode="r", encoding="utf-8")
        materias=json.load(f)
        f.close()

        f=open("jsons/cursos_json", mode="r", encoding="utf-8")
        cursos=json.load(f)
        f.close()

        # Asocio los nombres de las materias a los cursos correspondientes
        for i in materias:
            for j in cursos:
                if str(materias[i]["curso"]) == j:
                    if materias[i]["materia_nombre"] not in cursos[j]["materias"]:
                        cursos[j]["materias"].append(materias[i]["materia_nombre"])
                        
        # Actualizo el campo "materias" de cada curso
        f=open("jsons/cursos_json", mode="w", encoding="utf-8")
        json.dump(cursos, f, indent=4, ensure_ascii=False)
        f.close()

    except ValueError:
        print("Valor ingresado no válido, intente de nuevo")
    except FileNotFoundError:
        print(f"Archivo JSON no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON.")

def men_2(a):
    """
    Muestra un menú con opciones relacionadas a una entidad específica.
    """
    opciones = [f"[1] Ingresar {a} nuevos", f"[2] Baja de {a}", f"[3] Alta de {a}",
                f"[4] Modificar {a}", f"[5] Ver {a}", f"[0] Atras"]
    for i in opciones:
        print(i)


def obtener_nombre_diccionario(diccionario):
    """
    Devuelve el nombre de un diccionario global en formato string.
    """
    for nombre, valor in globals().items():
        if valor is diccionario:
            return nombre
    return None


def salir():
    """
    Finaliza la ejecución del programa mostrando un mensaje de despedida.
    """
    print("Gracias por usar el programa")
    exit()



def eliminar(nombre_diccionario):
    """
    Marca como inactivo (estado=False) un elemento en un archivo JSON, basado en su ID.
    """
    try:
        # Abro el archivo JSON
        f = open(f"jsons/{nombre_diccionario}_json", mode="r", encoding="utf-8")
        data = json.load(f)
        f.close()

        while True:
            id_eliminar = int(input(f"Ingrese el id del {nombre_diccionario} a dar de baja: "))
            if str(id_eliminar) not in data:
                print("ID no encontrado, intente de nuevo")
                continue
            # Marca como inactivo el elemento en el archivo JSON
            if input(f"Está seguro que desea eliminar {data[str(id_eliminar)]}? [S/N]: ").lower() == "s":
                data[str(id_eliminar)]["estado"] = False
                # Actualizo el archivo JSON
                f=open(f"jsons/{nombre_diccionario}_json", mode="w", encoding="utf-8")
                json.dump(data, f, indent=4, ensure_ascii=False)
                f.close()
                print(f"{data[str(id_eliminar)]} ha sido eliminado.")
                break
            else:
                print(f"No se eliminó {data[id_eliminar]}")
                break

    except ValueError:
        print("Valor ingresado no válido, intente de nuevo")
    except FileNotFoundError:
        print(f"Archivo JSON no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON.")



def alta(nombre_diccionario):
    """
    Marca como activo (estado=True) un elemento previamente inactivo en un archivo JSON, basado en su ID.
    """
    try:
        # Abro el archivo JSON
        f = open(f"jsons/{nombre_diccionario}_json", mode="r", encoding="utf-8")
        data = json.load(f)
        f.close()
        while True:
            # Marca como activo el elemento en el archivo JSON
            id_alta = int(input(f"Ingrese el id del {nombre_diccionario} a dar de alta: "))
            if str(id_alta) not in data:
                print("ID no encontrado, intente de nuevo")
                continue

            # Actualizo el archivo JSON
            if input(f"Está seguro que desea dar de alta {data[str(id_alta)]}? [S/N]: ").lower() == "s":
                data[str(id_alta)]["estado"] = True
                f=open(f"jsons/{nombre_diccionario}_json", mode="w", encoding="utf-8")
                json.dump(data, f, indent=4, ensure_ascii=False)
                f.close()
                break
            else:
                print(f"No se activó {data[str(id_alta)]}")

    except ValueError:
        print("Valor ingresado no válido, intente de nuevo")
    except FileNotFoundError:
        print(f"Archivo jsons/{nombre_diccionario}_json no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo jsons/{nombre_diccionario}_json.")


def modificar(nombre_diccionario):
    """
    Permite modificar un campo específico de un elemento en un archivo JSON, basado en su ID.
    """
    try:
        # Abro el archivo JSON
        f =open(f"jsons/{nombre_diccionario}_json", mode="r", encoding="utf-8")
        data = json.load(f)
        f.close()


        while True:
            # Modifica un campo específico del elemento en el archivo JSON
            id_modificar = int(input(f"Ingrese el id del {nombre_diccionario} a modificar: "))
            if str(id_modificar) not in str(data):
                print("ID no encontrado, intente de nuevo")
                continue
            campo = input(f"Ingrese el campo a modificar: {list(data[str(id_modificar)].keys())} - ")
            # Verifica si el campo ingresado es válido
            if campo in data[str(id_modificar)]:
                data[str(id_modificar)][campo] = input("Ingrese el nuevo valor: ")
                print(f"Objeto modificado: {data[str(id_modificar)]}")
                break
            else:
                print("Campo inválido, intente de nuevo")
            # Actualizo el archivo JSON
            f=open(f"jsons/{nombre_diccionario}_json",mode="w", encoding="utf-8")
            json.dump(data,f,ensure_ascii=False, indent=4)
            f.close()
            
    except ValueError:
        print("Valor ingresado no válido, intente de nuevo")
    except FileNotFoundError:
        print(f"Archivo JSON no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON.")

def buscar(nombre_diccionario):
    """
    Busca e imprime un elemento de un diccionario por su Key, verificando su estado.
    """
    try:
        #  Abro el archivo JSON
        while True:
            f=open(f"jsons/{nombre_diccionario}_json", mode="r", encoding="utf-8")
            a=json.load(f)
            f.close()
            
            # Busca e imprime un elemento del diccionario por su Key
            id_buscar = str(input(f"Ingrese el id del {nombre_diccionario} a buscar: "))
            if id_buscar not in a:
                print("ID no encontrado, intente de nuevo")
                continue
            else:
                if a[id_buscar]["estado"]:
                    print(f"{id_buscar}: {', '.join([f'{key.capitalize()}: {value}' for key, value in a[id_buscar].items()])}")
                else:
                    print(f"{id_buscar} no está activo (estado: False)")
                if input("¿Quiere buscar de nuevo? (s/n): ").lower() != "s":
                    return False
                
    except ValueError:
        print("Valor ingresado no válido, intente de nuevo")
    except FileNotFoundError:
        print(f"Archivo JSON no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON.")


def agregar_alumnos():
    """
    Agrega un nuevo elemento a alumnos_json, inicializando sus campos y asignando 'estado=True' y sus constantes respectivamente.
    """

    try:
        f=open(f"jsons/alumnos_json", mode="r", encoding="utf-8")
        a=json.load(f)
        f.close()
        lista_claves = ["nombre", "apellido", "curso_id" , "telefono", ]
        nuevo_a={}
        for i in lista_claves:
            if  i == "gmail" or i=="estado":
                nuevo_a[i] = ""
            else:
                nuevo_a[i] = input(f"Ingrese el nuevo {i}: ")
        nuevo_a["estado"] = True
        a[len(a)] = nuevo_a

        f=open(f"jsons/alumnos_json", mode="w", encoding="utf-8")
        json.dump(a,f,indent=4, ensure_ascii=False)
        f.close()

    except ValueError:
        print("Valor ingresado no válido, intente de nuevo")
    except FileNotFoundError:
        print(f"Archivo JSON no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON.")

def agregar_profesores():
    """
    Agrega un nuevo elemento a profesores_json, inicializando sus campos y asignando 'estado=True' y sus constantes respectivamente.
    """

    try:
        f=open(f"jsons/profesores_json", mode="r", encoding="utf-8")
        a=json.load(f)
        f.close()

        lista_claves = ["nombre", "apellido" , "telefono" ]
        nuevo_a={}
        for i in lista_claves:
            if  i == "gmail" or i=="estado" or i=="materias":
                nuevo_a[i] = ""
            else:
                nuevo_a[i] = input(f"Ingrese el nuevo {i}: ")

        nuevo_a["estado"] = True
        nuevo_a["materias"] = [x for x in input("Ingrese las materias que dicta separadas por coma: ").split(",")]
        a[len(a)] = nuevo_a

        f=open(f"jsons/profesores_json", mode="w", encoding="utf-8")
        json.dump(a,f,indent=4, ensure_ascii=False)
        f.close()

    except ValueError:
        print("Valor ingresado no válido, intente de nuevo")
    except FileNotFoundError:
        print(f"Archivo JSON no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON.")

def agregar_materias():
    """
    Agrega un nuevo elemento a materias_json, inicializando sus campos y asignando 'estado=True' y sus constantes respectivamente.
    """
    try:
        f=open(f"jsons/materias_json", mode="r", encoding="utf-8")
        a=json.load(f)
        f.close()
        lista_claves = ["materia_nombre", "curso"  ]
        nuevo_a={}
        for i in lista_claves:
            if  i == "gmail" or i=="estado" or i=="profesor":
                nuevo_a[i] = ""
            else:
                nuevo_a[i] = input(f"Ingrese el nuevo {i}: ")
        nuevo_a["estado"] = True
        nuevo_a["profesor"] = []
        a[len(a)] = nuevo_a

        f=open(f"jsons/materias_json", mode="w", encoding="utf-8")
        json.dump(a,f,indent=4, ensure_ascii=False)
        f.close()

    except ValueError:
        print("Valor ingresado no válido, intente de nuevo")
    except FileNotFoundError:
        print(f"Archivo JSON no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON.")

def agregar_cursos():
    """
    Agrega un nuevo elemento a cursos_json, inicializando sus campos y asignando 'estado=True' y sus constantes respectivamente.
    """
    try:
        f=open(f"jsons/cursos_json", mode="r", encoding="utf-8")
        a=json.load(f)
        f.close()
        lista_claves = ["curso_nombre" ]
        nuevo_a={}
        for i in lista_claves:
            if  i == "materias" or i=="estado" or i=="alumnos":
                nuevo_a[i] = ""
            else:
                nuevo_a[i] = input(f"Ingrese el nuevo {i}: ")
        nuevo_a["estado"] = True
        nuevo_a["materias"] = []
        a[len(a)] = nuevo_a

        f=open(f"jsons/cursos_json", mode="w", encoding="utf-8")
        json.dump(a,f,indent=4, ensure_ascii=False)
        f.close()

    except ValueError:
        print("Valor ingresado no válido, intente de nuevo")
    except FileNotFoundError:
        print(f"Archivo JSON no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON.")


def repetir(a):
    """
    Pregunta al usuario si desea realizar otra acción; finaliza el programa si la respuesta es negativa.
    """
    while True:
        respuesta = input("¿Desea realizar otra acción? [S/N]: ").lower()
        if respuesta == "n":
            salir()
        elif respuesta == "s":
            break
        else:
            print("Opción no válida, intente de nuevo.")


def generar_gmail(nombre_diccionario):
    """
    Genera correos electrónicos para todos los elementos de un archivo JSON, basándose en sus nombres y apellidos.
    """
    try:
        # Abro el archivo JSON
        f = open(f"jsons/{nombre_diccionario}_json", mode="r",encoding="utf-8")
        data = json.load(f)
        f.close()
        
        # Genero correos electrónicos para todos los elementos del archivo JSON
        if data == "profesores": 
            dominio = "@profe.edu.ar" 
        else:
            dominio = "@edu.ar"

        for i in data:
            nombre = data[i]["nombre"]
            apellido = data[i]["apellido"]
            inicial = nombre[0]
            correo = f"{inicial.upper()}{apellido.lower()}{dominio}"
            data[i]["gmail"] = correo

        # Actualizo el archivo JSON
        f = open(f"jsons/{nombre_diccionario}_json", mode="w", encoding="utf-8")
        json.dump(data,f,indent=4, ensure_ascii=False)
        f.close()
        
    except ValueError:
        print("Valor ingresado no válido, intente de nuevo")
    except FileNotFoundError:
        print(f"Archivo JSON no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON.")

def llamados_principales():
    """
    Ejecuta las funciones necesarias para inicializar los datos y asignaciones del programa.enera correos electrónicos para profesores y alumnos.
    """
    Asignacion()
    asignacion_2()
    asignacion_3()
    generar_gmail(obtener_nombre_diccionario(profesores))
    generar_gmail(obtener_nombre_diccionario(alumnos))

f=open("jsons/alumnos_json", mode="r", encoding="utf-8")
alumnos=json.load(f)
f.close()

f=open("jsons/profesores_json", mode="r", encoding="utf-8")
profesores=json.load(f)
f.close()

f=open("jsons/cursos_json", mode="r", encoding="utf-8")
cursos=json.load(f)
f.close()

f=open("jsons/materias_json", mode="r", encoding="utf-8")
materias=json.load(f)
f.close()
