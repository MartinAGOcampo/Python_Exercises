import random 

# Generamos los valores aleatorios 
lista = random.sample(range(1, 11), 10)  # Condicionamos que sean unicos

# Muestro los valores junto con su cuadrado y cubo
for numero in lista:
    cuadrado = numero ** 2  # Calcula el cuadrado
    cubo = numero ** 3  # Calcula el cubo
    print(f'Número: {numero}, el cuadrado es: {cuadrado}, y su cubo es: {cubo}')
