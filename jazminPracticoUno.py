
def notas_por_materia ():
    materias = ["lengua", "ed_fisica", "matematicas", "biologia", "geografia", "club_arte", "ed_artistica",
                        "historia", "club_deportes", "programacion", "estructuras", "diseño_interfaces", "ingles",
                        "tia", "club_ciencias", "fvt" ]
  notas = {
    "lengua": [],
        "ed_fisica": [],
        "matematicas": [],
        "biologia": [],
        "geografia": [],
        "club_arte": [],
        "ed_artistica": [],
        "historia": [],
        "club_deportes": [],
        "programacion": [],
        "estructuras": [],
        "diseño_interfaces": [],
        "ingles": [],
        "tia": [],
        "club_ciencias": [],
        "fvt": []
    }
    for materia in materias:
        nota = int(input("ingrese la nota de la materia"{materia}":"))
        if  0 <= nota <= 10:
            notas[materia].append(nota)
            #si la nota es mayor a 0 y menor a 10 esta se agrega a la materia, 
            #si no, le dice:
        else:
            print("La nota ingresada no es válida. Debe estar entre 0 y 10.")
