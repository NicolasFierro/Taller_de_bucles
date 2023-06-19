
canitidad_notas = int(input("Ingrese la cantidad de notas: "))

notas = []

for i in range(1, canitidad_notas+1):
    nota = float(input("Ingrese la nota {}: ".format(i)))
    notas.append(nota)

suma = sum(notas)
promedio = suma / canitidad_notas

print("El promedio de las notas es:", promedio)
