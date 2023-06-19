
n= int(input("Ingrese la cantidad de numeros a sumar: "))

if n <= 0:
    print("La cantidad de ser superior a 0")
else:
    suma = 0
    for i in range (1, n+1):
        suma += i
    
    print("La suma de", n, "tendria como resultado ",suma)

