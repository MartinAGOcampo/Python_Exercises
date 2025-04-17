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





