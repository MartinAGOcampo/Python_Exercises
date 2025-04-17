# Desarrolle un algoritmo que permita leer un valor cualquiera X 
# Escribir si dicho número es par o impar.

# Inicio de algoritmo
while True:
    try:
        X = int(input('Ingrese un valor numerico entero (sin decimales): '))
        if X % 2 == 0 :
            print('Es un numero par')
        else: print('Es un numero impar')
    except ValueError:
        print('Ingrese un valor valido') # Notifica el error en caso de una entrada no valida
    
    # Validacion de un segundo intento
    continuar = input('¿Quieres intentar con otro valor? Y / N: ').lower()
    while continuar not in ('n', 'y'):
        print('Ingrese una respuesta correcta por favor (Y/N)')
        continuar = input('¿Quieres intentar con otro valor? Y / N: ').lower()
    if continuar == 'n':
        print('Muy bien, si quieres volver a intentarlo reinicia el programa. Gracias')
        break  



        