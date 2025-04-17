def Ejercicio_1 ():
    print('')
    print('Escriba una función que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan')
    while True:
            clave_1 = input('Ingrese su contraseña: ')
            clave_2 = input('Reingrese nuevamente la contraseña: ')
            if clave_1 == clave_2:
                print('Su contraseña fue guardada exitosamente')
                break
            else:
                print('Las contraseñas no coinciden, reintente ')
    print('')
    print('Regresando al menu de opciones')
    print('')

def Ejercicio_2 ():
    print('''
    Escriba una función que simule una caja de ahorros. 
    Solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. 
    A continuación, solicitará una y otra vez las cantidades que se irán ahorrando, 
    hasta que el total ahorrado iguale y no supere al objetivo.''')
    print('')
    
    # Solicitamos el objetivo del ahorro
    while True:
        try:
            Ingreso = float(input('¿Cuánto quieres guardar en total?: $'))
            if Ingreso <= 0:
                print("El objetivo de ahorro debe ser un valor mayor que 0. Intenta nuevamente.")
                continue
            break
        except ValueError:
            print('Solo valores numéricos')

    # Inicializamos el contador de ingresos
    Ingreso_Diario = 0

    # Bucle para ir guardando dinero hasta alcanzar el objetivo
    while Ingreso_Diario < Ingreso:
        try:
            # Se solicita la cantidad a ahorrar
            cantidad = float(input('¿Cuánto quieres guardar parcialmente?: $'))

            # Se valida que la cantidad sea positiva
            if cantidad <= 0:
                print("La cantidad debe ser un valor mayor que 0. Intenta nuevamente.")
                continue

            # Sumamos la cantidad al total ahorrado
            Ingreso_Diario += cantidad

            # Verifica si se ha alcanzado o superado el objetivo
            if Ingreso_Diario > Ingreso:
                Diferencia = Ingreso_Diario - Ingreso
                print(f'El monto ingresado supera el objetivo. Te has excedido en ${Diferencia:.2f}.')
                break  

            # Mostrar el total ahorrado hasta el momento
            print(f'Al momento tienes ahorrado: ${Ingreso_Diario:.2f}')

        except ValueError:
            print('Por favor, ingresa solo valores numéricos.')

    # Mensaje final cuando se alcanza el objetivo
    if Ingreso_Diario >= Ingreso:
        print(f'Felicidades! Has alcanzado tu objetivo! Tu ahorro es de ${Ingreso:.2f}. Excediste el objetivo final por {Diferencia}')
    print('')
    print('Regresando al menu de opciones')
    print('')

def Ejercicio_3 ():
    print("""
    Crear una función que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. 
    Por cada número, informar cuántos dígitos pares y cuántos impares tiene. 
    Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.""")
    print('')

    # Aqui se almacenan los valores pares e impares
    Pares = []
    Impares = []

    # Reglas a tener en cuenta 
    print('Este programa solo admite valores enteros positivos ')
    print('Para finalizar el programa ingrese "0" ')

    # Bucle para pedir y organizar los numeros
    while True:
        try:
            valores = int(input('Ingrese un numero: '))
            
            # En caso de ingreso valores negativos
            if valores < 0 :
                print('Solo valores positivos')
                continue
            
            # En caso de ingreso de 0
            if valores == 0:
                break
            
            # Separamos mediante calculo los valores
            if valores % 2 == 0:
                Pares.append(valores)
            else:
                Impares.append(valores)

            # Vamos notificando la cantidad de valores ingresados 
            print(f'Hasta ahora el total de la lista de numeros pares es de: {len(Pares)} numeros')
            print(f'Hasta ahora el total de la lista de numeros impares es de: {len(Impares)} numeros')
        
        except ValueError:
            print('Ingrese solo valores permitidos')

    # Longitud final de las listas
    print(f'Finalmente el total de la lista de numeros pares es: {len(Pares)}')
    print(f'Finalmente el total de la lista de numeros impares es: {len(Impares)}')
    print('')
    print('Regresando al menu de opciones')
    print('')

def Ejercicio_4 ():
    print('Escribir una función que muestre la sumatoria de todos los múltiplos de 3 encontrados entre el 0 y el 100.')
    print('')
    suma = 0
    contador = 0  

    # Iterar desde 0 hasta 100
    for numero in range(101):
        if numero % 3 == 0:  
            suma += numero    
            contador += 1   

    # Mostramos el resultado
    print(f'Se encontraron {contador} múltiplos de 3 entre 0 y 100.')
    print(f'La sumatoria de todos los múltiplos de 3 entre 0 y 100 es: {suma}')
    print('')
    print('Regresando al menu de opciones')
    print('')

def Ejercicio_5 ():
    print("""
    Escribir una función que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos.
    Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos.
    Cabe recordar que no es posible dividir por cero, por lo que es necesario controlar que la función no permita su ingreso.""")
    print('')

    Positivos = []
    Negativos = 0


    # Bucle para pedir y organizar los numeros
    for i in range (6):
        while True:
            try:
                
                valores = int(input('Ingrese un numero: '))
                
                
                # En caso de ingreso valores negativos
                if valores < 0 :
                    Negativos += valores

                # En caso de ingreso valores positivos
                if valores > 0:
                    Positivos.append(valores)
                
                # En caso de ingreso de 0
                if valores == 0:
                    print('No se puede ingresar el cero')
                    continue
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

    print('')
    print('Regresando al menu de opciones')
    print('')

while True:
        print("Menú de opciones:")
        print('')
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Ejercicio 5")
        print("0. Salir del programa")
        print('')

        
        try:
            opcion = int(input("Selecciona una opción (1-5): "))
            
            if opcion == 1:
                Ejercicio_1()
            elif opcion == 2:
                Ejercicio_2()
            elif opcion == 3:
                Ejercicio_3()
            elif opcion == 4:
                Ejercicio_4()
            elif opcion == 5:
                Ejercicio_5()
            elif opcion == 0:
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intenta nuevamente.")
            
        except ValueError:
            print("Por favor, ingresa un número entero.")

