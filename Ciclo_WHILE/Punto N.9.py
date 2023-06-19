
valores_temperaturas = int(input("ingrese la cantidad de temperaturas: "))
temperaturas = []

contador = 0
suma = 0
mayor = float('-inf')
menor = float('inf')

while contador < valores_temperaturas:
    temperatura = float(input(f"Ingrese la temperatura {contador + 1}: "))
    temperaturas.append(temperatura)
    
    suma += temperatura
    
    if temperatura > mayor:
        mayor = temperatura
    
    if temperatura < menor:
        menor = temperatura
    
    contador += 1

promedio = suma / valores_temperaturas

print("la temperatura más alta seria:", mayor)
print("la temperatura más baja seria:", menor)
print("promedio de las temperaturas seria:", promedio)