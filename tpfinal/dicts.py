import json

alumnos = {
    0: {'nombre': 'Sofía', 'apellido': 'González', 'curso_id': 0, 'gmail': '', 'telefono': '+54 11 12345678', 'estado': True},
    1: {'nombre': 'Lucas', 'apellido': 'López', 'curso_id': 0, 'gmail': '', 'telefono': '+54 11 23456789', 'estado': True},
    2: {'nombre': 'Martín', 'apellido': 'Pérez', 'curso_id': 1, 'gmail': '', 'telefono': '+54 11 34567890', 'estado': True},
    3: {'nombre': 'Ana', 'apellido': 'Martínez', 'curso_id': 1, 'gmail': '', 'telefono': '+54 11 45678901', 'estado': True},
    4: {'nombre': 'Valentina', 'apellido': 'Ramírez', 'curso_id': 2, 'gmail': '', 'telefono': '+54 11 56789012', 'estado': True},
    5: {'nombre': 'Diego', 'apellido': 'Hernández', 'curso_id': 2, 'gmail': '', 'telefono': '+54 11 67890123', 'estado': True},
    6: {'nombre': 'Camila', 'apellido': 'Torres', 'curso_id': 3, 'gmail': '', 'telefono': '+54 11 78901234', 'estado': True},
    7: {'nombre': 'Javier', 'apellido': 'Sánchez', 'curso_id': 3, 'gmail': '', 'telefono': '+54 11 89012345', 'estado': True},
    8: {'nombre': 'Laura', 'apellido': 'Molina', 'curso_id': 4, 'gmail': '', 'telefono': '+54 11 90123456', 'estado': True},
    9: {'nombre': 'Felipe', 'apellido': 'Cruz', 'curso_id': 4, 'gmail': '', 'telefono': '+54 11 01234567', 'estado': True},
    10: {'nombre': 'Nicolás', 'apellido': 'Jiménez', 'curso_id': 0, 'gmail': '', 'telefono': '+54 11 12345678', 'estado': True},
    11: {'nombre': 'Lucía', 'apellido': 'Salazar', 'curso_id': 0, 'gmail': '', 'telefono': '+54 11 23456789', 'estado': True},
    12: {'nombre': 'Andrés', 'apellido': 'Morales', 'curso_id': 1, 'gmail': '', 'telefono': '+54 11 34567890', 'estado': True},
    13: {'nombre': 'Isabella', 'apellido': 'Vargas', 'curso_id': 1, 'gmail': '', 'telefono': '+54 11 45678901', 'estado': True},
    14: {'nombre': 'Gabriel', 'apellido': 'Aguilar', 'curso_id': 2, 'gmail': '', 'telefono': '+54 11 56789012', 'estado': True},
    15: {'nombre': 'Renata', 'apellido': 'Ponce', 'curso_id': 2, 'gmail': '', 'telefono': '+54 11 67890123', 'estado': True},
    16: {'nombre': 'Esteban', 'apellido': 'Salas', 'curso_id': 3, 'gmail': '', 'telefono': '+54 11 78901234', 'estado': True},
    17: {'nombre': 'Samantha', 'apellido': 'Mendoza', 'curso_id': 3, 'gmail': '', 'telefono': '+54 11 89012345', 'estado': True},
    18: {'nombre': 'Hugo', 'apellido': 'Córdoba', 'curso_id': 4, 'gmail': '', 'telefono': '+54 11 90123456', 'estado': True},
    19: {'nombre': 'Valeria', 'apellido': 'Ríos', 'curso_id': 4, 'gmail': '', 'telefono': '+54 11 01234567', 'estado': True},
    20: {'nombre': 'Joaquín', 'apellido': 'Alvarado', 'curso_id': 0, 'gmail': '', 'telefono': '+54 11 12345678', 'estado': True},
    21: {'nombre': 'Martina', 'apellido': 'Benítez', 'curso_id': 0, 'gmail': '', 'telefono': '+54 11 23456789', 'estado': True},
    22: {'nombre': 'Natalia', 'apellido': 'Rincón', 'curso_id': 1, 'gmail': '', 'telefono': '+54 11 34567890', 'estado': True},
    23: {'nombre': 'Camilo', 'apellido': 'Alvarado', 'curso_id': 1, 'gmail': '', 'telefono': '+54 11 45678901', 'estado': True},
    24: {'nombre': 'Ángela', 'apellido': 'Paz', 'curso_id': 0, 'gmail': '', 'telefono': '+54 11 56789012', 'estado': True},
    25: {'nombre': 'Sebastián', 'apellido': 'Hernández', 'curso_id': 1, 'gmail': '', 'telefono': '+54 11 67890123', 'estado': True},
    26: {'nombre': 'Lucía', 'apellido': 'Salas', 'curso_id': 2, 'gmail': '', 'telefono': '+54 11 78901234', 'estado': True},
    27: {'nombre': 'Ricardo', 'apellido': 'Torres', 'curso_id': 3, 'gmail': '', 'telefono': '+54 11 89012345', 'estado': True},
    28: {'nombre': 'Fernanda', 'apellido': 'Cruz', 'curso_id': 4, 'gmail': '', 'telefono': '+54 11 90123456', 'estado': True},
    29: {'nombre': 'Diego', 'apellido': 'Jiménez', 'curso_id': 0, 'gmail': '', 'telefono': '+54 11 01234567', 'estado': True}
}


