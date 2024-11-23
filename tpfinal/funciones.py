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
    Imprime un diccionario en formato de una sola línea, de manera legible.
    Args:
        a (dict): Diccionario que contiene las entidades a imprimir.
    Funcionamiento:
        - Itera sobre cada elemento del diccionario.
        - Si el estado de la entidad es `True`, imprime sus valores en una sola línea.
        - Cada campo de la entidad es presentado con su nombre capitalizado.
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
    Asigna la cantidad de alumnos a cada curso según su `curso_id`.

    Args:
        alumnos (dict): Diccionario que contiene a los alumnos.
        cursos (dict): Diccionario que contiene los cursos.

    Returns:
        dict: El diccionario de cursos actualizado con la cantidad de alumnos asignados a cada curso.

    Funcionamiento:
        - Cuenta cuántos alumnos están asignados a cada curso según el campo `curso_id`.
        - Actualiza el campo `alumnos` de cada curso con la cantidad correspondiente.
    """
    f=open("jsons/alumnos_json", mode="r", encoding="utf-8")
    alumnos=json.load(f)
    f.close()

    f=open("jsons/cursos_json", mode="r", encoding="utf-8")
    cursos=json.load(f)
    f.close()

    for i in cursos:
        cont_curso = 0
        for j in alumnos:
            if str(alumnos[j]["curso_id"]) == i:
                cont_curso += 1
        cursos[i]["alumnos"] = cont_curso  


    f=open("jsons/cursos_json", mode="w", encoding="utf-8")
    json.dump(cursos, f, indent=4, ensure_ascii=False)
    f.close()
    

def asignacion_2():
    """Funcion para vincular el nombre y apellido de un profesor a la lista (profesor) de una materia"""
    f=open("jsons/materias_json", mode="r", encoding="utf-8")
    materias=json.load(f)
    f.close()

    f=open("jsons/profesores_json", mode="r", encoding="utf-8")
    profesores=json.load(f)
    f.close()

    for i in materias:
        for j in profesores:
            if int(i) in profesores[j]["materias"]:
                if len(materias[i]["profesor"]) == 0:
                    materias[i]["profesor"].append(profesores[j]["nombre"]+" "+profesores[j]["apellido"])
    
    f=open("jsons/materias_json", mode="w", encoding="utf-8")
    json.dump(materias, f, indent=4, ensure_ascii=False)
    f.close()

def asignacion_3():
    """
    Vincula el nombre de cada materia con el curso al que pertenece.

    Args:
        materias (dict): Diccionario que contiene las materias.
        cursos (dict): Diccionario que contiene los cursos.

    Returns:
        dict: Diccionario de cursos actualizado con las materias asociadas.

    Funcionamiento:
        - Itera sobre las materias y encuentra el curso correspondiente.
        - Añade el nombre de la materia a la lista de `materias` del curso.
    """
    f=open("jsons/materias_json", mode="r", encoding="utf-8")
    materias=json.load(f)
    f.close()

    f=open("jsons/cursos_json", mode="r", encoding="utf-8")
    cursos=json.load(f)
    f.close()

    for i in materias:
        for j in cursos:
            if str(materias[i]["curso"]) == j:
                cursos[j]["materias"].append(materias[i]["materia_nombre"])

    f=open("jsons/cursos_json", mode="w", encoding="utf-8")
    json.dump(cursos, f, indent=4, ensure_ascii=False)
    f.close()

def men_2(a):
    """
    Imprime un submenú para gestionar una entidad.

    Args:
        a (str): Nombre de la entidad a gestionar.

    Funcionamiento:
        - Genera un menú de opciones específicas para la entidad proporcionada.
        - Imprime las opciones numeradas del submenú.
    """
    opciones = [f"[1] Ingresar {a} nuevos", f"[2] Baja de {a}", f"[3] Alta de {a}",
                f"[4] Modificar {a}", f"[5] Ver {a}", f"[0] Atras"]
    for i in opciones:
        print(i)


def obtener_nombre_diccionario(diccionario):
    """
    Obtiene el nombre de la variable que contiene un diccionario específico.

    Args:
        diccionario (dict): Diccionario del cual se desea conocer el nombre.

    Returns:
        str: Nombre de la variable que contiene el diccionario, o `None` si no se encuentra.
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
    Marca un objeto como eliminado cambiando su estado a `False`.

    Args:
        a (dict): Diccionario que contiene la entidad a gestionar.
        nombre_diccionario (str): Nombre del diccionario para identificar el archivo JSON.

    Funcionamiento:
        - Solicita el ID del objeto a eliminar.
        - Cambia el estado del objeto a `False` si se confirma la eliminación.-
    """
    try:
        f = open(f"jsons/{nombre_diccionario}_json", mode="r", encoding="utf-8")
        data = json.load(f)
        f.close()

        while True:
            id_eliminar = int(input(f"Ingrese el id del {nombre_diccionario} a dar de baja: "))
            if str(id_eliminar) not in data:
                print("ID no encontrado, intente de nuevo")
                continue

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
    Marca un objeto como activo cambiando su estado a `True`.

    Args:
        a (dict): Diccionario que contiene la entidad a gestionar.

    Funcionamiento:
        - Solicita el ID del objeto a activar.
        - Cambia el estado del objeto a `True` si se confirma la activación.
    """
    try:
        f = open(f"jsons/{nombre_diccionario}_json", mode="r", encoding="utf-8")
        data = json.load(f)
        f.close()
        while True:
            id_alta = int(input(f"Ingrese el id del {nombre_diccionario} a dar de alta: "))
            if str(id_alta) not in data:
                print("ID no encontrado, intente de nuevo")
                continue

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
    Modifica un campo de un objeto específico dentro de una entidad.

    Args:
        a (dict): Diccionario que contiene la entidad a gestionar.

    Funcionamiento:
        - Solicita el ID del objeto a modificar.
        - Permite seleccionar un campo y asignar un nuevo valor al mismo.
    """
    try:
        f =open(f"jsons/{nombre_diccionario}_json", mode="r", encoding="utf-8")
        data = json.load(f)
        f.close()


        while True:
            id_modificar = int(input(f"Ingrese el id del {nombre_diccionario} a modificar: "))
            if str(id_modificar) not in str(data):
                print("ID no encontrado, intente de nuevo")
                continue
            campo = input(f"Ingrese el campo a modificar: {list(data[str(id_modificar)].keys())} - ")
            if campo in data[str(id_modificar)]:
                data[str(id_modificar)][campo] = input("Ingrese el nuevo valor: ")
                print(f"Objeto modificado: {data[str(id_modificar)]}")
            else:
                print("Campo inválido, intente de nuevo")

            with open(f"jsons/{nombre_diccionario}_json",mode="w", encoding="utf-8") as f:
                json.dump(data,f,ensure_ascii=False, indent=4)
                f.close()
            
    except ValueError:
        print("Valor ingresado no válido, intente de nuevo")

def buscar(a: dict):
    """
    Busca un objeto dentro de una entidad por su ID.

    Args:
        a (dict): Diccionario que contiene la entidad a buscar.

    Funcionamiento:
        - Solicita el ID del objeto que se desea buscar.
        - Muestra la información del objeto si existe y está activo.
        - Informa si el objeto no está activo o no se encuentra.
    """
    try:
        while True:
            id_buscar = int(input(f"Ingrese el id del {obtener_nombre_diccionario(a)} a buscar: "))
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


def agregar(nombre_diccionario):
    """
    Agrega un nuevo objeto a una entidad.

    Args:
        a (dict): Diccionario que contiene la entidad a la que se añadirá un objeto.

    Funcionamiento:
        - Solicita valores para los campos del nuevo objeto.
        - Genera automáticamente valores predeterminados para campos específicos.
        - Añade el nuevo objeto al diccionario con una clave única.
    """
    try:
        f=open(f"jsons/{nombre_diccionario}_json", mode="r", encoding="utf-8")
        a=json.load(f)
        f.close()
        lista_claves = []
        nuevo_a = {}
        for valor, clave in a.items():
            for j in clave:
                lista_claves.append(j)
            break
        for i in lista_claves:
            if i == "profesor" or i == "materias" or i == "gmail" or i=="alumnos" or i=="estado":
                nuevo_a[i] = ""
            else:
                nuevo_a[i] = input(f"Ingrese el nuevo {i}: ")
        nuevo_a["estado"] = True
        a[len(a)] = nuevo_a
        llamados_principales()
        
        f=open(f"jsons/{nombre_diccionario}_json", mode="w", encoding="utf-8")
        json.dump(a,f, indent=4, ensure_ascii=False)
        f.close()
    except ValueError:
        print("Valor ingresado no válido, intente de nuevo")


def repetir(a):
    """
    Solicita al usuario si desea realizar otra acción.

    Args:
        a (dict): Diccionario que representa la entidad a gestionar.

    Funcionamiento:
        - Pregunta si el usuario desea continuar.
        - Finaliza el programa o regresa al flujo principal según la respuesta.
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
#     """
#     Genera automáticamente correos electrónicos para profesores o alumnos.

#     Args:
#         a (dict): Diccionario que contiene los objetos para los cuales se generarán los correos.

#     Returns:
#         dict: Diccionario actualizado con los correos generados.

#     Funcionamiento:
#         - Asigna un dominio específico según la entidad (profesores o alumnos).
#         - Construye el correo concatenando la inicial del nombre y el apellido en minúsculas.
#     """

    f = open(f"jsons/{nombre_diccionario}_json", mode="r",encoding="utf-8")
    data = json.load(f)
    f.close()

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


    f = open(f"jsons/{nombre_diccionario}_json", mode="w", encoding="utf-8")
    json.dump(data,f,indent=4, ensure_ascii=False)
    f.close()

def llamados_principales():
    """
    Ejecuta las funciones necesarias para inicializar los datos y asignaciones del programa.

    Funcionamiento:
        - Realiza asignaciones de alumnos a cursos.
        - Vincula profesores y materias a cursos.
        - Genera correos electrónicos para profesores y alumnos.
    """
    Asignacion()
    asignacion_2()
    asignacion_3()
    generar_gmail(alumnos)
    generar_gmail(profesores)

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
