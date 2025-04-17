#Escribir un algoritmo que permita calcular al valor absoluto de un número entero X

# Inicio de algoritmo
while True:
    try:
        A = int(input('Ingresa un número para conocer su valor absoluto: '))
        break
    except ValueError:
        print('Ingresa un valor válido, solo números enteros.') # Notificacion de entrada no valida

# Imprime el valor absoluto del numero ingresado
abs = abs(A)
print(f'El valor absoluto del numero ingresado es {abs}')