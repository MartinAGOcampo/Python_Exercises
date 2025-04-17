# Escriba una función que simule una caja de ahorros. 
# Solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar.
# A continuación, solicitará una y otra vez las cantidades que se irán ahorrando, 
#   hasta que el total ahorrado iguale y no supere al objetivo.

print('Caja de ahorros')

# Solicitamos el objetivo del ahorro
while True:
    try:
        Ingreso = float(input('¿Cuánto quieres guardar en total?: $'))
        if Ingreso <= 0:
            print("El objetivo de ahorro debe ser un valor mayor que 0. Intenta nuevamente.")
            continue
        break
    except ValueError:
        print('Solo valores numéricos')

# Inicializamos el contador de ingresos
Ingreso_Diario = 0

# Bucle para ir guardando dinero hasta alcanzar el objetivo
while Ingreso_Diario < Ingreso:
    try:
        # Se solicita la cantidad a ahorrar
        cantidad = float(input('¿Cuánto quieres guardar parcialmente?: $'))

        # Se valida que la cantidad sea positiva
        if cantidad <= 0:
            print("La cantidad debe ser un valor mayor que 0. Intenta nuevamente.")
            continue

        # Sumamos la cantidad al total ahorrado
        Ingreso_Diario += cantidad

        # Verifica si se ha alcanzado o superado el objetivo
        if Ingreso_Diario > Ingreso:
            Diferencia = Ingreso_Diario - Ingreso
            print(f'El monto ingresado supera el objetivo. Te has excedido en ${Diferencia:.2f}.')
            break  

        # Mostrar el total ahorrado hasta el momento
        print(f'Al momento tienes ahorrado: ${Ingreso_Diario:.2f}')

    except ValueError:
        print('Por favor, ingresa solo valores numéricos.')

# Mensaje final cuando se alcanza el objetivo
if Ingreso_Diario >= Ingreso:
    print(f'¡Felicidades! Has alcanzado tu objetivo de ahorro de ${Ingreso:.2f}. Tambien excediste el objetivo final por {Diferencia}')