profesores = {
    0: {"nombre": "Santiago", "apellido": "Pérez", "materias": [1, 9, 19], "telefono": "+54 11 12345678", "gmail": "", "estado": True},
    1: {"nombre": "María", "apellido": "López", "materias": [2, 10, 20], "telefono": "+54 11 23456789", "gmail": "", "estado": True},
    2: {"nombre": "Carlos", "apellido": "García", "materias": [3, 11, 21], "telefono": "+54 11 34567890", "gmail": "", "estado": True},
    3: {"nombre": "Ana", "apellido": "Fernández", "materias": [4, 12, 22], "telefono": "+54 11 45678901", "gmail": "", "estado": True},
    4: {"nombre": "Javier", "apellido": "Martínez", "materias": [5, 15, 25], "telefono": "+54 11 56789012", "gmail": "", "estado": True},
    5: {"nombre": "Lucía", "apellido": "Gómez", "materias": [6, 16, 26], "telefono": "+54 11 67890123", "gmail": "", "estado": True},
    6: {"nombre": "Ricardo", "apellido": "Sánchez", "materias": [7, 17, 27], "telefono": "+54 11 78901234", "gmail": "", "estado": True},
    7: {"nombre": "Paola", "apellido": "Ramírez", "materias": [8, 18, 28], "telefono": "+54 11 89012345", "gmail": "", "estado": True},
    8: {"nombre": "Diego", "apellido": "Torres", "materias": [29, 31, 41], "telefono": "+54 11 90123456", "gmail": "", "estado": True},
    9: {"nombre": "Valentina", "apellido": "Hernández", "materias": [30, 32, 42], "telefono": "+54 11 01234567", "gmail": "", "estado": True},
    10: {"nombre": "Fernando", "apellido": "Alvarez", "materias": [33, 34, 44], "telefono": "+54 11 12345678", "gmail": "", "estado": True},
    11: {"nombre": "Natalia", "apellido": "Benítez", "materias": [35, 36, 45], "telefono": "+54 11 23456789", "gmail": "", "estado": True},
    12: {"nombre": "Emilio", "apellido": "Castro", "materias": [37, 38, 46], "telefono": "+54 11 34567890", "gmail": "", "estado": True},
    13: {"nombre": "Camila", "apellido": "Ríos", "materias": [39, 40, 47], "telefono": "+54 11 45678901", "gmail": "", "estado": True},
    14: {"nombre": "Gabriel", "apellido": "Ponce", "materias": [41, 42, 48], "telefono": "+54 11 56789012", "gmail": "", "estado": True}
}
cursos={
    0: {"curso_nombre": "Primer Año", "materias": [], "alumnos": 0, "estado": True},
    1: { "curso_nombre": "Segundo Año", "materias": [], "alumnos": 0, "estado": True},
    2: {"curso_nombre": "Tercer Año", "materias": [], "alumnos": 0, "estado": True},
    3: {"curso_nombre": "Cuarto Año", "materias": [], "alumnos": 0, "estado": True},
    4: {"curso_nombre": "Quinto Año", "materias": [], "alumnos": 0, "estado": True},
}
materias= {
    1: {"materia_nombre": "Lengua y Literatura I", "profesor": [], "curso": 0, "estado": True},
    2: {"materia_nombre": "Matemática I", "profesor": [], "curso": 0, "estado": True},
    3: {"materia_nombre": "Ciencias Sociales I", "profesor": [], "curso": 0, "estado": True},
    4: {"materia_nombre": "Ciencias Naturales I", "profesor": [], "curso": 0, "estado": True},
    5: {"materia_nombre": "Educación Física I", "profesor": [], "curso": 0, "estado": True},
    6: {"materia_nombre": "Inglés I", "profesor": [], "curso": 0, "estado": True},
    7: {"materia_nombre": "Tecnología I", "profesor": [], "curso": 0, "estado": True},
    8: {"materia_nombre": "Arte I", "profesor": [], "curso": 0, "estado": True},
    9: {"materia_nombre": "Lengua y Literatura II", "profesor": [], "curso": 1, "estado": True},
    10: {"materia_nombre": "Matemática II", "profesor": [], "curso": 1, "estado": True},
    11: {"materia_nombre": "Historia I", "profesor": [], "curso": 1, "estado": True},
    12: {"materia_nombre": "Geografía I", "profesor": [], "curso": 1, "estado": True},
    13: {"materia_nombre": "Biología I", "profesor": [], "curso": 1, "estado": True},
    14: {"materia_nombre": "Química I", "profesor": [], "curso": 1, "estado": True},
    15: {"materia_nombre": "Educación Física II", "profesor": [], "curso": 1, "estado": True},
    16: {"materia_nombre": "Inglés II", "profesor": [], "curso": 1, "estado": True},
    17: {"materia_nombre": "Tecnología II", "profesor": [], "curso": 1, "estado": True},
    18: {"materia_nombre": "Arte II", "profesor": [], "curso": 1, "estado": True},
    19: {"materia_nombre": "Lengua y Literatura III", "profesor": [], "curso": 2, "estado": True},
    20: {"materia_nombre": "Matemática III", "profesor": [], "curso": 2, "estado": True},
    21: {"materia_nombre": "Historia II", "profesor": [], "curso": 2, "estado": True},
    22: {"materia_nombre": "Geografía II", "profesor": [], "curso": 2, "estado": True},
    23: {"materia_nombre": "Física I", "profesor": [], "curso": 2, "estado": True},
    24: {"materia_nombre": "Química II", "profesor": [], "curso": 2, "estado": True},
    25: {"materia_nombre": "Educación Física III", "profesor": [], "curso": 2, "estado": True},
    26: {"materia_nombre": "Inglés III", "profesor": [], "curso": 2, "estado": True},
    27: {"materia_nombre": "Tecnología III", "profesor": [], "curso": 2, "estado": True},
    28: {"materia_nombre": "Arte III", "profesor": [], "curso": 2, "estado": True},
    29: {"materia_nombre": "Lengua y Literatura IV", "profesor": [], "curso": 3, "estado": True},
    30: {"materia_nombre": "Matemática IV", "profesor": [], "curso": 3, "estado": True},
    31: {"materia_nombre": "Historia III", "profesor": [], "curso": 3, "estado": True},
    32: {"materia_nombre": "Geografía III", "profesor": [], "curso": 3, "estado": True},
    33: {"materia_nombre": "Biología II", "profesor": [], "curso": 3, "estado": True},
    34: {"materia_nombre": "Física II", "profesor": [], "curso": 3, "estado": True},
    35: {"materia_nombre": "Química III", "profesor": [], "curso": 3, "estado": True},
    36: {"materia_nombre": "Educación Física IV", "profesor": [], "curso": 3, "estado": True},
    37: {"materia_nombre": "Inglés IV", "profesor": [], "curso": 3, "estado": True},
    38: {"materia_nombre": "Tecnología IV", "profesor": [], "curso": 3, "estado": True},
    39: {"materia_nombre": "Arte IV", "profesor": [], "curso": 3, "estado": True},
    40: {"materia_nombre": "Lengua y Literatura V", "profesor": [], "curso": 4, "estado": True},
    41: {"materia_nombre": "Matemática V", "profesor": [], "curso": 4, "estado": True},
    42: {"materia_nombre": "Historia IV", "profesor": [], "curso": 4, "estado": True},
    43: {"materia_nombre": "Geografía IV", "profesor": [], "curso": 4, "estado": True},
    44: {"materia_nombre": "Ciencias Naturales I", "profesor": [], "curso": 4, "estado": True},
    45: {"materia_nombre": "Orientación Vocacional I", "profesor": [], "curso": 4, "estado": True},
    46: {"materia_nombre": "Inglés V", "profesor": [], "curso": 4, "estado": True},
    47: {"materia_nombre": "Educación Física V", "profesor": [], "curso": 4, "estado": True},
    48: {"materia_nombre": "Tecnología V", "profesor": [], "curso": 4, "estado": True},
    49: {"materia_nombre": "Arte V", "profesor": [], "curso": 4, "estado": True},
}

f = open("alumnos_json", mode="w", encoding="utf-8")
json.dump(alumnos, f, ensure_ascii=False, indent=4)
f.close()

f = open("profesores_json", mode="w", encoding="utf-8")
json.dump(profesores, f, ensure_ascii=False, indent=4)
f.close()

f = open("cursos_json", mode="w", encoding="utf-8")
json.dump(cursos, f, ensure_ascii=False, indent=4)
f.close()

f = open("materias_json", mode="w", encoding="utf-8")
json.dump(materias, f, ensure_ascii=False, indent=4)
f.close()

