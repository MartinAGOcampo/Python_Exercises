# Escribir un programa que permita ingresar la edad en años de una persona
# Luego mostrar “Sos mayor de edad” o “No sos mayor de edad” según la edad ingresada

# Inicio de algoritmo
print('Ingrese su edad para validar si es mayor o menor')

# Validamos la edad
while True:
    try:
        edad = int(input('Introduce tu edad: '))
        if edad >= 18:
            print('Mayor de edad')
        else:
            print('Menor de edad')
    except ValueError:
        print('Ingrese solo valores numéricos')
        # Si ingresan valores no validos el programa lo notificara
        continue  
    
    # Validacion de un segundo intento
    continuar = input('¿Quieres intentar con otro valor? Y / N: ').lower()
    while continuar not in ('n', 'y'):
        print('Ingrese una respuesta correcta por favor (Y/N)')
        continuar = input('¿Quieres intentar con otro valor? Y / N: ').lower()
    if continuar == 'n':
        print('Muy bien, si quieres volver a intentarlo reinicia el programa. Gracias')
        break  