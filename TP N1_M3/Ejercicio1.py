# Funcion para mostrar la divisa
def mostrar_simbolo_divisa():
    
    # Definimos el diccionario
    divisas = {
        'Euro': '€',
        'Dólar': 'U$S',
        'Yen': '¥',
        'Real': 'R$'
    }
    
    divisa = input("Introduce el nombre de una divisa (Euro, Dólar, Yen, Real): ").capitalize()
    
    # Corroboramos la entrada
    if divisa in divisas:
        print(f"El símbolo de {divisa} es: {divisas[divisa]}")
    else:
        print("La divisa no está en el diccionario.")
        
# Llamamos a la funcion
print('Hola ')
mostrar_simbolo_divisa()
print('Gracias!')


