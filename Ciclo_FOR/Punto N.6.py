
tabla_multiplicar = int(input("Ingrese el número de la tabla de multiplicar que desea ver: "))

print("Tabla de multiplicar del", tabla_multiplicar)
for i in range(11):
    resultado = tabla_multiplicar * i
    print(tabla_multiplicar, "x", i, "=", resultado)
