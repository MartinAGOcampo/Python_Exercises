"""Programar un script que pueda crear a partir de una lista o diccionario (como ud. lo
prefiera); un archivo llamado calificaciones.csv el cual contiene los datos personales y
las notas del Primer Parcial de al menos 10 (diez) alumnos de la materia Programación
II (DISTANCIA) del ISFdZ (se adjunta como ejemplo un archivo con la primera línea)."""

"""Construir una función que lea el archivo calificaciones.csv y devuelva un diccionario con
los datos del archivo por columnas."""

"""Construir una función que reciba el diccionario devuelto por la función anterior y cree un
archivo en formato txt denominado resumen.txt en donde deberá decir en la primera
línea “Resumen de Notas Primer Parcial Programación II”, además de los resultados de
la mínima, la máxima y el promedio de notas de todos los alumnos."""


import csv

# Funcion para crear el archivo CSV
def crear_archivo_csv():
    alumnos = [
        {"Nombre": "Juan Perez", "Nota": 7},
        {"Nombre": "Ana López", "Nota": 9},
        {"Nombre": "Carlos Martínez", "Nota": 8},
        {"Nombre": "Laura Gómez", "Nota": 6},
        {"Nombre": "Pedro Sánchez", "Nota": 7},
        {"Nombre": "Marta Torres", "Nota": 8},
        {"Nombre": "Luis Fernández", "Nota": 5},
        {"Nombre": "Sofía Ramírez", "Nota": 6},
        {"Nombre": "Diego Vargas", "Nota": 4},
        {"Nombre": "Camila Díaz", "Nota": 9},
    ]

    with open('calificaciones.csv', mode='w', newline='') as archivo_csv:
        campos = ["Nombre", "Nota"]
        escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
        
        escritor.writeheader()
        escritor.writerows(alumnos)

# Funcion para introducir los datos en un diccionario
def leer_archivo_csv():
    diccionario = {"Nombre": [], "Nota": []}

    with open('calificaciones.csv', mode='r') as archivo_csv:
        lector = csv.DictReader(archivo_csv)
        # Introducimos los datos
        for fila in lector:
            diccionario["Nombre"].append(fila["Nombre"])
            diccionario["Nota"].append(int(fila["Nota"]))

    return diccionario

# Funcion para crear el resumen .txt
def crear_resumen_txt(diccionario):
    notas = diccionario["Nota"]
    minima = min(notas)
    maxima = max(notas)
    promedio = sum(notas) // len(notas)  
    # Creamos el archivo .txt
    with open('resumen.txt', mode='w') as archivo_txt:
        archivo_txt.write("Resumen de Notas Primer Parcial Programación II\n")
        archivo_txt.write(f"Nota mínima: {minima}\n")
        archivo_txt.write(f"Nota máxima: {maxima}\n")
        archivo_txt.write(f"Nota promedio: {promedio}\n")

# Main, llamamos a las funciones 
crear_archivo_csv() 

datos = leer_archivo_csv() 

crear_resumen_txt(datos)  
