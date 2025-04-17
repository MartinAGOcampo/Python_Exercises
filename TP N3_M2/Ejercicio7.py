# Desarrolle un algoritmo que permita leer un valor A 
# Decir si dicho número es positivo, negativo o cero.

# Inicio del algoritmo
while True:
    try:
        X = float(input('Ingrese un valor numerico entero o decimal: '))
        if X > 0: # Validacion de la consigna
            print(f'El número {X} pertenece a los positivos.')
        elif X < 0:
            print(f'El número {X} pertenece a los negativos.')
        else:
            print('Es el mismo número.')
    except ValueError:
        print('Ingrese un valor valido') # Validacion de entradas validas
    
    # Validacion de un segundo intento
    continuar = input('¿Quieres intentar con otro valor? Y / N: ').lower()
    while continuar not in ('n', 'y'):
        print('Ingrese una respuesta correcta por favor (Y/N)')
        continuar = input('¿Quieres intentar con otro valor? Y / N: ').lower()
    if continuar == 'n':
        print('Muy bien, si quieres volver a intentarlo reinicia el programa. Gracias')
        break  