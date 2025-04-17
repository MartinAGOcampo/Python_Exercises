lista = []

print('Vamos a crear una lista con caracteres (palabras o letras)')
print('Luego vamos a revertir el orden de la lista')

# Iniciamos un bucle para pedir los caracteres al usuario
for i in range(5):
        while True: # Verificamos que el ingreso no sea un numero
            character = input('Ingresa una letra o palabra: ')
            if character.isalpha():
                lista.append(character) 
                break
            else:
                print('Tiene que ser una palabra o letra, numeros no estan permitidos')

# Creamos la variable y la revertimos
lista_inv = list(reversed(lista)) 

# Imprimimos ambas listas 
print(f'Las listas quedan conformadas como: {lista} y su inverso {lista_inv}')