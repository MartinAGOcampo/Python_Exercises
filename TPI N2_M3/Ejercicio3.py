#Crear una función que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. 
# Por cada número, informar cuántos dígitos pares y cuántos impares tiene. 
# Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.

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


