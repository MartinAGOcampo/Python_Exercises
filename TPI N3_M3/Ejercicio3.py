"""
Escribir una función que reciba un diccionario con las notas de las asignaturas
de un curso y una cadena con el nombre de un color y devuelva un diagrama de barras
de las notas en el color dado.
"""

import matplotlib.pyplot as plt

notas = {}
print("Ingrese las notas de las asignaturas (ingrese 'fin' para terminar):")
while True:
    asignatura = input("Asignatura: ")
    if asignatura.lower() == 'fin':
        break
    try:
        nota = float(input(f"Nota para {asignatura}: "))
        notas[asignatura] = nota
    except ValueError:
        print("Por favor, ingrese un número válido para la nota.")

colores_disponibles = {
    "1": "rojo",
    "2": "azul",
    "3": "verde",
    "4": "naranja"
}

print("\nSeleccione un color para las barras:")
for key, color in colores_disponibles.items():
    print(f"{key}. {color.capitalize()}")

while True:
    opcion_color = input("Ingrese el número correspondiente al color (1-4): ")
    if opcion_color in colores_disponibles:
        color = colores_disponibles[opcion_color]
        break
    else:
        print("Opción no válida. Por favor, elija un número entre 1 y 4.")

if notas:
    asignaturas = list(notas.keys())
    valores = list(notas.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(asignaturas, valores, color=color)
    plt.title("Notas por Asignatura", fontsize=16)
    plt.xlabel("Asignaturas", fontsize=14)
    plt.ylabel("Notas", fontsize=14)
    plt.ylim(0, 10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
else:
    print("No se ingresaron datos.")

