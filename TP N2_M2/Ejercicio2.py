# Iniciamos la variable
materias = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []

# Solicitamos la nota de cada materia 
print('Hola, veamos que calificacion obtuviste en cada materia. Veamos!')
for asignatura in materias:
    while True:
        try:
            nota_mat = float(input(f'Cual fue tu calificacion en {asignatura}: '))
            notas.append (nota_mat) # A cada valor agregado por teclado lo introducimos en una nueva lista
            break
        except:
            print('Ese no es un valor permitido! Revisa!')

# Imprimimos el resultado
print('Bien! Como lo veo es:')
for asignatura, nota_final in zip(materias, notas):
    print(f'En {asignatura} te sacaste un {nota_final}')

print('Felicidades en caso de las notas altas, en caso de las bajas a poner esfurezo!')

