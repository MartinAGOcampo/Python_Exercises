# Escriba una función que solicite una contraseña (el texto de la contraseña no es importante) 
# y la vuelva a solicitar hasta que las dos contraseñas coincidan.

print('Evaluacion')
while True:
        clave_1 = input('Ingrese su clave: ')
        clave_2 = input('Reingrese nuevamente la clave: ')
        if clave_1 == clave_2:
            print('Su clave fue guardada exitosamente')
            break
        else:
            print('Las claves no coinciden, reintente ')
    


