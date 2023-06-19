
contador_nota = 1
notas = []
suma_nota = 0

while contador_nota <= 3:
    nota = float(input(f"Ingrese la nota {contador_nota}: "))
    notas.append(nota)
    suma_nota += nota
    contador_nota += 1

nota_maxima = max(notas)
nota_minima = min(notas)
promedio = suma_nota / 3

print("La nota más alta es:", nota_maxima)
print("La nota más baja es:", nota_minima)
print("El promedio de las notas es:", promedio)


