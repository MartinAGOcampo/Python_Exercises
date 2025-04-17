# Escribir un algoritmo que lea los nombres y edades de dos personas 
# Imprima cuál de ellas tiene más edad o si son de la misma edad.

# Inicio de variables
while True:
    try:
        persona1 = str(input('Ingrese solo el nombre, de una persona cualquiera: '))
        edad1 = float(input(f'Ingrese la edad de {persona1}: '))
        while edad1 < 0:
            print('Revisa el valor, no hay nadie con esa edad en el mundo.') # Validamos que se ingrese valores minimos
            edad1 = float(input(f'Ingrese la edad de {persona1}: '))
        persona2 = str(input('Ingrese solo el nombre de otra persona cualquiera: '))
        edad2 = float(input(f'Ingrese la edad de {persona2}: '))
        
        # Corroboramos la consigna
        while edad2 < 0:
            print('Revisa el valor, no hay nadie con esa edad en el mundo.')
            edad2 = float(input(f'Ingrese la edad de {persona2}: '))
        if edad1 > edad2:
            print(f'Aqui {persona1} es mayor que {persona2}.')
        elif edad1 < edad2:
            print(f'En este caso {persona1} es menor que {persona2}.')
        else:
            print(f'Al parecer {persona1} y {persona2} tienen la misma edad.')
    except ValueError:
        print('Ingrese un valor valido')
    
    # Validacion de un segundo intento
    continuar = input('¿Quieres intentar nuevamente? Y / N: ').lower()
    while continuar not in ('n', 'y'):
        print('Ingrese una respuesta correcta por favor (Y/N)')
        continuar = input('¿Quieres intentar nuevamente? Y / N: ').lower()
    if continuar == 'n':
        print('Muy bien, si quieres volver a intentarlo reinicia el programa. Gracias')
        break  