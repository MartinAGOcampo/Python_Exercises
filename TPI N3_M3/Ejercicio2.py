""""
Escribir un programa que pregunte al usuario por las ventas de un rango de años
y muestre por pantalla un diagrama de líneas con la evolución de las ventas

"""
import matplotlib.pyplot as plt

# Funcion para graficar
def graficar_ventas(ventas):
    if not ventas:
        print("No se ingresaron ventas.")
        return
    
    años = list(ventas.keys())
    valores_ventas = list(ventas.values())
    
    plt.figure(figsize=(10, 6))
    plt.plot(años, valores_ventas, marker='o', linestyle='-', color='b')
    plt.title("Evolución de las Ventas por Año", fontsize=16)
    plt.xlabel("Año", fontsize=14)
    plt.ylabel("Ventas", fontsize=14)
    plt.grid(True)
    plt.show()

# Main
ventas = {}
print("Ingrese las ventas para cada año (ingrese 'fin' para terminar):")

while True:
    año = input("Año: ")
    if año.lower() == 'fin':
        break
    try:
        ventas_año = float(input(f"Ventas para el año {año}: "))
        ventas[año] = ventas_año
    except ValueError:
        print("Por favor, ingrese un número válido para las ventas.") 

graficar_ventas(ventas)
