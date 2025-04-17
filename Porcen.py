# Se pide la cantidad de alumnos, mujeres y hombres
total_alumnos = int(input("Introduce el total de alumnos en el aula: "))
mujeres = int(input("Introduce la cantidad de mujeres: "))
varones = int(input("Introduce la cantidad de varones: "))

# Calculo
if mujeres + varones != total_alumnos:
    print("Error: La suma de mujeres y varones no coincide con el total de alumnos.")
else:
    # Calcular el porcentaje de mujeres y varones
    porcentaje_mujeres = (mujeres / total_alumnos) * 100
    porcentaje_varones = (varones / total_alumnos) * 100
    # Mostrar los resultados
    print("El porcentaje de mujeres es:", porcentaje_mujeres, "%")
    print("El porcentaje de varones es:", porcentaje_varones, "%")
