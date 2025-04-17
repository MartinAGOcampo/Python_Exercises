"""E
scribir un programa que permita gestionar la base de datos de alumnos del IFdeZ. 
Los alumnos se guardarán en un diccionario en el que la clave de cada uno de ellos será su DNI, y el valor será otro diccionario con los datos del alumno 
El programa debe preguntar al usuario por una opción del menú
En función de la opción elegida el programa tendrá que hacer lo siguiente:
• Opción (1): Preguntar los datos del alumno, crear un diccionario con los datos
y añadirlo a la base de datos.
• Opción (2): Preguntar por el DNI del alumno y eliminar sus datos de la base
de datos.
• Opción (3): Preguntar por el DNI del alumno y mostrar sus datos.
• Opción (4): Mostrar lista de todos los alumnos de la base datos con todos
sus datos en columnas.
• Opción (5): Terminar el programa
"""


# Funcion para agregar alumnos
def agregar_alumno(base_datos):
    dni = input("Ingrese el DNI del alumno: ")
    if dni in base_datos:
        print("El alumno con ese DNI ya existe.")
        return
    nombre = input("Ingrese el nombre del alumno: ")
    direccion = input("Ingrese la dirección del alumno: ")
    telefono = input("Ingrese el teléfono del alumno: ")
    correo = input("Ingrese el correo electrónico del alumno: ")
    base_datos[dni] = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono,
        "correo": correo
    }
    print("Alumno agregado exitosamente.")

# Funcion para eliminar alumnos 
def eliminar_alumno(base_datos):
    dni = input("Ingrese el DNI del alumno que desea eliminar: ")
    if dni in base_datos:
        del base_datos[dni]
        print("Alumno eliminado exitosamente.")
    else:
        print("No se encontró un alumno con ese DNI.")

# Funcion para mostrar alumnos
def mostrar_alumno(base_datos):
    dni = input("Ingrese el DNI del alumno que desea ver: ")
    if dni in base_datos:
        alumno = base_datos[dni]
        print(f"\nDatos del alumno con DNI {dni}:")
        for key, value in alumno.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("No se encontró un alumno con ese DNI.")

# Funcion para detallar alumnos
def listar_alumnos(base_datos):
    if not base_datos:
        print("No hay alumnos en la base de datos.")
        return
    print("\nLista de todos los alumnos:\n")
    for dni, datos in base_datos.items():
        print(f"DNI: {dni}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Dirección: {datos['direccion']}")
        print(f"Teléfono: {datos['telefono']}")
        print(f"Correo: {datos['correo']}")
        print("-" * 40)  # Separador entre alumnos

# Main
base_datos = {}
while True:
    print("\nMenú de opciones:")
    print("1. Agregar alumno")
    print("2. Eliminar alumno")
    print("3. Mostrar alumno")
    print("4. Listar todos los alumnos")
    print("5. Terminar")
    
    try:
        opcion = int(input("\nSelecciona una opción (1-5): "))
        
        if opcion == 1:
            agregar_alumno(base_datos)
        elif opcion == 2:
            eliminar_alumno(base_datos)
        elif opcion == 3:
            mostrar_alumno(base_datos)
        elif opcion == 4:
            listar_alumnos(base_datos)
        elif opcion == 5:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")
            
    except ValueError:
        print("Por favor, ingresa un número entero.")
