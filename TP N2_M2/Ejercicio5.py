lista1 = []
lista2 = []


# Ingresamos los valores para la lista 1
print('Ingresa los valores para la lista 1: ')
for i in range(5):
    while True:
        try:
            numero = int(input('Introduce un numero: '))
            lista1.append(numero)
            break
        except ValueError:
            print('Revisa el valor por favor e intentalo nuevamente')

# Ingresamos los valores de la lista 2
print('Ingresa los valores para la lista 2: ')
for i in range(5):
    while True:
        try:
            numero = int(input('Introduce un numero: '))
            lista2.append(numero)
            break
        except:
            print('Revisa el valor por favor e intentalo nuevamente')

lista3 = [] # Creamos la tercera lista para guardar los resultados

# Calculos 
for i in range(5):
    suma = lista1[i] + lista2[i]
    lista3.append(suma)
    print(f'{lista1[i]} + {lista2[i]} = {suma}')

# Imprimimos 
print ('Perfecto, hemos ingresado los valores para las primeras dos listas (lista1 y lista2) y hemos calculado una tercera con los valores sumados ')
print (f'Las listas quedan conformadas por: {lista1}, {lista2}, y {lista3} ')