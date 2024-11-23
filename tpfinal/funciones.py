"""
-----------------------------------------------------------------------------------------------
Título: Trabajo práctico, primer parcial.
Fecha: 1/11/2024
Autores: Ignacio Bailo, Santiago Lagares, Bautista Gioseffi, Ignacio Mones Ruiz, Tobias Picardo

Descripción: Hoja de Python dedicada a las funciones del programa.

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
    nombre = obtener_nombre_diccionario(a)
    # Carga los datos desde el archivo JSON correspondiente.
    f = open(f"jsons/{nombre}_json", mode="r", encoding="utf-8")
    a = json.load(f)
    f.close()
    # Itera sobre cada elemento del diccionario y lo imprime si está activo.
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
        f = open("jsons/alumnos_json", mode="r", encoding="utf-8")
        alumnos = json.load(f)
        f.close()

        f = open("jsons/cursos_json", mode="r", encoding="utf-8")
        cursos = json.load(f)
        f.close()
        # Itera sobre los cursos y los alumnos, y si el ID del curso está en los cursos de los alumnos, se suma 1 al contador de alumnos.   
        for i in cursos:
            cont_curso = 0
            for j in alumnos:
                if str(alumnos[j]["curso_id"]) == i:
                    cont_curso += 1
            cursos[i]["alumnos"] = cont_curso

    except ValueError:
        print("Valor ingresado no válido, intente de nuevo")
    except FileNotFoundError:
        print(f"Archivo no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo.")

    f = open("jsons/cursos_json", mode="w", encoding="utf-8")
    json.dump(cursos, f, indent=4, ensure_ascii=False)
    f.close()


def asignacion_2():
    """
    Vincula los nombres completos de los profesores con las materias que dictan, actualizando el campo "profesor".
    """
    try:
        f = open("jsons/materias_json", mode="r", encoding="utf-8")
        materias = json.load(f)
        f.close()

        f = open("jsons/profesores_json", mode="r", encoding="utf-8")
        profesores = json.load(f)
        f.close()
        # Itera sobre las materias y los profesores, y si el ID de la materia está en las materias del profesor, se agrega el nombre completo del profesor a la lista de profesores de la materia.
        for i in materias:
            for j in profesores:
                if int(i) in profesores[j]["materias"]:
                    if profesores[j]["nombre"] + " " + profesores[j]["apellido"] not in materias[i]["profesor"]:
                        materias[i]["profesor"].append(profesores[j]["nombre"] + " " + profesores[j]["apellido"])

        f = open("jsons/materias_json", mode="w", encoding="utf-8")
        json.dump(materias, f, indent=4, ensure_ascii=False)
        f.close()
    except ValueError:
        print("Valor ingresado no válido, intente de nuevo")
    except FileNotFoundError:
        print(f"Archivo no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo.")


def asignacion_3():
    """
    Asocia los nombres de las materias a los cursos correspondientes, actualizando el campo "materias" de cada curso.
    """
    try:
        f = open("jsons/materias_json", mode="r", encoding="utf-8")
        materias = json.load(f)
        f.close()

        f = open("jsons/cursos_json", mode="r", encoding="utf-8")
        cursos = json.load(f)
        f.close()

        for i in materias:
            for j in cursos:
                if str(materias[i]["curso"]) == j:
                    if materias[i]["materia_nombre"] not in cursos[j]["materias"]:
                        cursos[j]["materias"].append(materias[i]["materia_nombre"])

        f = open("jsons/cursos_json", mode="w", encoding="utf-8")
        json.dump(cursos, f, indent=4, ensure_ascii=False)
        f.close()
    except ValueError:
        print("Valor ingresado no válido, intente de nuevo")
    except FileNotFoundError:
        print(f"Archivo no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo.")


def men_2(a):
    """
    Muestra un menú con opciones relacionadas a una entidad específica.
    """
    # Muestra las opciones disponibles para la entidad seleccionada.
    opciones = [f"[1] Ingresar {a} nuevos", f"[2] Baja de {a}", f"[3] Alta de {a}",
                f"[4] Modificar {a}", f"[5] Ver {a}", f"[0] Atras"]
    for i in opciones:
        print(i)


def obtener_nombre_diccionario(diccionario):
    """
    Devuelve el nombre de un diccionario global en formato de string.
    """
    # Itera sobre los diccionarios globales y devuelve el nombre del diccionario que coincida con el parámetro.
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
        f = open(f"jsons/{nombre_diccionario}_json", mode="r", encoding="utf-8")
        data = json.load(f)
        f.close()

        while True:
            # Solicita el ID del objeto a eliminar.
            id_eliminar = int(input(f"Ingrese el id del {nombre_diccionario} a dar de baja: "))
            if str(id_eliminar) not in data:
                print("ID no encontrado, intente de nuevo")
                continue
            # Confirma la eliminación y actualiza el estado.
            if input(f"Está seguro que desea eliminar {data[str(id_eliminar)]}? [S/N]: ").lower() == "s":
                data[str(id_eliminar)]["estado"] = False
                with open(f"jsons/{nombre_diccionario}_json", mode="w", encoding="utf-8") as f:
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
        print(f"Archivo jsons/{nombre_diccionario}_json no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo jsons/{nombre_diccionario}_json.")


def alta(nombre_diccionario):
    """
    Marca como activo (estado=True) un elemento previamente inactivo en un archivo JSON, basado en su ID.
    """
    try:
        f = open(f"jsons/{nombre_diccionario}_json", mode="r", encoding="utf-8")
        data = json.load(f)
        f.close()
        while True:
            # Solicita el ID del objeto a activar.
            id_alta = int(input(f"Ingrese el id del {nombre_diccionario} a dar de alta: "))
            if str(id_alta) not in data:
                print("ID no encontrado, intente de nuevo")
                continue
             # Confirma la eliminación y actualiza el estado.
            if input(f"Está seguro que desea dar de alta {data[str(id_alta)]}? [S/N]: ").lower() == "s":
                data[str(id_alta)]["estado"] = True
                with open(f"jsons/{nombre_diccionario}_json", mode="w", encoding="utf-8") as f:
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
        f = open(f"jsons/{nombre_diccionario}_json", mode="r", encoding="utf-8")
        data = json.load(f)
        f.close()

        while True:
            # Solicita el ID del objeto a modificar y el campo a modificar.
            id_modificar = int(input(f"Ingrese el id del {nombre_diccionario} a modificar: "))
            if str(id_modificar) not in str(data):
                print("ID no encontrado, intente de nuevo")
                continue
            campo = input(f"Ingrese el campo a modificar: {list(data[str(id_modificar)].keys())} - ")
            # Modifica el campo y actualiza el archivo JSON.
            if campo in data[str(id_modificar)]:
                data[str(id_modificar)][campo] = input("Ingrese el nuevo valor: ")
                print(f"Objeto modificado: {data[str(id_modificar)]}")
            else:
                print("Campo inválido, intente de nuevo")
            with open(f"jsons/{nombre_diccionario}_json", mode="w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
                f.close()
            break
    except ValueError:
        print("Valor ingresado no válido, intente de nuevo")
    except FileNotFoundError:
        print(f"Archivo no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo.")


def buscar(a):
    """
    Busca e imprime un elemento de un diccionario por su ID, verificando su estado.
    """
    # Solicita el ID a buscar y muestra el resultado.
    print_dict(a)
    id_buscar = input("Ingrese ID a buscar: ")
    print(f"Su búsqueda devolvió:\n{a.get(id_buscar)}")


def agregar(nombre_diccionario):
    """
    Agrega un nuevo elemento a un archivo JSON, inicializando sus campos y asignando 'estado=True'.
    """
    try:
        f = open(f"jsons/{nombre_diccionario}_json", mode="r", encoding="utf-8")
        data = json.load(f)
        f.close()
        # Solicita los datos del nuevo elemento y los agrega al archivo JSON.
        while True:
            id_agregar = str(len(data) + 1)
            data[id_agregar] = {}
            data[id_agregar]["estado"] = True
            print(f"Datos actuales: {data[id_agregar]}")
            # Solicita los datos del nuevo elemento.
            campo = input(f"Ingrese campo nuevo o 'salir': ").strip().lower()
            if campo == "salir":
                with open(f"jsons/{nombre_diccionario}_json", mode="w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                    f.close()
                    break
            valor = input(f"Valor para {campo}: ").strip()
            data[id_agregar][campo] = valor
    except ValueError:
        print("Valor ingresado no válido, intente de nuevo")
    except FileNotFoundError:
        print(f"Archivo no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo.")


def repetir(a):
    """
    Pregunta al usuario si desea realizar otra acción; finaliza el programa si la respuesta es negativa.
    """
    respuesta = input("Desea realizar otra acción? [S/N]: ").lower()
    if respuesta != "s":
        salir()
    else:
        men_2(a)


def generar_gmail(nombre_diccionario):
    """
    Genera correos electrónicos para todos los elementos de un archivo JSON, basándose en sus nombres y apellidos.
    """
    try:
        f = open(f"jsons/{nombre_diccionario}_json", mode="r", encoding="utf-8")
        data = json.load(f)
        f.close()
        # Itera sobre los elementos del archivo JSON y genera un correo para cada uno.
        for i in data:
            if data[i]["estado"]:
                nombre = data[i]["nombre"].replace(" ", "").lower()
                apellido = data[i]["apellido"].replace(" ", "").lower()
                data[i]["correo"] = f"{nombre}{apellido}@gmail.com"
        with open(f"jsons/{nombre_diccionario}_json", mode="w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            f.close()
    except ValueError:
        print("Valor ingresado no válido, intente de nuevo")
    except FileNotFoundError:
        print(f"Archivo no encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo.")

def llamados_principales():
    """
    Ejecuta las funciones principales del programa para realizar asignaciones iniciales y generar correos.
    """
    Asignacion()
    asignacion_2()
    asignacion_3()
    generar_gmail("alumnos")
    generar_gmail("profesores")

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
