# Desarrolle un algoritmo que permita leer tres valores distintos A, B y C 
# Luego indique el menor de ellos.

# Inicio de algoritmo
while True:
    try:
        A = int(input("Ingrese el valor de A: "))
        B = int(input("Ingrese el valor de B: "))
        C = int(input("Ingrese el valor de C: "))

        # Verificamos que los valores sean distintos
        if A != B and A != C and B != C:
            break
        else:
            print("Por favor, asegúrese de que todos los valores sean distintos.")
    except ValueError:
        print("Ingrese solo números válidos.")

# Determinamos el menor valor
if A < B and A < C:
    menor = A
elif B < A and B < C:
    menor = B
else:
    menor = C

# Imprime el resultado
print(f"El menor valor es: {menor}")
