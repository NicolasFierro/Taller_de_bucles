
numero = int(input("Digite un numero: "))
resultado = 0

if numero >10:
    i = 1
    while i <=10:
        resultado += numero * i
        i+=1

else:
    i = 1
    while i <= numero:
        resultado += i
        i += 1

print("El resultado es:", resultado)