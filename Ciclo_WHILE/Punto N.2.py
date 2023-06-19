
valor_suma = int(input("Ingrese el valor a sumar: "))
resultado = 0
i = 0

while i <= valor_suma:
    resultado +=i
    i += 2

print("La suma de los pares hasta el valor ",valor_suma, "seria: ",resultado)