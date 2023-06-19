
numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero:"))

if numero_1 >= numero_2:
    print("El primer número debe ser menor que el segundo número.")
else:
    numero_actual = numero_1
    while numero_actual <= numero_2:
        print(numero_actual)
        numero_actual += 1