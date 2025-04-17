# Pedir al usuario la cantidad de artículos y el precio por unidad
cantidad = int(input("Ingrese la cantidad de artículos: "))
precio = float(input("Ingrese el precio por unidad: "))

# Calcular el subtotal sin IVA
subt_s_iva = cantidad * precio

# Aplicar el IVA (21%)
subt_c_iva = subt_s_iva * 1.21

print(f'El costo de los articulos sin el IVA es {subt_s_iva} y con el IVA 21% es {subt_c_iva}')

# Corroborar el descuento
if subt_c_iva > 5000:
    desc = subt_c_iva * 0.90  # Aplicar un descuento del 10%
    print(f'Accediste a un descuento del 10% de {desc - subt_c_iva}'
    f' y tu total a pagar es {desc}')
else:
    sin_desc = subt_c_iva  # No hay descuento
    print('Tu compra no aplica para un descuento')
    print(f"El total a pagar es: {sin_desc:.2f}")