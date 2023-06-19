
numero_notas = int(input("Ingrese la cantidad de notas: "))
notas = []
contador = 1
suma = 0

while contador <= numero_notas:
    nota = float(input(f"Ingrese la nota {contador}: "))
    notas.append(nota)
    suma += nota
    contador += 1

promedio = suma / numero_notas

print("El promedio del estudiante es:", promedio)
