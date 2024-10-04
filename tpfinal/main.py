import random

alumnos={ 
        1:{"id": 0 , "nombre": "Santiago", "apellido": "Pérez", "curso_id": 3},
        2:{"id": 0 ,"nombre": "María", "apellido": "González", "curso_id": 6},
        3:{"id": 0 ,"nombre": "José", "apellido": "López", "curso_id": 6}
         }

profesores={ 
        1:{"id": 0 , "nombre": "Santiago", "apellido": "Pérez", "materias": [5,6,7,8]},
        2:{"id": 0 ,"nombre": "María", "apellido": "González", "materias": [5,6,7,8]},
        3:{"id": 0 ,"nombre": "José", "apellido": "López", "materias": [5,6,7,8]}
         }

cursos={
    1:{"curso_id":3, "curso_nombre":"primero A", "alumnos":0, "materias": [1,2,3,4]},
    2:{"curso_id":6, "curso_nombre":"primero A", "alumnos":0, "materias":[5,6,7,8]}
    }

Materias={
    1:{"materia_id":3, "curso_nombre":"geografia", "profesor":0, "materias": [1,2,3,4]},
    2:{"materia":6, "curso_nombre":"historia", "profesor":0, "materias":[5,6,7,8]}
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
    
id_loop(alumnos)
id_loop(profesores)
Asignacion(alumnos, cursos)
print_dict(cursos)