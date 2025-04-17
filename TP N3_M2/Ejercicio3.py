# Desarrolle un algoritmo que permita leer un valor cualquiera A 
# Escribir si dicho número es múltiplo de Z.

# Inicio de algoritmo
while True:
    try:
        A = int(input('Ingresa el primer número (A): '))
        if A == 0: # Validacion de la entrada
            print('Cero no es un valor válido. Por favor, ingresa un número diferente.')
            continue 
        break
    except ValueError: 
        print('Ingresa un valor válido, solo números enteros.')

# Solicitamos el segundo valor 
while True:
    try:
        Z = int(input('Ingresa el segundo número (Z): '))
        if Z == 0: # Validacion de la entrada
            print('Cero no es un valor válido para Z. Por favor, ingresa un número diferente.')
            continue
        break  
    except ValueError:
        print('Ingresa un valor válido, solo números enteros.')

# Calculo de resultados
if Z == 0:
    print('No se puede dividir por cero, reintenta')
elif A % Z == 0:
    print(f'{A} es multiplo de {Z}')
else:
    print(f'{A} no es multiplo {Z}')
    