def notas_por_materia():
    materias = ["lengua", "ed_fisica", "matematicas", "biologia", "geografia", "club_arte", "ed_artistica",
                "historia", "club_deportes", "programacion", "estructuras", "diseño_interfaces", "ingles",
                "tia", "club_ciencias", "fvt"]
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
    for materia in materias:  # este bucle for  va a recorrer las materias en (la lista) materias
        print(f"\nIngresando notas para la materia: {materia}")
        for i in range(3):    # este bucle for va a recorrer los valores de las  claves en notas
            while True:
                nota_str = input(f"Ingrese la nota {i+1} de la materia {materia}: ")
                es_entero = True
                for caracter in nota_str:
                    if not '0' <= caracter <= '9':
                        es_entero = False
                        break
                if es_entero:
                    if nota_str:    # Asegurarse de que la cadena no esté vacía
                        nota = int(nota_str)
                        if 0 <= nota <= 10:
                            notas[materia].append(nota)
                            break
                        else:
                            print("La nota ingresada no es válida. Debe estar entre 0 y 10.")
                    else:
                        print("Error: Por favor, ingrese un número entero válido.")
                else:
                    print("Error: Por favor, ingrese un número entero válido.")

    print("\n--- Resultados por Materia ---")
    for materia, lista_notas in notas.items():
        if lista_notas:
            promedio_materia = sum(lista_notas) / len(lista_notas)
            aprobado = "Aprobado" if promedio_materia >= 7 else "Desaprobado"
            print(f"{materia}: Promedio = {promedio_materia:.2f} - {aprobado}")
        else:
            print(f"{materia}: No se ingresaron notas.")

# Llamamos a la función para ejecutar el programa
notas_por_materia()