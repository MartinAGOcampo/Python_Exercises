# Escribir una función que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos.
#  Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos.
#  Cabe recordar que no es posible dividir por cero, por lo que es necesario controlar que la función no permita su ingreso.

Positivos = []
Negativos = 0

# Bucle para pedir y organizar los numeros
while True:
    try:
        for i in range (6):
            valores = float(input('Ingrese un numero: '))
            
            # En caso de ingreso valores negativos
            if valores < 0 :
                Negativos += valores

            # En caso de ingreso valores positivos
            if valores > 0 :
                Positivos.append(valores)

            # En caso de ingreso de 0
            if valores == 0:
                print('No se puede ingresar el cero')
                valores = float(input('Ingrese un numero: '))
        break
            
    except ValueError:
        print('Ingrese solo valores permitidos')
if Positivos:
    Promedio = (sum(Positivos) / len(Positivos))
    print(f'El promedio de los valores positivos es: {Promedio}')
else:
    print('No se ingresaron valores positivos, no hay promedio')

if Negativos == 0:
    print('No se insertaron valores negativos')
else:
    print(f'La suma de los valores negativos es {Negativos:.2f}')