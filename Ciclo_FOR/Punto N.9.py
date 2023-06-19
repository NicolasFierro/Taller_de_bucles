
Numero = int(input("Ingrese el valor"))

if Numero <= 0:
    print("Ingrese un valor superior a 0")

else:
    print("Los divisores de", Numero, "son:")
    for i in range(1, Numero + 1):
        if Numero % i == 0:
            print(i)