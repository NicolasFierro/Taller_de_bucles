
notas = []

for i in range(4):
    nota = float(input("Ingrese la nota {}: ".format(i+1)))
    notas.append(nota)

maxima = max(notas)
minima = min(notas)
promedio = sum(notas) / len(notas)

print("Nota más alta:", maxima)
print("Nota más baja:", minima)
print("Promedio de notas:", promedio)


