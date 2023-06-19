
Numero_1= int(input("Ingrese el primer numero: "))
Numero_2= int(input("Ingrese el segundo numero: "))

if Numero_1 >= Numero_2:
    print("El primer número debe ser menor que el segundo número.")
else:
    for i in range(Numero_1, Numero_2 + 1):
        print(i)