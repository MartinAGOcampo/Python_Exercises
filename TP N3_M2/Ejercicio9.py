# Una frutería ofrece las manzanas con descuento 
# Dado el precio por kilo, y el peso, determinar cuánto pagará una persona que compre manzanas en esa frutería.

# Inicializar variables
precio_por_kilo = 0
kilos_comprados = 0

# Validar la entrada del precio por kilo
while True:
    try:
        precio_por_kilo = float(input("Ingrese el precio por kilo de manzanas: "))
        if precio_por_kilo < 0:
            print("El precio no puede ser negativo. Intente nuevamente.")
            continue
        break  
    except ValueError:
        print("Ingrese un valor numérico válido.")

# Validar la entrada de kilos comprados
while True:
    try:
        kilos_comprados = float(input("Ingrese la cantidad de kilos de manzanas comprados: "))
        if kilos_comprados < 0:
            print("La cantidad de kilos no puede ser negativa. Intente nuevamente.")
            continue
        break  
    except ValueError:
        print("Ingrese un valor numérico válido.")

# Inicializar la variable descuento
descuento = 0

# Calculo del porcentaje de descuento
if 0 <= kilos_comprados <= 2:
    descuento = 0
elif 2.01 <= kilos_comprados <= 5:
    descuento = 10
elif 5.01 <= kilos_comprados <= 10:
    descuento = 15
elif kilos_comprados > 10:
    descuento = 20

# Calcular el total a pagar
total_sin_descuento = precio_por_kilo * kilos_comprados
total_con_descuento = total_sin_descuento - (total_sin_descuento * (descuento / 100))

# Imprime el resultado
print(f"El total a pagar es: {total_con_descuento:.2f}")
