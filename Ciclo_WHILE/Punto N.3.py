
numero_suma = int(input("Ingrese el numero para la operacion:"))
resultado = 0
i = 1

while i <= numero_suma:
    resultado += i
    i += 2

print("La suma de los números impares hasta", numero_suma, "es:", resultado)
