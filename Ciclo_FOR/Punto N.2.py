
numero = int(input("Ingrese un número: "))

if numero > 10:
    multiplicacion = 1
    for i in range(1, 11):
        multiplicacion *= i
    resultado = numero * multiplicacion
    print("El resultado seria:", resultado)
else:
    suma = 0
    for i in range(1, 4):
        suma += i
    resultado = numero + suma
    print("El resultado de la suma es:", resultado)

nombre = input("Ingrese su nombre, por favor: ")

for _ in range(10):
    print(nombre)
