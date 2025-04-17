# Desarrolle un algoritmo que permita leer dos valores A y B 
# Que escriba cuál es el mayor.

# Inicio de algoritmo
while True:
    try:
        num1 = float(input('Ingrese un valor numerico entero o decimal: '))
        num2 = float(input('Ingrese un segundo valor numerico entero o decimal: '))
        
        # Validacion de la consigna <, >, =
        if num1 > num2:
            print(f'El primer número que fue {num1} es mayor que el segundo numero {num2}.')
        elif num1 < num2:
            print(f'El primer número que fue {num1} es menor que el segundo numero {num2}.')
        else:
            print('Es el mismo número.')
    except ValueError:
        print('Ingrese un valor valido')
    
    # Validacion de un segundo intento
    continuar = input('¿Quieres intentar con otro valor? Y / N: ').lower()
    while continuar not in ('n', 'y'):
        print('Ingrese una respuesta correcta por favor (Y/N)')
        continuar = input('¿Quieres intentar con otro valor? Y / N: ').lower()
    if continuar == 'n':
        print('Muy bien, si quieres volver a intentarlo reinicia el programa. Gracias')
        break  