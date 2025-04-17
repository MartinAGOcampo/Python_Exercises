while True:
# Interaccion
    print('Ingresa dos numeros por teclado y voy a compararlos')

# Ingreso de datos
    while True:
        try:
            X1 = int(input('Empecemos por el primero '))
            break
        except ValueError:
            print ('No es un valor valido, intenta de vuelta')

    while True:
        try:
            X2 = int(input('Continuemos por el segundo '))
            break
        except ValueError:
            print ('No es un valor valido, intenta de vuelta')

# Comparamos
    if X1 == X2:
        print ('Los numeros son iguales')
    elif X1 < X2:
        print (f'{X1} es menor que {X2}')
    elif X1 > X2:
        print (f'{X1} es mayor que {X2}')

# Verificamos si continuamos o paramos
    Reiniciar = input(str('Deseas repetir el ejercicio? (s/n)'))
    if Reiniciar != 's':
        print('Gracias por participar')
        break
        
