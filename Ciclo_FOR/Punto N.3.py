
valor=int(input("Ingrese el numero: "))

if valor <= 0:
    print("Ingrese un valor superior a cero")

suma= 0
for i in range(0, valor+1, 2):
    suma += i
print("la suma de los pares de", valor, "es:",suma)
