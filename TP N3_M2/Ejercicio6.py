# En un almacén se descuenta 20% del precio al cliente si el valor a pagarse es mayor a $200.
# Dado un valor de precio, muestre lo que debe pagar el cliente

# Inicio de algoritmo
while True:
    try:
        monto = float(input('Ingrese el monto a pagar: $'))
        if monto >= 200:
            pagar = monto - (monto * 0.2) # Si el valor es > 200 se le aplica el descuento
            print(f'Obtuviste un descuento del 20% del total a pagar, tu total es: ${pagar}')
        else:
            print(f'Tu monto no aplica para un descuento, tu monto a pagar es: ${monto}')
        break
    except ValueError:
        print('Ingresa valores validos') # Validacion de la entrada
