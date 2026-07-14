
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
        
menu()