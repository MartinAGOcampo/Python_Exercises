# Funcion para ingreso de datos
def datos():
    info = {
    }

    # No hay restricciones para el ingreso de datos
    nombre = input('Ingresa tu nombre: ').upper()
    info["Nombre"] = nombre

    edad = input('Ingresa tu edad: ')
    info["Edad"] = edad

    direccion = input('Ingresa tu direccion: ').upper()
    info["Direccion"] = direccion

    telefono = input('Ingresa tu telefono: ')
    info["Telefono"] = telefono

    # Se imprime los datos almacenados
    print(f"""
Los datos almacenados son:
          
Nombre: {info['Nombre']}
Edad: {info['Edad']}
Direccion: {info['Direccion']}
Telefono: {info['Telefono']}
    """)

# Llamamos a la funcion
print('Hola ')
datos()
print('Gracias!')






