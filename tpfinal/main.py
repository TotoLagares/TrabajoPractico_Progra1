import random

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
    1:{"curso_id":1, "curso_nombre":"primero A", "alumnos":0, "materias": []},
    2:{"curso_id":2, "curso_nombre":"primero A", "alumnos":0, "materias":[]}
    }

materias={
    1:{"materia_id":3, "curso_nombre":"geografia", "profesor":[], "curso": 1},
    2:{"materia_id":6, "curso_nombre":"historia", "profesor":[], "curso":1}
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
            if cursos[i]["curso_id"]==alumnos[j]["curso_id"]:
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
            if materias[i]["curso"] == cursos[j]["curso_id"]:
                cursos[j]["materias"].append(materias[i]["materia_id"])
    return cursos


def main():
    opciones = ["1- Alumnos", "2- Profesores", "3- Cusos", "4- Materias", "0- Salir"]
    for opcion in opciones:
        print(opcion)

id_loop(alumnos)
id_loop(profesores)
Asignacion(alumnos, cursos)
asignacion_2(materias, profesores, "materia_id","materias","profesor","id")
asignacion_3(materias, cursos)
print_dict(cursos)
print_dict(materias)
main()