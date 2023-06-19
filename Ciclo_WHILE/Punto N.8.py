
numero = int(input("Ingrese un número mayor a cero: "))

while numero <= 0:
    print("El número debe ser mayor a cero.")
    numero = int(input("Ingrese un número mayor a cero: "))

print("Los divisores de", numero, "son:")

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
