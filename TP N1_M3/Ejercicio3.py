# Funcion para convertir la fecha 
def convertir_fecha():
    
    meses = {
        "01": "enero", "02": "febrero", "03": "marzo", "04": "abril",
        "05": "mayo", "06": "junio", "07": "julio", "08": "agosto",
        "09": "septiembre", "10": "octubre", "11": "noviembre", "12": "diciembre"
    }
    
    # Validamos la entrada
    while True:
        try:
            fecha = input("Introduce una fecha en formato dd/mm/aaaa: ")
            dia, mes, anio = fecha.split("/")
            
            if mes not in meses:
                print("Mes inválido. Por favor, inténtalo de nuevo.")
                continue
            
            # Mostrar la fecha en el formato solicitado
            print(f"{dia} de {meses[mes]} de {anio}")
            break
        
        except ValueError:
            print("Formato inválido. Por favor, ingresa la fecha en formato dd/mm/aaaa.")

# Llamamos a la funcion
print('Hola ')
convertir_fecha()
print('Gracias!')
