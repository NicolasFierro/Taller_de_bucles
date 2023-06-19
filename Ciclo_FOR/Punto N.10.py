
cantidad = int(input("Ingrese la cantidad de temperaturas a introducir: "))

temperaturas = []

for i in range(cantidad):
    temperatura = float(input("Ingrese la temperatura {}: ".format(i+1)))
    temperaturas.append(temperatura)

maxima_temperatura = max(temperaturas)
minima_temperatura = min(temperaturas)
promedio_temperatura = sum(temperaturas) / cantidad

print("Temperatura más alta seria:", maxima_temperatura)
print("Temperatura más baja seria:", minima_temperatura)
print("Promedio de temperaturas seria:", promedio_temperatura)
