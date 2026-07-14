
planes = {
    "F001":["Plan basico", "Mensual", 1, False, False, "Libre"],
    "F002":["Plan Full", "Mensual", 1, True, True, "Libre"],
    "F003":["Plan de Estudiante", "Trimestral", 3, False, True, "Tarde"]
}

inscripciones = {
    "F001": [14990, 30],
    "F002": [18990, 10],
    "F003": [22990, 20]
}

def num_positivo(msg):
    while True:
        try:
            opcion = int(input(msg))
            if opcion >= 0:
                return
            else:
                print("Debe ingresar un valor positivo, no puede ingresar 0 o numeros negativos.")
        except:
            print("Error, ingrese solamente valores de tipo numerico.")

def validar_opcion(msg, min, max):
    while True:
        try:
            opcion = int(input(msg))
            if opcion < min or opcion > max:
                print("Valor fuera de rango, porfavor elija una opcion dentro del rango.")
            else:
                return opcion
        except:
            print("Error, porfavor ingrese solamente valores del tipo numerico.")

def Cupos_por_tipo_de_plan():
    plan = input("Ingrese el tipo de plan: ")
    if plan.lower() == "mensual":
        for k, v in planes.items():
            if v[1] == "Mensual":
                print("")
                print(v[0], "Plan de tipo:", v[1], "Duracion (meses):", v[2], "Acceso a piscina:", v[3], "Incluye clases:", v[4], "Horario:", v[5])
                print("Valor de inscripcion:", inscripciones[k][0])
                print("Cupos disponibles:", inscripciones[k][1])
            else:
                None
    
    elif plan.lower() == "trimestral":
        for k, v in planes.items():
            if v[1] == "Trimestral":
                print("")
                print(v[0], "Plan de tipo:", v[1], "Duracion (meses):", v[2], "Acceso a piscina:", v[3], "Incluye clases:", v[4], "Horario:", v[5])
                print("Valor de inscripcion:", inscripciones[k][0])
                print("Cupos disponibles:", inscripciones[k][1])
            else:
                None

    elif plan.lower() == "anual":
        for k, v in planes.items():
            if v[1] == "Anual":
                print("")
                print(v[0], "Plan de tipo:", v[1], "Duracion (meses):", v[2], "Acceso a piscina:", v[3], "Incluye clases:", v[4], "Horario:", v[5])
                print("Valor de inscripcion:", inscripciones[k][0])
                print("Cupos disponibles:", inscripciones[k][1])
            else:
                None
    
    else:
        print("No se ha podido encontrar el tipo de plan que buscas, porfavor ingrese uno de los planes posiblemente registrados (Mensual, Trimestral o Anual)")

def Busqueda_Segun_precio():
    minimo = num_positivo("Ingrese el minimo de su rango a buscar: ")
    maximo = num_positivo("Ingrese el maximo de su rango a buscar: ")

    lista_vacia = []

    for k, v in inscripciones.items():
        if v[0] <= maximo and k >= minimo and k[1] > 0:
            lista_vacia.append(k, v)
        else:
            None
    
    print(lista_vacia)

    lista_vacia.clear()




                




def menu():
    while True:
        print("""
========== MENÚ PRINCIPAL ==========
1. Cupos por tipo de plan
2. Búsqueda de planes por rango de precio
3. Actualizar precio de plan
4. Agregar plan
5. Eliminar plan
6. Salir
=====================================
    """)
        opcion = validar_opcion("Elija una opcion: ", 1, 6)

        if opcion == 1:
            Cupos_por_tipo_de_plan()
        elif opcion == 3:
            None
            
            

menu()